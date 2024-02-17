import unittest
from hangman.main import *

class TestHangman(unittest.TestCase):
    def testEncapsulate(self):
        word = "South Africa"
        filteredWord = encapsulate(word)[1]
        encapsulatedWord = encapsulate(word)[0]

        self.assertEqual(filteredWord, "SOUTHAFRICA")

if __name__ == '__main__':
    unittest.main()