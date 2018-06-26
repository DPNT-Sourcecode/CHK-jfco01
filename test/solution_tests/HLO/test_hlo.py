import unittest

from solutions.HLO import hello_solution


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello("Jim"), "Hello, World!")

    # def test_sum_string_params(self):
    # 	with self.assertRaises(TypeError):
    #         sum_solution.compute("A", '@')

    # def test_sum_below_zero(self):
    # 	with self.assertRaises(ValueError):
    #         sum_solution.compute(-1, -2)

    # def test_sum_above_hundred(self):
    # 	with self.assertRaises(ValueError):
    #         sum_solution.compute(101, 200)


if __name__ == '__main__':
    unittest.main()
