import unittest

from solutions import euler016


class ProjectEuler016Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler016.get_sum_of_digits(2**15), 26)

  def test_Answer(self):
    self.assertEquals(euler016.get_sum_of_digits(2**1000), 1366)


if __name__ == "__main__":
  unittest.main()
