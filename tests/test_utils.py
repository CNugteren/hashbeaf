from src.hashbeaf import utils


def test_ishex() -> None:
    assert utils.ishex("deadbeaf")
    assert utils.ishex("c0de")
    assert not utils.ishex("code")
    assert not utils.ishex("word")
