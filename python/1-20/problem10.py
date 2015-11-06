"""
Summation of primes
https://projecteuler.net/problem=10
"""
import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def main():
    max_limit = 2000000
    primes = [n for n in range(2, max_limit+1) if is_prime(n)]
    print sum(primes)

main()