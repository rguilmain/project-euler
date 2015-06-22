import sys


ones = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine"}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
         15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
         19: "nineteen"}
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}


def get_num_letters(number):
  if len(str(number)) == 1:
    return len(ones[number])
  if number in teens:
    return len(teens[number])
  leading_digit = int(str(number)[0])
  if len(str(number)) == 2:
    remainder = number % 10
    return len(tens[leading_digit]) + len(ones[remainder])
  if len(str(number)) == 3:
    hundreds_string = ones[leading_digit] + "hundred"
    remainder = number % 100
    if remainder == 0:
      return len(hundreds_string)
    return len(hundreds_string + "and") + get_num_letters(remainder)
  if len(str(number)) == 4:
    remainder = number % 1000
    return len(ones[leading_digit] + "thousand") + get_num_letters(remainder)
  raise NotImplementedError("Cannot process numbers with five or more digits!")


def get_sum_letter_counts(upper_bound):
  s = 0
  for i in range(1, upper_bound + 1):
    s += get_num_letters(i)
  return s


def main(argv=None):
  if argv is not None:
    sys.argv = argv

  number = 1000
  print get_sum_letter_counts(number)


if __name__ == "__main__":
  sys.exit(main())
