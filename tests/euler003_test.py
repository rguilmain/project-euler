import unittest

from solutions import euler003


class ProjectEuler003Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler003.get_largest_prime_factor(13195), 29)

  def test_Answer(self):
    self.assertEquals(euler003.get_largest_prime_factor(600851475143), 6857)


if __name__ == "__main__":
  unittest.main()
