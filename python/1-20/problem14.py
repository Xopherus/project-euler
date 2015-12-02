"""
Longest Collatz Sequence
https://projecteuler.net/problem=14
"""


def generate_next_collatz_number(n):
    """
    Generates the next number in a Collatz sequence.
        n -> n/2    (n is even)
        n -> 3n + 1 (n is odd)
    :param n:
    :return:
    """
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1


def generate_collatz_sequence(n):
    """
    Generates a Collatz sequence for any positive integer n.
    :param n:
    :return:
    """
    sequence = []

    if n < 1:
        return sequence

    while True:
        sequence.append(n)
        n = generate_next_collatz_number(n)

        if sequence[-1] == 1:
            return sequence


def main():
    longest_chain = {'number': 1, 'chain_length': 1}

    for n in xrange(1, 1000000):
        sequence = generate_collatz_sequence(n)
        # print 'Generated sequence for %d' % n

        if len(sequence) > longest_chain['chain_length']:
            longest_chain = {
                'number': n,
                'chain_length': len(sequence)
            }

    print longest_chain


main()
