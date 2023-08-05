from pathlib import Path

from src.hashbeaf import utils


def test_run_command() -> None:
    assert utils.run_command("pwd").strip() == str(Path.cwd())
    assert "git version" in utils.run_command("git --version")


def test_ishex() -> None:
    assert utils.ishex("deadbeaf")
    assert utils.ishex("c0de")
    assert not utils.ishex("code")
    assert not utils.ishex("word")


def test_get_hash() -> None:
    for test_string in ("", "abc123", "very_long_strong with \n a newline !@#$"):
        result = utils.get_hash(test_string)
        assert len(result) == 40
        assert utils.ishex(result)
