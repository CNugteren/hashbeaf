from src.hashbeaf import utils, words


def test_words() -> None:
    for word in words.WORDS:
        assert utils.ishex(word)
