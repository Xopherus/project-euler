"""
Non-abundant sums
https://projecteuler.net/problem=23
"""


def sum_of_divisors(n):
    return sum([i for i in range(1, n/2 + 1) if n % i == 0])


def is_abundant_number(n):
    """
    n is defined as "abundant" if sum of its proper divisors is > n
    """
    return sum_of_divisors(n) > n


def is_deficient_number(n):
    """
    n is defined as "deficient" if sum of its proper divisors is < n
    """
    return sum_of_divisors(n) < n


def is_perfect_number(n):
    """
    n is defined as "perfect" if sum of its proper divisors = n
    """
    return sum_of_divisors(n) > n


def main():
    min_abundant_num = 12
    max_abundant_num = 28123

    # find all abundant numbers between 12 and 28123
    abundant_numbers = [
        n for n in range(min_abundant_num, max_abundant_num + 1) if is_abundant_number(n)
    ]

    # find all numbers which can be written in terms of those numbers
    numbers_written_in_terms_of_two_abundant_numbers = set([
        a + b for a in abundant_numbers for b in abundant_numbers if a + b < max_abundant_num
    ])

    # take the inverse of that set to find all numbers which cannot be written in terms of two abundant numbers
    numbers_that_cannot_be_written_in_terms_of_two_abundant_numbers = \
        set(range(1, max_abundant_num)).difference(set(numbers_written_in_terms_of_two_abundant_numbers))

    # sum those numbers
    print sum(numbers_that_cannot_be_written_in_terms_of_two_abundant_numbers)


main()
