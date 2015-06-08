import unittest

from solutions import euler014


class ProjectEuler014Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler014.get_term_with_longest_sequence(1000000), 837799)


if __name__ == "__main__":
  unittest.main()
