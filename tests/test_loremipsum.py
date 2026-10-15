from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_loremipsum_word_count():
    result = runner.invoke(app, ["loremipsum", "--words", "20"])
    assert result.exit_code == 0
    words = result.stdout.strip().split()
    assert len(words) == 20
    assert words[0].lower().startswith("lorem")


def test_loremipsum_single_word():
    result = runner.invoke(app, ["loremipsum", "--words", "1"])
    assert result.exit_code == 0
    assert result.stdout.strip().split() == ["lorem"]
