import unittest

from solutions import euler005


class ProjectEuler005Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler005.get_smallest_multiple(10), 2520)

  def test_Answer(self):
    self.assertEquals(euler005.get_smallest_multiple(20), 232792560)


if __name__ == "__main__":
  unittest.main()
