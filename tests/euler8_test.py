import unittest

from solutions import euler8


class ProjectEuler8Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler8.get_largest_product(4), 5832)

  def test_Answer(self):
    self.assertEquals(euler8.get_largest_product(13), 23514624000)


if __name__ == "__main__":
  unittest.main()
