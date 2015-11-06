"""
Special Pythagorean Triplet
https://projecteuler.net/problem=9
"""
import math


def is_pythagorean_triplet(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)


def main():
    # choose arbitrary max limits for a,b.
    # this is a brute force method to try all combinations of a < b until you hit the
    # one where a + b + c == 1000
    for a in range(1, 5000):
        for b in range(a, 5000):
            # write c in terms of a and b so we can optimize 2 variables instead of 3
            c = math.sqrt((a ** 2) + (b ** 2))

            if is_pythagorean_triplet(a, b, c) and a + b + c == 1000:
                print 'a: %d, b: %d, c: %d' % (a, b, c)
                print a * b * c


main()