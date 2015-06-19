import unittest

from solutions import euler067


class ProjectEuler067Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler067.get_max_path_sum(), 7273)


if __name__ == "__main__":
  unittest.main()
