import math
import unittest

from solutions import euler020


class ProjectEuler020Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler020.get_sum_of_digits(math.factorial(10)), 27)

  def test_Answer(self):
    self.assertEquals(euler020.get_sum_of_digits(math.factorial(100)), 648)


if __name__ == "__main__":
  unittest.main()
