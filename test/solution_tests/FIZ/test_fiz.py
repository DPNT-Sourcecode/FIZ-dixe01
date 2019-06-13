import unittest
from lib.solutions.FIZ import fizz_buzz_solution as fb

class FizTest(unittest.TestCase):

    def test_returns_number_as_string(self):
        self.assertEqual(fb.fizz_buzz(2), '2')

    def test_returns_fizz_for_3s(self):
        self.assertEqual(fb.fizz_buzz(3), 'fizz')
        self.assertEqual(fb.fizz_buzz(6), 'fizz')
        self.assertEqual(fb.fizz_buzz(999), 'fizz')

    def test_returns_buzz_for_5s(self):
        self.assertEqual(fb.fizz_buzz(25), 'buzz')

    def test_returns_fizz_buzz_for_15s(self):
        self.assertEqual(fb.fizz_buzz(30), 'fizz buzz')