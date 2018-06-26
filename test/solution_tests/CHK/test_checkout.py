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

    def test_checkout_illegal(self):
        self.assertEqual(checkout_solution.checkout(12345), -1)

    def test_checkout_doesnt_exist(self):
        self.assertEqual(checkout_solution.checkout("ABCDFGHIJKLMNOP"), -1)

    def test_checkout_lowercase(self):
        self.assertEqual(checkout_solution.checkout("aABC"), -1)

    def test_checkout_punctuation(self):
        self.assertEqual(checkout_solution.checkout("AA!BC"), -1)

    def test_checkout_punctuation(self):
        self.assertEqual(checkout_solution.checkout(None), -1)

    def test_checkout_e_b_deal(self):
        self.assertEqual(checkout_solution.checkout("EEB"), 80)

if __name__ == '__main__':
    unittest.main()
