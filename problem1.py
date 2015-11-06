"""
Multiples of 3 and 5
https://projecteuler.net/problem=1
"""


def arithmetic_series(max_value, step):
    return sum([i for i in xrange(0, max_value, step)])


def main():
    max_value = 1000

    print (
        arithmetic_series(max_value, 3) + arithmetic_series(max_value, 5) -
        arithmetic_series(max_value, 3*5)
    )

main()