"""
10001st prime
https://projecteuler.net/problem=7
"""
import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def main():
    primes = []

    i = 2
    while i > 0:
        if is_prime(i):
            primes.append(i)

        if len(primes) == 10001:
            print primes
            print primes[-1]
            return

        i += 1


main()