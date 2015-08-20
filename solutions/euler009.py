import sys


def get_special_pythagorean_triplet(s):
  for a in range(s / 3):
    for b in range(a, (s - a) / 2):
      c = s - a - b
      if a**2 + b**2 == c**2:
        return a * b * c


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  print get_special_pythagorean_triplet(1000)


if __name__ == "__main__":
  sys.exit(main())
