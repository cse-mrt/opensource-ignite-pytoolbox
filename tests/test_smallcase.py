from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_smallcase_converts_text_to_lowercase():
    result = runner.invoke(app, ["smallcase", "HELLO WORLD"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "hello world"


def test_smallcase_handles_apostrophes():
    result = runner.invoke(app, ["smallcase", "DON'T STOP"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "don't stop"