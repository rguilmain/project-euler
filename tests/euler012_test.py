import unittest

from solutions import euler012


class ProjectEuler012Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(
      euler012.get_first_triangle_num_with_over_n_divisors(n=5), 28)

  def test_Answer(self):
    self.assertEquals(
      euler012.get_first_triangle_num_with_over_n_divisors(n=500), 76576500)


if __name__ == "__main__":
  unittest.main()
