"""
Factorial digit sum
https://projecteuler.net/problem=20
"""
import math


def main():
    n = 100
    digits = [int(digit) for digit in str(math.factorial(n))]

    print 'Sum of digits in {}! is: {}'.format(n, sum(digits))

main()
