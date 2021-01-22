import unittest
import input_check

class PasswordTest(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(input_check.character_check("testcase", "username", 5, 10, r"[^\w\.]+"))

    def test_length(self):
        expected = print("The username must be between 5 and 10 characters.")
        self.assertEqual(input_check.character_check("", "username", 5, 10, r"[^\w\.]+"), expected)
        self.assertEqual(input_check.character_check("pw", "username", 5, 10, r"[^\w\.]+"), expected)
        self.assertEqual(input_check.character_check("too_long_password_example", "username", 5, 10, r"[^\w\.]+"), expected)

    def test_char_set(self):
        expected = print("The username can only contain letters, numbers and underscores.")
        self.assertEqual(input_check.character_check("pass word", "username", 5, 10, r"[^\w\.]+"), expected)
        self.assertEqual(input_check.character_check("p@ssword", "username", 5, 10, r"[^\w\.]+"), expected)
        self.assertEqual(input_check.character_check("pass-w", "username", 5, 10, r"[^\w\.]+"), expected)

unittest.main()
