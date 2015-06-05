import unittest

from solutions import euler6


class ProjectEuler6Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler6.get_sum_square_difference(10), 2640)

  def test_Answer(self):
    self.assertEquals(euler6.get_sum_square_difference(100), 25164150)


if __name__ == "__main__":
  unittest.main()
