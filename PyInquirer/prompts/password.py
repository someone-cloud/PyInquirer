# -*- coding: utf-8 -*-
"""
`password` type question
"""
from . import input


def question(message, **kwargs):
    kwargs['is_password'] = True
    
    # Fix #53: add confirm parameter for password confirmation
    confirm_pw = kwargs.pop('confirm', False)
    
    if confirm_pw:
        # Import prompt here to avoid circular dependency
        from . import input as input_module
        
        pw1 = input_module.question(message, **kwargs)
        if pw1:
            # Create a separate kwargs copy for confirmation
            confirm_kwargs = kwargs.copy()
            confirm_kwargs['is_password'] = True
            confirm_msg = kwargs.pop('confirm_message', 'Confirm password: ')
            pw2 = input_module.question(confirm_msg, **confirm_kwargs)
            if pw1 != pw2:
                raise ValueError('Passwords do not match!')
        return pw1
    
    return input.question(message, **kwargs)
