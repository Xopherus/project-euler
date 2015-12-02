"""
Lattice paths
https://projecteuler.net/problem=15
"""
import math


def n_choose_k(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def main():
    grid_size = 20

    right_steps, down_steps = grid_size, grid_size

    # 40 total moves to get from top corner to bottom (just add up dimensions of the grid)
    # we want to choose
    print n_choose_k(right_steps + down_steps, right_steps)
    print n_choose_k(right_steps + down_steps, down_steps)

main()
