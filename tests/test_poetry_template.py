from click.testing import CliRunner

from poetry_template import __version__
from poetry_template.main import hello


def test_version():
    assert __version__ == "0.1.0"


def test_output():
    runner = CliRunner()
    result = runner.invoke(hello, ["Bob"])
    assert result.exit_code == 0
    assert result.output == "Hello, Bob!\n"
