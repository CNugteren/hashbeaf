import hashlib
import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def run_command(command: str, working_dir: Path = Path.cwd()) -> str:
    result = subprocess.run(
        command, shell=True, capture_output=True, encoding="utf-8", cwd=str(working_dir)
    )
    if result.returncode != 0:
        logger.info(f"'{command}' failed:\n{result.stdout}{result.stderr}")
        result.check_returncode()
    return result.stdout


def ishex(word: str) -> bool:
    return all(c in "0123456789abcdef" for c in word)


def get_hash(text: str) -> str:
    header = "commit " + str(len(text)) + "\0"
    full_text = (header + text).encode("utf-8")
    return hashlib.sha1(full_text).hexdigest()
