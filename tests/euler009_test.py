import unittest

from solutions import euler009


class ProjectEuler009Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler009.get_special_pythagorean_triplet(1000), 31875000)


if __name__ == "__main__":
  unittest.main()
