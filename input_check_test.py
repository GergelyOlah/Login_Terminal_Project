import unittest
import input_check

class PasswordTest(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(input_check.character_check("testcase"))

    def test_length(self):
        expected = print("The password must be between 3 and 10 characters.")
        self.assertEqual(input_check.character_check(""), expected)
        self.assertEqual(input_check.character_check("pw"), expected)
        self.assertEqual(input_check.character_check("too_long_password_example"), expected)

    def test_char_set(self):
        expected = print("The password can only contain letters, numbers and underscores.")
        self.assertEqual(input_check.character_check("pass word"), expected)
        self.assertEqual(input_check.character_check("p@ssword"), expected)
        self.assertEqual(input_check.character_check("pass-w"), expected)

unittest.main()
