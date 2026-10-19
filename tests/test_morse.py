from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_morse_encode_sos():
    result = runner.invoke(app, ["morse", "SOS"])

    assert result.exit_code == 0
    assert "... --- ..." in result.stdout


def test_morse_decode_sos():
    result = runner.invoke(app, ["morse", "... --- ...", "--decode"])

    assert result.exit_code == 0
    assert "SOS" in result.stdout


def test_morse_invalid_character():
    result = runner.invoke(app, ["morse", "hello@"])

    assert result.exit_code == 1
    assert "Invalid character" in result.stdout


def test_morse_invalid_code():
    result = runner.invoke(app, ["morse", "......--", "--decode"])

    assert result.exit_code == 1
    assert "Invalid Morse code" in result.stdout
