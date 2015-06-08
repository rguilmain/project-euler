import unittest

from solutions import euler14


class ProjectEuler14Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler14.get_longest_sequence(1000000), 837799)


if __name__ == "__main__":
  unittest.main()
