import unittest

from solutions.CHK import checkout_solution


class TestHello(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("AABBBBCDDD"), 255)

if __name__ == '__main__':
    unittest.main()
