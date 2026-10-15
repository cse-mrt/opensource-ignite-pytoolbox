from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()

def test_caesar_shift():
    result = runner.invoke(app, ["caesar", "hello", "--shift", "3"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "khoor"
    