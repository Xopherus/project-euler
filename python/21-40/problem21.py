"""
Amicable numbers
https://projecteuler.net/problem=21
"""


def sum_of_proper_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])


def main():
    amicable_numbers = set()

    for a in range(1, 10000):
        b = sum_of_proper_divisors(a)
        d_of_b = sum_of_proper_divisors(b)

        if a != b and a == d_of_b:
            amicable_numbers = amicable_numbers.union({a, b})

    print 'Set of amicable numbers is:', list(amicable_numbers)
    print 'Sum of amicable numbers:', sum(amicable_numbers)

main()
