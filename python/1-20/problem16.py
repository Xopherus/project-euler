"""
Power digit sum
https://projecteuler.net/problem=16
"""


def digit_sum(n):
    """
    Calculates the sum of all digits in a number n.
    :param n:
    :return:
    """
    return sum([int(digit) for digit in str(n)])


def main():
    print digit_sum(pow(2, 1000))

main()
