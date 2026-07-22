# Changelog

## [1.0.4] — 2026-07-22

### Added
- Python 3.10, 3.11, 3.12 support — full compatibility restored after the `collections.Mapping` removal in Python 3.10 broke the original
- GitHub Actions CI — tests run on Python 3.8 through 3.12 on every push and pull request
- Official badge for CI status in README
- This changelog

### Fixed
- **Python 3.10+ crash**: Removed `pygments.token.Token` import (deprecated and internally used `collections.Mapping` which was removed in 3.10). Added backward-compatible `Token` stub class.
- **prompt_toolkit version lock**: Updated dependency bounds from `<3.1.0` to `<4.0.0`, enabling compatibility with all modern prompt_toolkit 3.x releases
- **`PosixPipeInput` API compat**: Fixed test helpers to work with prompt_toolkit ≥3.0.30 which changed constructor signature
- **Example cleanup**: Removed deprecated `Token` import from example files

### Changed
- Version bump: 1.0.3 → 1.0.4
- Python minimum version: 3.6 → 3.8
- Removed Python 2.7 classifier (EOL 2020)
- Development status: Planning → Beta
- Replaced README.rst with README.md (modern, better rendering on GitHub)
- Replaced dead `.travis.yml` with GitHub Actions workflow

### Removed
- `.travis.yml` — Travis CI for open source ended in 2021

## [1.0.3] — 2018-11-22
- Bugfix release (by original author)

## [1.0.2] — 2018-07-20
- Minor fixes (by original author)

## [1.0.1] — 2018-06-14
- Initial PyPI release (by original author)

## [1.0.0] — 2018-06-14
- First stable release (by original author)
