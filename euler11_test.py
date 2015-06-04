import unittest

import euler11


class ProjectEuler11Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler11.get_largest_product_in_grid(4), 70600674)


if __name__ == "__main__":
  unittest.main()
