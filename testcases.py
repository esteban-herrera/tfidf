import unittest
import tfidf

class TestTFIDF(unittest.TestCase):
    def test_nofiles(self):
        tfidf.count_dir("nofiles")
        self.assertTrue(len(tfidf.counts)==0, "no files in dir")
    def test_empty(self):
        tfidf.count_dir("empty")
        self.assertTrue(len(tfidf.counts)==1, "single empty file")
    def test_word1(self):
        tfidf.count_dir("word_1")
        self.assertTrue(len(tfidf.counts)==1, "single file with 1 word")

if __name__ == '__main__':
    unittest.main()
