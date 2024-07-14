import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()
        def test_addition(self):
            self.assertEqual(self.calc.add(2, 3), 8)
            def test_subtraction(self):
                self.assertEqual(self.calc.subtract, test_subtraction(self))
                def test_multiply(self):
                    result = self.calculator.multiply(2, 6)
                    self.assertEqual(result, 12)
                    def test_divide(self):
                        result = self.calculator.divide(10, 2)
                        self.assertEqual(result, 5)
                        def test_divide_by_zero(self)
                        with self.assertRaises(ValueError):
                            self.calculator.divide(10, 0)
                            def test_divide_float(self):
                                result = self.calculator.divide(5,2)
                                self.assertAlmostEqual (result, 2.5)
                            

