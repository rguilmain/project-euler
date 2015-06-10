import unittest

from solutions import euler015


class ProjectEuler015Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler015.get_num_routes(2, 2), 6)

  def test_Answer(self):
    self.assertEquals(euler015.get_num_routes(20, 20), 137846528820)


if __name__ == "__main__":
  unittest.main()
