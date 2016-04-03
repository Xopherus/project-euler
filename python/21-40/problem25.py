"""
1000-digit Fibonacci number
https://projecteuler.net/problem=25
"""


def main():
    fn_2 = 1
    fn_1 = 1

    # loop starts at F(3)
    n = 3

    while True:
        fn = fn_2 + fn_1

        if len(str(fn)) == 1000:
            print 'First Fibonacci number with 1000 digits is F({})'.format(n)
            exit(0)

        # update last 2 states: F(n-2), F(n-1)
        fn_2 = fn_1
        fn_1 = fn

        # increment index
        n += 1

main()
