import unittest

from solutions import euler5


class ProjectEuler5Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler5.get_smallest_multiple(10), 2520)

  def test_Answer(self):
    self.assertEquals(euler5.get_smallest_multiple(20), 232792560)


if __name__ == "__main__":
  unittest.main()
