import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_bmi_calculates_from_options():
    result = runner.invoke(app, ["bmi", "--height", "1.75", "--weight", "70"])
    assert result.exit_code == 0
    assert "22.86" in result.stdout


@pytest.mark.parametrize(
    ("option", "value"),
    [
        ("--height", "0"),
        ("--height", "-1"),
        ("--height", "nan"),
        ("--weight", "0"),
        ("--weight", "-1"),
        ("--weight", "inf"),
    ],
)
def test_bmi_rejects_invalid_measurements(option, value):
    args = ["bmi", "--height", "1.75", "--weight", "70"]
    args[args.index(option) + 1] = value

    result = runner.invoke(app, args)

    assert result.exit_code != 0
    assert "Error:" in result.stdout
