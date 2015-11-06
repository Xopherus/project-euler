"""
Sum Square Difference
https://projecteuler.net/problem=6
"""
import math


def main():
    max_val = 100

    sum_of_squares = sum([
        i ** 2 for i in range(max_val+1)
    ])

    square_of_sum = sum([i for i in range(max_val+1)]) ** 2

    print math.fabs(sum_of_squares - square_of_sum)

main()