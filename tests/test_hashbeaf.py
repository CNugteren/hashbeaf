import pytest

from src.hashbeaf import hashbeaf


EXPECTED_COMMIT_DATA = """tree 889ba39969dbfe2b1633b24dcd52195242f2d925
parent c0de41075e60cff5b31c8d56ad8d31b4ffc44306
author The Doctor <the@doctor.co.uk> 1691226217 +0200
committer The Doctor <the@doctor.co.uk> 1691226249 +0200

This commit is great
"""

UNEXPECTED_COMMIT_DATA = """tree ba5f96b189c1c41f849f5046a270d6fa4d8d410a
parent 40037581b186fce93c4748f186a51d6997ed631e
parent cafec85e464a03...GP SIGNATURE-----

Merge cafec85e464a03ee55b6444a4553808639570fdd into 40037581b186fce93c4748f186a51d6997ed631e
"""


@pytest.mark.parametrize(
    "commit_data",
    (
        EXPECTED_COMMIT_DATA,
        UNEXPECTED_COMMIT_DATA,
        hashbeaf._get_commit_data_original(),
    ),
)
def test_commit_data_modify_increment(commit_data: str) -> None:
    if "author " not in commit_data or "committer " not in commit_data:
        print(f"Received unexpected commmit-data:\n{commit_data}")
        return  # skipping this test
    modified_commit_data, _, _ = hashbeaf._commit_data_modify_increment(commit_data, 0, 0)
    assert modified_commit_data == commit_data
    for author_incr in range(0, 3):
        for commit_incr in range(0, 3):
            (
                modified_commit_data,
                author_time_full,
                commit_time_full,
            ) = hashbeaf._commit_data_modify_increment(commit_data, author_incr, commit_incr)
            assert author_time_full in modified_commit_data
            assert commit_time_full in modified_commit_data
            assert len(modified_commit_data.split("\n")) == 7
