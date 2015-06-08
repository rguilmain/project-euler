import unittest

from solutions import euler011


class ProjectEuler011Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler011.get_largest_product_in_grid(4), 70600674)


if __name__ == "__main__":
  unittest.main()
