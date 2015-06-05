# Miscellaneous utility functions.


def range_large(start, stop, step=1):
  """Similar to the built-in Python 2.7 range() function, but is able to
  handle large input values.
  """
  i = start
  while i < stop:
    yield i
    i += step
