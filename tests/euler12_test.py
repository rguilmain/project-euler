import unittest

from solutions import euler12


class ProjectEuler12Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(
      euler12.get_first_triangle_num_with_over_n_divisors(5), 28)

  def test_Answer(self):
    self.assertEquals(
      euler12.get_first_triangle_num_with_over_n_divisors(500), 76576500)


if __name__ == "__main__":
  unittest.main()
