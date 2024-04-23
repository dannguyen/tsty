import pytest
from click.testing import CliRunner
from tsty.cli import cli


def pytest_sessionfinish(session, exitstatus):
    """test_cli screws up the terminal colors, so this resets them to something usable"""

    CliRunner().invoke(
        cli,
        [
            "reset",
        ],
    )
