#test_string_utils.py
import unittest
from string_utils import reverse_string, is_palindrome

class TestStringUtils(unittest.TestCase):

    # Valid input tests for reverse_string
    def test_reverse_string_valid(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("12345"), "54321")

    # Invalid input tests for reverse_string
    def test_reverse_string_invalid(self):
        with self.assertRaises(TypeError):
            reverse_string(None)
        with self.assertRaises(TypeError):
            reverse_string(12345)
        with self.assertRaises(TypeError):
            reverse_string(["h", "e", "l", "l", "o"])

    # Valid input tests for is_palindrome
    def test_is_palindrome_valid(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Level"))  # Case-insensitive
        self.assertTrue(is_palindrome("A"))      # Single character
        self.assertTrue(is_palindrome(""))       # Empty string is a palindrome
        self.assertFalse(is_palindrome("hello"))

    # Invalid input tests for is_palindrome
    def test_is_palindrome_invalid(self):
        with self.assertRaises(TypeError):
            is_palindrome(None)
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(["r", "a", "c", "e", "c", "a", "r"])

if __name__ == "__main__":
    unittest.main()