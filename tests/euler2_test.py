import unittest

from solutions import euler2


class ProjectEuler2Tests(unittest.TestCase):

  def test_Answer(self):
    self.assertEquals(euler2.get_sum_of_even_fibonacci(4000000), 4613732)


if __name__ == "__main__":
  unittest.main()
