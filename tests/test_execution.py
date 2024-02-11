import pytest
from typer.testing import CliRunner
from main import app

@pytest.fixture
def runner():
    return CliRunner()


def test_perform_with_rep(runner):
    result = runner.invoke(app, ["/test_folder", "--rep"])
    assert result.exit_code == 0

def test_perform_with_ctg(runner):
    result = runner.invoke(app, ["/test_folder", "--ctg"])
    assert result.exit_code == 0

def test_perform_with_thr(runner):
    result = runner.invoke(app, ["/test_folder", "--thr", "1"])
    assert result.exit_code == 0

def test_perform_with_dsp(runner):
    result = runner.invoke(app, ["/test_folder", "--dsp"])
    assert result.exit_code == 0

def test_perform_with_all_args(runner):
    result = runner.invoke(app, ["/test_folder", "--rep", "--thr", "1", "--ctg", "--dsp"])
    assert result.exit_code == 0

@pytest.mark.xfail(reason="This test is expected to fail due to value not being provided")
def test_without_value():
    result = runner.invoke(app, ["/test_folder", "--rep", "--thr", "--ctg", "--dsp"])
    assert result.exit_code == 0