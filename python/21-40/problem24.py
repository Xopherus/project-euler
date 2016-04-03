"""
Lexicographic permutations
https://projecteuler.net/problem=24
"""
import itertools


def main():
    # python is awesome...itertools already returns permutations in lexicographic order
    permutations = [p for p in itertools.permutations('0123456789')]

    # find the millionth permutation (remember python starts at 0-index]
    print ''.join(permutations[999999])

main()
