import unittest

from solutions import euler024


class ProjectEuler024Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler024.get_nth_permutation(range(3), n=1), "012")
    self.assertEquals(euler024.get_nth_permutation(range(3), n=3), "102")
    self.assertEquals(euler024.get_nth_permutation(range(3), n=6), "210")

  def test_Answer(self):
    self.assertEquals(
      euler024.get_nth_permutation(range(10), n=1000000), "2783915460")


if __name__ == "__main__":
  unittest.main()
