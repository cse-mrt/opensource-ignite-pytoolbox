from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_wordcount_basic(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("hello world\n")
    result = runner.invoke(app, ["wordcount", str(path)])
    assert result.exit_code == 0
    assert "Words: 2" in result.stdout


def test_wordcount_multiple_spaces(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("hello   world")
    result = runner.invoke(app, ["wordcount", str(path)])
    assert result.exit_code == 0
    assert "Words: 2" in result.stdout
