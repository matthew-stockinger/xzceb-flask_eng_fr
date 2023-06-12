import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Pepitoooo")
        self.assertEqual(englishToFrench("Hi"), "Bonjour")
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish("Pepitoooo"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Goodbye")

unittest.main()
