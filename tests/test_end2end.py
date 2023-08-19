from pathlib import Path

from src.hashbeaf import utils


def test_end2end(tmp_path: Path) -> None:
    root_dir = Path(__file__).parent.parent.resolve()
    target_hash = "c0de"
    commands = [
        "git init",
        "touch file.txt",
        "git add file.txt",
        "git commit -m 'Add a file'",
        f"PYTHONPATH={str(root_dir)} python3 -m src.hashbeaf.hashbeaf {target_hash}",
    ]
    for command in commands:
        utils.run_command(command, working_dir=tmp_path)
    assert target_hash in utils.run_command("git rev-parse HEAD", working_dir=tmp_path)
