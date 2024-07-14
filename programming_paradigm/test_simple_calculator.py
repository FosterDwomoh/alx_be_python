import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()
        def test_addition(self):
            self.assertEqual(self.calc.add(2, 3), 8)
            def test_subtraction(self):
                self.assertEqual(self.calc.subtract, test_subtraction(self))
                def test_multiplication(self):
                    self.assertEqual(self.calc.multiply)
                    def test_division(self):
                        self.assertEqual(self.calc.divide)
                        def test_divide_by_zero(self)
                        with self.assertRaises(ValueError):
                            self.calculator.divide(10, 0)
                            def test_divide_float(self):
                                result = self.calculator.divide(5,2)
                                self.assertAlmostEqual (result, 2.5)
                            

