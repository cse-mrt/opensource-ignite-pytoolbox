from typer.testing import CliRunner
from pytoolbox.cli import app

runner = CliRunner()


def test_hexrgb_orange():
    result = runner.invoke(app, ["hexrgb", "#FF8800"])
    assert result.exit_code == 0
    assert "R=255 G=136 B=0" in result.stdout


def test_hexrgb_black():
    result = runner.invoke(app, ["hexrgb", "#000000"])
    assert result.exit_code == 0
    assert "R=0 G=0 B=0" in result.stdout


def test_hexrgb_invalid_length():
    result = runner.invoke(app, ["hexrgb", "#FF88"])
    assert result.exit_code != 0