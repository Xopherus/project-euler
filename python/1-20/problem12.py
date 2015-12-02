"""
Highly divisible triangular number
https://projecteuler.net/problem=12
"""


def get_factors(n):
    """
    Returns a list of all of the factors of a number. (Recursive implementation)

    :param n:
    :return: []
    """
    factors = 1

    count = 0
    while n % 2 == 0:
        count += 1
        n /= 2

    factors *= (count + 1)

    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n /= p

        factors *= (count + 1)
        p += 2

    return factors


def main():
    n = 1
    triangular_number = n

    while True:
        factors = get_factors(triangular_number)
        print triangular_number, factors

        if factors > 500:
            print n, triangular_number, factors
            exit()

        n += 1
        triangular_number += n

main()
