# -*- coding: utf-8 -*-
"""
`input` type question
"""
import inspect
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.lexers import SimpleLexer

from .common import default_style


def question(message, **kwargs):
    # Fix #151: Allow message as function (#96)
    if callable(message):
        message = message()

    default = kwargs.pop('default', '')
    # Fix #185: pop style first to avoid conflicts with prompt_toolkit
    style = kwargs.pop('style', default_style)
    validate_prompt = kwargs.pop('validate', None)
    if validate_prompt:
        if inspect.isclass(validate_prompt) and issubclass(validate_prompt, Validator):
            kwargs['validator'] = validate_prompt()
        elif callable(validate_prompt):
            class _InputValidator(Validator):
                def validate(self, document):
                    verdict = validate_prompt(document.text)
                    if not verdict == True:
                        if verdict == False:
                            verdict = 'invalid input'
                        raise ValidationError(
                            message=verdict,
                            cursor_position=len(document.text))
            kwargs['validator'] = _InputValidator()

    # Fix #155: convert default to string if number
    if default is not None and not isinstance(default, str):
        default = str(default)

    kwargs['style'] = style
    qmark = kwargs.pop('qmark', '?')


    def _get_prompt_tokens():
        return [
            ('class:questionmark', qmark),
            ('class:question', ' %s  ' % message)
        ]

    return prompt(
        message=_get_prompt_tokens,
        lexer=SimpleLexer('class:answer'),
        default=default,
        **kwargs
    )
