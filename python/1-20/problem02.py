"""
Even Fibonacci Numbers
https://projecteuler.net/problem=2
"""


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def main():
    fibonacci_num = 1
    even_sum = 0
    i = 1

    while fibonacci_num < 4000000:
        fibonacci_num = fibonacci(i)

        if fibonacci_num % 2 == 0:
            even_sum += fibonacci_num
        i += 1

    print even_sum

main()