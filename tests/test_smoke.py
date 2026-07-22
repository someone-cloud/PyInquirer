def test_import():
    """Verify the package imports successfully."""
    import PyInquirer
    from PyInquirer import prompt, print_json, Separator, Validator, ValidationError
    assert PyInquirer.__version__ == '1.0.4'


def test_style_from_dict():
    """Verify style_from_dict backward compatibility."""
    from PyInquirer import style_from_dict
    style = style_from_dict({'questionmark': '#ff0000'})
    assert style is not None


def test_prompt_parameter_exception():
    """Verify prompt raises PromptParameterException with missing fields."""
    from PyInquirer import prompt
    try:
        prompt([{'type': 'input'}])
        assert False, 'Should have raised'
    except Exception as e:
        assert 'message' in str(e) or 'name' in str(e)
