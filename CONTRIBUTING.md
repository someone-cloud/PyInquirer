# Contributing to PyInquirer

Thanks for wanting to contribute to PyInquirer! This project was revived from abandonment in 2026 and is actively seeking maintainers and contributors.

## Issues

- **Bug reports**: Open an issue with the bug template. Include Python version, OS, and a minimal reproduction.
- **Feature requests**: Open an issue with the feature template. Describe what you're building and why.
- **Questions**: Use the Discussions tab.

## Pull Requests

1. **Fork** the repo and create your branch from `master`.
2. **Install locally**: `pip install -e ".[dev]"`
3. **Make your changes**. Keep them focused — one feature or fix per PR.
4. **Add or update tests** for your changes.
5. **Run tests**: `pytest tests/`
6. **Commit** with a clear message following conventional commits:
   - `fix:` — bug fix
   - `feat:` — new feature
   - `docs:` — documentation
   - `test:` — testing
   - `refactor:` — code change without feature/bug
7. **Push** and open a PR.

## Code Style

- Follow PEP 8
- Use type hints where practical
- Keep line length under 100 characters
- Write docstrings for public APIs

## Testing

Tests use pytest with pty-based terminal simulation. Run locally:

```bash
pip install -e ".[dev]"
pytest -sv tests/
```

Some tests require an interactive terminal and may be skipped on CI.

## Release Process

1. Bump version in `PyInquirer/__init__.py` and `setup.py`
2. Update `CHANGELOG.md`
3. Create a signed tag: `git tag -s v1.0.5 -m "v1.0.5"`
4. Push tag: `git push origin v1.0.5`
5. GitHub Actions builds and publishes to PyPI

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
