import unittest

from solutions import euler018


class ProjectEuler018Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler018.get_max_path_sum(), 1074)


if __name__ == "__main__":
  unittest.main()
