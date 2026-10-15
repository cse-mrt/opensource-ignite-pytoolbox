import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_unitconvert_simple():
    result = runner.invoke(app, ["unitconvert","10","kg","g"])
    assert result.exit_code == 0
    assert "10000g" in result.stdout


def test_unitconvert_unrecognized_unit():
    result = runner.invoke(app, ["unitconvert","10","apple","car"])
    assert result.exit_code == 1
    assert "Error: invalid unit found" in result.stdout
    
    
def test_unitconvert_unitCatogary_mismatch():
    result = runner.invoke(app, ["unitconvert","10","kg","f"])
    assert result.exit_code == 1
    assert "Error: units does not match" in result.stdout
    
def test_unitconvert_negativeValue():
    result = runner.invoke(app, ["unitconvert","--","-10","kg","g"])
    assert result.exit_code == 1
    assert "Error: value must be greater than 0" in result.stdout