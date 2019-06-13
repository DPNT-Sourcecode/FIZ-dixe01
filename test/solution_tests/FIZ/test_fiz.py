import unittest
from lib.solutions.FIZ import fizz_buzz_solution as fb

class FizTest(unittest.TestCase):

    def test_returns_number_as_string(self):
        self.assertEqual(fb.fizz_buzz(2), '2')

