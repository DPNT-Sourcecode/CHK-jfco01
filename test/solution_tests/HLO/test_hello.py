import unittest

from solutions.HLO import hello_solution


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello("Jim"), "Hello, Jim!")

    def test_hello_number(self):
        with self.assertRaises(TypeError):
            hello_solution.hello(1)

    def test_hello_blank(self):
        with self.assertRaises(ValueError):
            hello_solution.hello("")

if __name__ == '__main__':
    unittest.main()
