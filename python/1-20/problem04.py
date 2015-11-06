"""
Largest Palindrome Project
https://projecteuler.net/problem=4
"""


def is_palindrome(number):
    number = str(number)

    if len(number) % 2 == 0:
        return number[0:len(number) / 2] == number[:(len(number) / 2 - 1):-1]
    else:
        return number[0:len(number) / 2] == number[:(len(number) / 2):-1]


def main():
    palindromes = [
        i * j
        for i in range(100, 999) for j in range(100, 999)
        if is_palindrome(i * j)
    ]

    print sorted(palindromes)[-1]


main()