import unittest
from lib.solutions.HLO import hello_solution

class HelloTest(unittest.TestCase):

    def test_says_hello_to_friend(self):
        self.assertEqual(hello_solution.hello('David'), 'Hello, David!')




