import unittest 
from simple_calculator import SimpleCalculator

class testSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 5),10)

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        self.assertEqual(self.calc.divide(10, 5), 2)

if __name__ == "__main__":
    unittest.main()  