"""Small spelling helper with an intentional bug for contribution practice."""


def correct_spelling(word: str) -> str:
    """Correct a known lowercase misspelling, leaving other words unchanged."""
    corrections = {
        "teh": "the",
        "recieve": "recieve",
    }
    return corrections.get(word, word)
