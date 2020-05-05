import unittest
from math import pi
import circle
class CirclesTestCase(unittest.TestCase):

  def test_check_for_negatives(self):
      # it should not accept the negatives as a radius
      # radius negatives should raise error
      c1 = circle.Circle(-1)
      myError = ValueError('a should be a positive')
      self.assertRaises(myError)
      self.assertEqual(c1.area, (pi))


  def test_check_for_positives(self):
      c1 = circle.Circle(1)
      self.assertEqual(c1.area, pi)


# if __name__ == '__main__':
#     unittest.main()


'''

   Testing the unit test for the circle_test.py would be 
   python -m unittest circle_test.py

import unittest

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
'''