import unittest

from solutions import euler4_fast
from solutions import euler4_simple


class ProjectEuler4Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler4_fast.get_max_palindromic_product(10, 99), 9009)
    self.assertEquals(euler4_simple.get_max_palindromic_product(10, 99), 9009)

  def test_Answer(self):
    self.assertEquals(euler4_fast.get_max_palindromic_product(100, 999), 906609)
    self.assertEquals(euler4_simple.get_max_palindromic_product(100, 999), 906609)


if __name__ == "__main__":
  unittest.main()
