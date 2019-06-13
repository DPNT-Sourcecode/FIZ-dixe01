import unittest
from lib.solutions.FIZ import fizz_buzz_solution as fb

class FizTest(unittest.TestCase):

    def test_returns_number_as_string(self):
        self.assertEqual(fb.fizz_buzz(2), '2')

    def test_returns_fizz_for_3_multiples(self):
        self.assertEqual(fb.fizz_buzz(3), 'fizz fake deluxe')
        self.assertEqual(fb.fizz_buzz(6), 'fizz')
        self.assertEqual(fb.fizz_buzz(996), 'fizz')

    def test_returns_buzz_for_5_multiples(self):
        self.assertEqual(fb.fizz_buzz(25), 'buzz fake deluxe')

    def test_returns_fizz_buzz_for_15_multiples(self):
        self.assertEqual(fb.fizz_buzz(30), 'fizz buzz deluxe')

    def test_returns_fizz_for_nums_with_3_in(self):
        self.assertEqual(fb.fizz_buzz(13), 'fizz')
        self.assertEqual(fb.fizz_buzz(301), 'fizz')

    def test_returns_buzz_for_nums_with_5_in(self):
        self.assertEqual(fb.fizz_buzz(52), 'buzz')
        self.assertEqual(fb.fizz_buzz(502), 'buzz')

    def test_returns_fizz_buzz_for_nums_with_5_and_3(self):
        self.assertEqual(fb.fizz_buzz(352), 'fizz buzz')

    def test_new_deluxe(self):
        self.assertEqual(fb.fizz_buzz(65), 'buzz fake deluxe')
        self.assertEqual(fb.fizz_buzz(36), 'fizz deluxe')
        self.assertEqual(fb.fizz_buzz(30), 'fizz buzz deluxe')
        self.assertEqual(fb.fizz_buzz(405), 'fizz buzz fake deluxe')


