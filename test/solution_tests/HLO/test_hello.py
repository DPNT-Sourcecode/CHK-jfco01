import unittest

from solutions.HLO import hello_solution


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello("John"), "Hello, John!")

if __name__ == '__main__':
    unittest.main()
