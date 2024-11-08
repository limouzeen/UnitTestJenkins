import unittest
from xmlrunner import XMLTestRunner  # ใช้ unittest-xml-reporting
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

if __name__ == '__main__':
    # ใช้ XMLTestRunner ในการสร้างรายงานผลลัพธ์การทดสอบเป็น XML
    with open('test-results.xml', 'wb') as output:
        unittest.main(testRunner=XMLTestRunner(output=output), exit=False)
