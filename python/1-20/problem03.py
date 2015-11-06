"""
Largest Prime Factor
https://projecteuler.net/problem=3
"""
import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_primes(number):
    return [
        i for i in range(2, int(math.sqrt(number))) if is_prime(i)
    ]


def main():
    number = 600851475143
    prime_factors = [
        prime for prime in get_primes(number) if number % prime == 0
    ]

    print prime_factors
    print prime_factors[-1]


main()