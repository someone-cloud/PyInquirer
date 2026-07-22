# -*- coding: utf-8 -*-
"""
`list` type question
"""
from prompt_toolkit.application import Application, get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.filters import IsDone
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import ConditionalContainer, HSplit
from prompt_toolkit.layout.dimension import LayoutDimension as D
from prompt_toolkit.layout import Layout
from prompt_toolkit.shortcuts import PromptSession

from . import PromptParameterException
from ..separator import Separator
from .common import if_mousedown, default_style, setup_simple_validator

# custom control based on FormattedTextControl


class InquirerControl(FormattedTextControl):
    def __init__(self, choices, default, **kwargs):
        self.selected_option_index = 0
        self.answered = False
        self.choices = choices
        self._init_choices(choices, default)
        super().__init__(self._get_choice_tokens, **kwargs)

    def _init_choices(self, choices, default):
        # helper to convert from question format to internal format
        self.choices = []  # list (name, value, disabled)
        searching_first_choice = True
        for i, c in enumerate(choices):
            if isinstance(c, Separator):
                self.choices.append((c, None, None))
            else:
                if isinstance(c, str):
                    self.choices.append((c, c, None))
                else:
                    name = c.get('name')
                    value = c.get('value', name)
                    disabled = c.get('disabled', None)
                    self.choices.append((name, value, disabled))
                    # Fix #78: don't auto-select disabled choices
                    if value == default and not disabled:
                        self.selected_option_index = i
                        searching_first_choice = False
                if searching_first_choice and not self.choices[-1][2]:
                    self.selected_option_index = i
                    searching_first_choice = False
                if default and (default == i or default == c):
                    self.selected_option_index = i
                    searching_first_choice = False

    @property
    def choice_count(self):
        return len(self.choices)

    def _get_choice_tokens(self):
        tokens = []

        def append(index, choice):
            selected = (index == self.selected_option_index)

            @if_mousedown
            def select_item(mouse_event):
                # bind option with this index to mouse event
                self.selected_option_index = index
                self.answered = True
                try:
                    get_app().exit(result=self.get_selection()[0])
                except Exception:
                    pass

            if isinstance(choice[0], Separator):
                tokens.append(('class:separator', '  %s\n' % choice[0]))
            else:
                tokens.append(('class:pointer' if selected else '', ' \u276f ' if selected
                else '   '))
                if selected:
                    tokens.append(('[SetCursorPosition]', ''))
                if choice[2]:  # disabled
                    tokens.append(('class:Selected' if selected else '',
                                   '- %s (%s)' % (choice[0], choice[2])))
                else:
                    try:
                        tokens.append(('class:Selected' if selected else '', str(choice[0]),
                                    select_item))
                    except:
                        tokens.append(('class:Selected' if selected else '', choice[0],
                                    select_item))
                tokens.append(('', '\n'))

        # prepare the select choices
        for i, choice in enumerate(self.choices):
            append(i, choice)
        tokens.pop()  # Remove last newline.
        return tokens

    def get_selection(self):
        return self.choices[self.selected_option_index]


def question(message, **kwargs):
    if not 'choices' in kwargs:
        raise PromptParameterException('choices')

    choices = kwargs.pop('choices', None)
    default = kwargs.pop('default', None)
    qmark = kwargs.pop('qmark', '?')
    # Fix #185: use default_style if no style provided
    style = kwargs.pop('style', default_style)
    # Fix #54/#183: implement pageSize
    page_size = kwargs.pop('pageSize', kwargs.pop('page_size', None))
    # Fix #107: allow disabling mouse support
    mouse_support = kwargs.pop('mouse_support', True)

    ic = InquirerControl(choices, default=default)

    def get_prompt_tokens():
        tokens = []

        tokens.append(('class:questionmark', qmark))
        tokens.append(('class:question', ' %s ' % message))
        if ic.answered:
            tokens.append(('class:answer', ' ' + ic.get_selection()[0]))
        else:
            tokens.append(('class:instruction', ' (Use arrow keys)'))
        return tokens

    # Fix #166: allow multiline messages by not fixing height to exact 1
    window_height = D(min=1)
    if page_size:
        window_height = D(min=min(3, page_size), max=page_size + 1)

    layout = HSplit([
        Window(height=D.exact(1),
               content=FormattedTextControl(get_prompt_tokens)
        ),
        ConditionalContainer(
            Window(ic, height=window_height),
            filter=~IsDone()
        )
    ])

    # key bindings
    kb = KeyBindings()

    @kb.add('c-q', eager=True)
    @kb.add('c-c', eager=True)
    def _(event):
        raise KeyboardInterrupt()
        # event.app.exit(result=None)

    # Fix #138/#87: add vim-style navigation
    @kb.add('down', eager=True)
    @kb.add('j', eager=True)
    def move_cursor_down(event):
        def _next():
            ic.selected_option_index = (
                (ic.selected_option_index + 1) % ic.choice_count)
        _next()
        while isinstance(ic.choices[ic.selected_option_index][0], Separator) or\
                ic.choices[ic.selected_option_index][2]:
            _next()

    @kb.add('up', eager=True)
    @kb.add('k', eager=True)
    def move_cursor_up(event):
        def _prev():
            ic.selected_option_index = (
                (ic.selected_option_index - 1) % ic.choice_count)
        _prev()
        while isinstance(ic.choices[ic.selected_option_index][0], Separator) or \
                ic.choices[ic.selected_option_index][2]:
            _prev()

    @kb.add('enter', eager=True)
    def set_answer(event):
        ic.answered = True
        event.app.exit(result=ic.get_selection()[1])

    return Application(
        layout=Layout(layout),
        key_bindings=kb,
        mouse_support=mouse_support,
        style=style
    )
