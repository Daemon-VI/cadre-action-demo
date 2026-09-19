import unittest

from textstats import reading_time, top_words, word_count, words


class Words(unittest.TestCase):
    def test_punctuation_and_case(self):
        self.assertEqual(words("Hello, hello! Don't stop."), ["hello", "hello", "don't", "stop"])

    def test_count(self):
        self.assertEqual(word_count("one two  three\nfour"), 4)
        self.assertEqual(word_count(""), 0)


class TopWords(unittest.TestCase):
    def test_most_common_first(self):
        self.assertEqual(top_words("b a b c b a", 2), [("b", 3), ("a", 2)])

    def test_ties_are_alphabetical(self):
        self.assertEqual(top_words("pear apple fig", 3), [("apple", 1), ("fig", 1), ("pear", 1)])

    def test_edges(self):
        self.assertEqual(top_words("", 3), [])
        self.assertEqual(top_words("a a b", 0), [])
        self.assertEqual(top_words("a a b", 10), [("a", 2), ("b", 1)])


class ReadingTime(unittest.TestCase):
    def test_rounds_up(self):
        self.assertEqual(reading_time("word " * 200), 1)
        self.assertEqual(reading_time("word " * 201), 2)
        self.assertEqual(reading_time("word " * 30, wpm=10), 3)

    def test_edges(self):
        self.assertEqual(reading_time(""), 0)
        self.assertEqual(reading_time("hi"), 1)
        with self.assertRaises(ValueError):
            reading_time("hi", wpm=0)


if __name__ == "__main__":
    unittest.main()
