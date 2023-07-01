import argparse
import logging
from typing import List, Tuple

import utils
import words

logger = logging.getLogger(__name__)


def _commit_data_modify_increment(
    commit_data: str, author_increment: int, commit_increment: int
) -> Tuple[str, str, str]:
    lines = commit_data.split("\n")
    author_data_split = lines[2].split(" ")
    commit_data_split = lines[3].split(" ")
    author_timestamp = int(author_data_split[-2]) + author_increment
    commit_timestamp = int(commit_data_split[-2]) + commit_increment
    author_time_full = f"{author_timestamp} {author_data_split[-1]}"
    commit_time_full = f"{commit_timestamp} {commit_data_split[-1]}"
    author_line = " ".join([*author_data_split[:-2], author_time_full])
    commit_line = " ".join([*commit_data_split[:-2], commit_time_full])
    modified_commit_data = "\n".join([lines[0], lines[1], author_line, commit_line, *lines[4:]])
    return modified_commit_data, author_time_full, commit_time_full


def hashbeaf_main(words: List[str], max_minutes_in_future: int) -> None:
    words = [word.lower() for word in words]
    for word in words:
        if not utils.ishex(word):
            raise RuntimeError(
                f"User input '{word}' contains non-hexadecimal characters, aborting."
            )

    commit_data_original = utils.run_command("git cat-file commit HEAD")
    for commit_increment in range(max_minutes_in_future * 60):
        for author_increment in range(commit_increment + 1):
            (commit_data, author_time_full, commit_time_full) = _commit_data_modify_increment(
                commit_data_original, author_increment, commit_increment
            )
            new_hash = utils.get_hash(commit_data)
            for word in words:
                if new_hash.startswith(word):
                    if commit_increment == author_increment == 0:
                        logger.info("The current hash is already nice, nothing to do")
                        return
                    result = utils.run_command(
                        f"GIT_COMMITTER_DATE='{commit_time_full}' "
                        f"git commit --amend -C HEAD --date='{author_time_full}'"
                    )
                    print(result)
                    return

    logger.info("Did not find a nice hash, retry with a shorter word or more minutes in the future")


if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser("Change the last commit to a commit hash with words you like")
    parser.add_argument("words", type=str, nargs="?", default=words.WORDS)
    parser.add_argument("--max_minutes_in_future", type=int, default=15)
    hashbeaf_main(**vars(parser.parse_args()))
