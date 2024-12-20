import unittest
from simple_calculator import SimpleCalculator 

class test(unittest.TestCase):
    def setUp(self):
        
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), 0)
        self.assertEqual(self.calc.multiply(-1, 1), 0)
        self.assertEqual(self.calc.divide(-1, 1), 0)
        
    