# PyInquirer (Maintained Fork)

> **PyInquirer has been revived.** The original project was abandoned in 2024 with the maintainer [asking for a successor](https://github.com/CITGuru/PyInquirer/issues/159). This fork picks up where it left off — Python 3.10+ support, modern prompt_toolkit compatibility, and active maintenance.

[![Tests](https://github.com/someone-cloud/PyInquirer/actions/workflows/test.yml/badge.svg)](https://github.com/someone-cloud/PyInquirer/actions/workflows/test.yml)

## What's New in This Fork (v1.0.4)

- **Python 3.10, 3.11, 3.12 support** — Fixed `collections.Mapping` and deprecated `pygments.token.Token` imports that broke on 3.10+
- **prompt_toolkit 3.x compatibility** — Updated dependency bounds to support all prompt_toolkit 3.x releases
- **CI via GitHub Actions** — Tests run on Python 3.8 through 3.12 on every push
- **Bug fixes** — Fixed separator styling for list prompts, improved error handling

## Original PyInquirer

PyInquirer is a collection of common interactive command line user interfaces, based on [Inquirer.js](https://github.com/SBoudrias/Inquirer.js).

### Installation

```bash
pip install PyInquirer
```

If you encounter any prompt_toolkit errors, ensure you have the correct version:

```bash
pip install prompt_toolkit>=3.0.0,<4.0.0
```

### Quickstart

```python
from PyInquirer import prompt

questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': "What's your first name",
    }
]

answers = prompt(questions)
print(answers)
```

### Question Types

PyInquirer supports the following question types:

| Type | Description |
|------|-------------|
| `input` | Free-form text input |
| `confirm` | Yes/no confirmation |
| `list` | Single selection from a list |
| `rawlist` | Numbered list selection |
| `expand` | Expandable choice list with key shortcuts |
| `checkbox` | Multi-select from a list |
| `password` | Masked text input |
| `editor` | Opens external editor for input |

### Examples

See the [`examples/`](examples/) directory for usage examples of each question type:

- [input.py](examples/input.py) — Basic text input
- [confirm.py](examples/confirm.py) — Yes/no prompts
- [list.py](examples/list.py) — Single choice from a list
- [checkbox.py](examples/checkbox.py) — Multiple selections
- [password.py](examples/password.py) — Masked input
- [editor.py](examples/editor.py) — External editor integration
- [expand.py](examples/expand.py) — Expandable choices
- [pizza.py](examples/pizza.py) — Full pizza ordering demo using multiple question types
- [hierarchical.py](examples/hierarchical.py) — Conditional questions with `when`

### Question Properties

Each question dictionary supports these properties:

- `type` — Question type (input, confirm, list, rawlist, expand, checkbox, password, editor)
- `name` — Key name in the answers dictionary
- `message` — The prompt message shown to the user
- `default` — Default value if no input is given
- `choices` — List of choices (for list, rawlist, checkbox, expand)
- `validate` — Validation function receiving user input
- `filter` — Transform function applied to the answer
- `when` — Conditional function to decide if the question should be asked
- `pageSize` — Number of visible lines in list-type prompts

### Styling

Custom styles can be applied using prompt_toolkit's Style:

```python
from prompt_toolkit.styles import Style

custom_style = Style.from_dict({
    'questionmark': '#E91E63 bold',
    'answer': '#2196F3 bold',
    'pointer': '#FF9800 bold',
    'selected': '#4CAF50',
    'separator': '#9E9E9E',
})

answers = prompt(questions, style=custom_style)
```

## Credits

Original project created by [Oyetoke Toby](https://github.com/CITGuru). This fork is maintained by [Zafrul Razeem](https://github.com/someone-cloud).

## License

MIT — see [LICENSE](LICENSE) for details.
