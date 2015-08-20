import unittest

from solutions import euler017


class ProjectEuler017Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler017.get_sum_letter_counts(upper_bound=5), 19)

  def test_Answer(self):
    self.assertEquals(euler017.get_sum_letter_counts(upper_bound=1000), 21124)


if __name__ == "__main__":
  unittest.main()
