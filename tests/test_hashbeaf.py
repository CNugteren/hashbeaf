from src.hashbeaf import hashbeaf


def test_commit_data_modify_increment() -> None:
    commit_data = hashbeaf._get_commit_data_original()
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
