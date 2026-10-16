import json

import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_csv2json_runs(tmp_path):
    path = tmp_path / "data.csv"
    path.write_text("name,age\nalice,30\nbob,25\n")
    result = runner.invoke(app, ["csv2json", str(path)])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert isinstance(data, list)


@pytest.mark.xfail(strict=True, reason="See ISSUES.md #10")
def test_csv2json_keeps_first_row(tmp_path):
    path = tmp_path / "data.csv"
    path.write_text("name,age\nalice,30\nbob,25\n")
    result = runner.invoke(app, ["csv2json", str(path)])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data == [{"name": "alice", "age": "30"}, {"name": "bob", "age": "25"}]


def test_csv2json_missing_file():
    result = runner.invoke(app, ["csv2json", "does-not-exist.csv"])
    assert result.exit_code != 0
    assert "Error: file not found: does-not-exist.csv" in result.output
