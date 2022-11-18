import unittest 
import calculate
from calculate import *  

class CalculatorTest(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calculate.add(75, 25), 100) 

  def test_subtract(self):
    self.assertEqual(calculate.subtract(60, 30), 30)

  def test_multiply(self):
    self.assertEqual(calculate.multiply(3, 7), 21)

  def test_divide(self):
    self.assertEqual(calculate.divide(10, 4), 2)
    self.assertRaises(ZeroDivisionError)
  
if __name__=='__main__':
  unittest.main()