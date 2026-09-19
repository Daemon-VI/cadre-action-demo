"""Small text statistics: word counts, the most common words, and reading time."""

import re

WORD = re.compile(r"[a-z0-9']+")


def words(text: str) -> list[str]:
    """Lower-cased words, with punctuation stripped. Apostrophes stay inside words ("don't")."""
    return [w.strip("'") for w in WORD.findall(text.lower()) if w.strip("'")]


def word_count(text: str) -> int:
    """How many words the text has."""
    return len(words(text))


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """The n most common words as (word, count), most common first.

    Ties are broken alphabetically, so the result is the same on every run. n <= 0 gives [].
    """
    raise NotImplementedError


def reading_time(text: str, wpm: int = 200) -> int:
    """Whole minutes needed to read the text at wpm words per minute, rounded up.

    Empty text takes 0 minutes; any other text takes at least 1. wpm must be positive, otherwise
    ValueError.
    """
    raise NotImplementedError
