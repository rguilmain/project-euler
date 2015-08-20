import unittest

from solutions import euler008


class ProjectEuler008Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler008.get_largest_product(num_adjacent_digits=4), 5832)

  def test_Answer(self):
    self.assertEquals(euler008.get_largest_product(num_adjacent_digits=13), 23514624000)


if __name__ == "__main__":
  unittest.main()
