import math
import unittest

from solutions import euler022


class ProjectEuler022Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler022.get_sum_of_names_scores(), 871198282)


if __name__ == "__main__":
  unittest.main()
