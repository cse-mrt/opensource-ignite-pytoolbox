import pytest

from pytoolbox.spelling import correct_spelling


def test_correct_spelling_teh():
    assert correct_spelling("teh") == "the"


def test_correct_spelling_leaves_unknown_words_unchanged():
    assert correct_spelling("hello") == "hello"


def test_correct_spelling_preserves_correct_word():
    assert correct_spelling("receive") == "receive"


@pytest.mark.xfail(strict=True, reason="Practice bug: recieve should become receive")
def test_correct_spelling_recieve():
    assert correct_spelling("recieve") == "receive"
