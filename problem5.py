"""
Smallest Multiple
https://projecteuler.net/problem=5
"""


def is_evenly_divisible(number):
    for i in range(1, 21):
        if number % i != 0:
            return False

    return True


def main():
    i = 2
    while i > 0:
        if is_evenly_divisible(i):
            print i
            return

        i += 2


main()