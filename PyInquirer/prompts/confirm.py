# -*- coding: utf-8 -*-
"""
confirm type question
"""
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.styles import Style


def question(message, **kwargs):
    # Fix #48: add require_enter option
    require_enter = kwargs.pop('require_enter', False)
    default = kwargs.pop('default', True)

    style = kwargs.pop('style', Style.from_dict({
        'questionmark': '#5F819D',
        'instruction': '',
        'answer': '#FF9D00 bold',
        'question': 'bold',
    }))
    status = {'answer': None}

    qmark = kwargs.pop('qmark', '?')

    def get_prompt_tokens():
        tokens = []

        tokens.append(('class:questionmark', qmark))
        tokens.append(('class:question', ' %s ' % message))
        if isinstance(status['answer'], bool):
            tokens.append(('class:answer', ' Yes' if status['answer'] else ' No'))
        else:
            if default:
                instruction = ' (Y/n)' if not require_enter else ' (Y/n, Enter to confirm)'
            else:
                instruction = ' (y/N)' if not require_enter else ' (y/N, Enter to confirm)'
            tokens.append(('class:instruction', instruction))
        return tokens

    # key bindings
    kb = KeyBindings()

    @kb.add('c-q', eager=True)
    @kb.add('c-c', eager=True)
    def _(event):
        raise KeyboardInterrupt()

    @kb.add('n')
    @kb.add('N')
    def key_n(event):
        status['answer'] = False
        if not require_enter:
            event.app.exit(result=False)
        # If require_enter, wait for Enter

    @kb.add('y')
    @kb.add('Y')
    def key_y(event):
        status['answer'] = True
        if not require_enter:
            event.app.exit(result=True)
        # If require_enter, wait for Enter

    @kb.add('enter', eager=True)
    def set_answer(event):
        if require_enter and status['answer'] is None:
            # Enter without Y/N = use default
            status['answer'] = default
        if status['answer'] is not None:
            event.app.exit(result=status['answer'])
        # If no answer selected yet, just submit default
        if status['answer'] is None:
            event.app.exit(result=default)

    return PromptSession(
        message=get_prompt_tokens,
        key_bindings=kb,
        mouse_support=False,
        style=style,
        erase_when_done=False,
    )
