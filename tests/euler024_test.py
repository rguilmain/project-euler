import unittest

from solutions import euler024


class ProjectEuler024Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler024.get_nth_permutation(1, range(3)), "012")
    self.assertEquals(euler024.get_nth_permutation(3, range(3)), "102")
    self.assertEquals(euler024.get_nth_permutation(6, range(3)), "210")

  def test_Answer(self):
    self.assertEquals(
      euler024.get_nth_permutation(1000000, range(10)), "2783915460")


if __name__ == "__main__":
  unittest.main()
