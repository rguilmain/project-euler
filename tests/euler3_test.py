import unittest

from solutions import euler3


class ProjectEuler3Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler3.get_largest_prime_factor(13195), 29)

  def test_Answer(self):
    self.assertEquals(euler3.get_largest_prime_factor(600851475143), 6857)


if __name__ == "__main__":
  unittest.main()
