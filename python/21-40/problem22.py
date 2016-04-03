"""
Names scores
https://projecteuler.net/problem=22
"""


def alphabetical_value(letter):
    return ord(letter) - ord('A') + 1


def name_score(name, index):
    return sum([alphabetical_value(letter) for letter in name]) * index


def main():
    with open('problem22_names.txt', 'r') as input_file:
        names = sorted(input_file.read().strip().replace('"', '').split(','))
        name_scores = sum([name_score(name=names[i], index=i+1) for i in range(len(names))])

        print 'Total of all name scores in the file: {}'.format(name_scores)


main()
