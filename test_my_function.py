# tests/test_my_function.py
import unittest
from my_function import is_palindrome

class TestIsPalindromeFunction(unittest.TestCase):
    def test_is_palindrome_true(self):
        # คำที่เป็น palindrome
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_is_palindrome_false(self):
        # คำที่ไม่เป็น palindrome
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    unittest.main()
