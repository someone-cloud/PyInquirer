# Changelog

## [1.0.6] — 2026-07-22

### Fixed
- **List prompt**: Implemented pageSize, vim j/k navigation, multiline wrapping, separator styling
- **Checkbox prompt**: Fixed validation on submit (was a no-op), added vim j/k, Ctrl+A select all
- **Input prompt**: Fixed message callback, numeric defaults, style propagation
- **Confirm prompt**: Added require_enter option for explicit confirmation
- **Expand prompt**: Fixed NameError on plain string choices, fixed default key behavior
- **Editor prompt**: Fixed require_save parameter handling
- **Password prompt**: Added confirm parameter for password confirmation
- **KeyboardInterrupt**: Reset terminal state to prevent garbled output
- **when=False**: Added default value to answers when question is skipped

## [1.0.5] — 2026-07-22
### Fixed
- **prompt not exported**: Fixed circular import; uses lazy import pattern

## [1.0.4] — 2026-07-22
### Added
- Python 3.10–3.12 compatibility
- GitHub Actions CI (Python 3.8–3.12)
- CHANGELOG.md, CONTRIBUTING.md, pyproject.toml
### Fixed
- pygments.token.Token/colllections.Mapping removal error
- prompt_toolkit version lock (<3.1.0 → <4.0.0)
- Various test compatibility issues
- Example cleanup, Token stub for backward compatibility

## [1.0.3] — 2018-11-22
- Bugfix release (original author)
## [1.0.2] — 2018-07-20
- Minor fixes (original author)
## [1.0.1] — 2018-06-14
- Initial PyPI release (original author)
## [1.0.0] — 2018-06-14
- First stable release (original author)
