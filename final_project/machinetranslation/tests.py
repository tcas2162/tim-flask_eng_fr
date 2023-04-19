from translator import english_to_french, french_to_english
import unittest

class TestTranslateFunctions(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(french_to_english(' '), ' ')

    def test_null(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'),'Hello' )

    def test_new_line(self):
        self.assertEqual(english_to_french(
            "I learned to code in Python.\nHello"),
            "J'ai appris à coder en Python.\nBonjour"
        )
        self.assertEqual(french_to_english(
            "J'ai appris à coder en Python.\nBonjour"),
            "I learned to code in Python.\nHello"
        )

    def test_untranslatable(self):
        self.assertNotEqual(english_to_french(
            "こんにちは"),
            None
        )
        self.assertNotEqual(french_to_english(
            "こんにちは"),
            None
        )
    
if __name__ == '__main__':
    unittest.main()
