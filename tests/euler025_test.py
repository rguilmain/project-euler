import unittest

from solutions import euler025


class ProjectEuler025Tests(unittest.TestCase):

  def test_Given(self):
    self.assertEquals(euler025.get_first_fib(3), 12)

  def test_Answer(self):
    self.assertEquals(euler025.get_first_fib(1000), 4782)


if __name__ == "__main__":
  unittest.main()
