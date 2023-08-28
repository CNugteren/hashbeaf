from pathlib import Path

import pytest

from src.hashbeaf import utils, words


def _run_bash_test(argument: str, working_dir: Path) -> None:
    root_dir = Path(__file__).parent.parent.resolve()
    commands = [
        "git init",
        "touch file.txt",
        "git add file.txt",
        "git commit -m 'Add a file'",
        f"PYTHONPATH={str(root_dir)} python3 -m src.hashbeaf.hashbeaf {argument}",
    ]
    for command in commands:
        utils.run_command(command, working_dir=working_dir)


def _get_hash(working_dir: Path) -> str:
    return utils.run_command("git rev-parse HEAD", working_dir=working_dir)


@pytest.mark.parametrize("target_hash", ("c0de", "beaf"))
def test_end2end_single_arg(tmp_path: Path, target_hash: str) -> None:
    _run_bash_test(target_hash, tmp_path)
    assert target_hash in _get_hash(tmp_path)


def test_end2end_no_arg(tmp_path: Path) -> None:
    _run_bash_test("", tmp_path)
    words_short = [word[:4] for word in words.WORDS]
    assert _get_hash(tmp_path)[:4] in words_short


def test_end2end_two_args(tmp_path: Path) -> None:
    _run_bash_test("c0de beaf", tmp_path)
    actual_hash = _get_hash(tmp_path)
    assert "c0de" in actual_hash or "beaf" in actual_hash
