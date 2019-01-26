# -*- coding: utf-8 -*-
import unittest
import unit_test_practice

class UnitTestPracticeMain(unittest.TestCase):
    """This class unit tests the unit_test_practice.py file
    """    
    def test_add(self):
        self.assertEqual(unit_test_practice.add(10, 5), 15)
        self.assertEqual(unit_test_practice.add(-1, 1), 0)
        self.assertEqual(unit_test_practice.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(unit_test_practice.subtract(10, 5), 5)
        self.assertEqual(unit_test_practice.subtract(-1, 1), -2)
        self.assertEqual(unit_test_practice.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(unit_test_practice.multiply(10, 5), 50)
        self.assertEqual(unit_test_practice.multiply(-1, 1), -1)
        self.assertEqual(unit_test_practice.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(unit_test_practice.divide(10, 5), 2)
        self.assertEqual(unit_test_practice.divide(-1, 1), -1)
        self.assertEqual(unit_test_practice.divide(-1, -1), 1)
        self.assertEqual(unit_test_practice.divide(5, 2), float(2.5))
        self.assertEqual(unit_test_practice.divide(1, 0), float("inf"))
    
    def test_divide2(self):
        self.assertRaises(ValueError, unit_test_practice.divide2, 10, 0)
        with self.assertRaises(ValueError):
            unit_test_practice.divide2(10000, 0)

if __name__ == '__main__':
    unittest.main()