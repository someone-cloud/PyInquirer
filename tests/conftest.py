import os
import pytest

# PTY-based tests require a real interactive terminal and are sensitive
# to prompt_toolkit version differences. Skip on CI to avoid flakes.
def pytest_collection_modifyitems(config, items):
    if os.environ.get('CI') == 'true':
        skip_pty = pytest.mark.skip(reason='PTY-based test, skipped on CI')
        for item in items:
            if 'example' in item.nodeid:
                item.add_marker(skip_pty)
