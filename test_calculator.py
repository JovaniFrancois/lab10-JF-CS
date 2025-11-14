#https://github.com/JovaniFrancois/lab10-JF-CS
#Cecil Took Role 2
#Jovani Took Role 1
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(5, 3), 8)
        self.assertEqual(calculator.add(1, 9), 10)


    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(5, 4), 1)
        self.assertEqual(calculator.subtract(10, 6), 4)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertAlmostEqual(calculator.div(7, 3), 7 / 3)
        self.assertEqual(calculator.div(-8, 4), -2)
    ###########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, calculator.div, 5, 0)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.logarithm(2, 2), 1)
        self.assertEqual(calculator.logarithm(100, 10), 2)
        self.assertAlmostEqual(calculator.logarithm(8, 2), 3)
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, calculator.logarithm, 10, 0)


    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertEqual(calculator.hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()