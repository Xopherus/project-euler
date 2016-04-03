"""
Maximum path sum I
https://projecteuler.net/problem=18
"""

TEXT = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def parse_triangle(text):
    """
    Assumes that a block of text represents an equilateral triangle. Converts this into a list of numbers.
    :param text:
    """
    numbers = [
        num for num in ' '.join(text.split('\n')).split(' ')
        if num != ''
    ]

    return numbers


def get_possible_children(triangle, depth, current_location):
    """
    Returns true if the specified cell has a child cell below that lies adjacent to it.
    :param triangle:
    :param depth:
    :param current_location:
    :return:
    """
    try:
        # assuming you have a list of numbers arranged in an equilateral triangle, like so:
        #
        #                    0
        #                   1 2
        #                  3 4 5
        #                 6 7 8 9
        #                   ...
        #
        # you can calculate the children of any node by using the following algorithm:
        #
        # children(n) = {
        #       sum(L) + (n % sum(L)) + (L+1),
        #       sum(L) + (n % sum(L)) + (L+1)
        #   }
        #   Where L is how many levels deep from the top n is.

        if current_location == 0:
            children = (1, 2)
        else:
            far_left_index = sum(i for i in range(depth+1))

            children = (
                far_left_index + (current_location % far_left_index) + (depth+1),
                far_left_index + (current_location % far_left_index) + (depth+2)
            )

        return (
            (children[0], int(triangle[children[0]])),
            (children[1], int(triangle[children[1]]))
        )

    except IndexError:
        return None


def best_path_greedy():
    triangle = parse_triangle(TEXT)

    index = 0
    depth = 0

    best_path = {
        'path': [int(triangle[index])],
        'sum': int(triangle[index])
    }

    children = get_possible_children(triangle, depth=depth, current_location=index)

    while children is not None:
        # uses greedy algorithm for determining best path to take
        max_step = max(children, key=lambda x: int(x[1]))

        best_path['path'].append(max_step[1])
        best_path['sum'] += max_step[1]

        # update current location
        index = max_step[0]
        depth += 1

        # find current location's children
        children = get_possible_children(triangle, depth=depth, current_location=index)

    print best_path


def best_path_part_2():
    def generate_best_moves(potential_cells):
        for i in potential_cells:
            # can move up one, to the left
            if i > 0:
                yield triangle[index-1][i-1]

            # can move up one to the right
            if i < len(triangle[index]):
                yield triangle[index-1][i]

    triangle = [
        [
            int(num) for num in line.strip().split(' ')
        ]
        for line in TEXT.split('\n') if line != ''
    ]

    best_path = {
        'path': [],
        'sum': 0
    }

    index = len(triangle) - 1
    possible_moves = triangle[index]

    while index > 0:
        max_val = max(possible_moves)

        # update best path
        best_path['sum'] += max_val
        best_path['path'].append(max_val)

        # find potential moves
        max_val = max(possible_moves)
        potential_cells = [i for i, j in enumerate(possible_moves) if j == max_val]
        possible_moves = list(generate_best_moves(potential_cells))

        print best_path
        print possible_moves

        index -= 1

    print best_path

def main():
    best_path_greedy()
    best_path_part_2()



main()
