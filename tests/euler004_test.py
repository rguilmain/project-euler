import unittest

from solutions import euler004_fast
from solutions import euler004_simple


class ProjectEuler004Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(
      euler004_fast.get_max_palindromic_product(lower_bound=10, upper_bound=99), 9009)
    self.assertEquals(
      euler004_simple.get_max_palindromic_product(lower_bound=10, upper_bound=99), 9009)

  def test_Answer(self):
    self.assertEquals(
      euler004_fast.get_max_palindromic_product(lower_bound=100, upper_bound=999), 906609)
    self.assertEquals(
      euler004_simple.get_max_palindromic_product(lower_bound=100, upper_bound=999), 906609)


if __name__ == "__main__":
  unittest.main()
