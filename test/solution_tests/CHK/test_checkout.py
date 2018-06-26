import unittest

from solutions.CHK import checkout_solution


class TestHello(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout_solution.checkout("AABBBBCDDD"), 255)

    def test_checkout_a_deal(self):
        self.assertEqual(checkout_solution.checkout("AAA"), 130)

    def test_checkout_b_deal(self):
        self.assertEqual(checkout_solution.checkout("BB"), 45)

    def test_checkout_no_deal(self):
        self.assertEqual(checkout_solution.checkout("CCDDC"), 90)

if __name__ == '__main__':
    unittest.main()
