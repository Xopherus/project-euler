"""
Number letter counts
https://projecteuler.net/problem=17
"""

single_digits = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

thousands = [
    'one thousand'
]


def len_digit_string(num_string):
    """
    Counts the number of characters in a number string. Doesn't count spaces or hyphens.
    :param num_string:
    :return:
    """
    return len([char for char in num_string.strip() if char not in [' ', '-']])


def main():
    numbers = {
        '0-9': single_digits,

        '10-19': teens,

        '20-99': [
            '{} {}'.format(ten, digit)
            for ten in tens
            for digit in single_digits
        ],

        '100-999': [
            '{} hundred {}'.format(
                hundreds_digit, 'and {}'.format(ones_digit)
                if ones_digit != '' else '{}'.format(ones_digit)
            )
            for hundreds_digit in single_digits[1:]
            for ones_digit in single_digits

        ] + [
            '{} hundred and {}'.format(hundreds_digit, teen)
            for hundreds_digit in single_digits[1:]
            for teen in teens

        ] + [
            '{} hundred and {} {}'.format(hundreds_digit, ten, ones_digit)
            for hundreds_digit in single_digits[1:]
            for ten in tens
            for ones_digit in single_digits

        ],

        '1000': thousands
    }

    letter_count = {
        key: sum([len_digit_string(number_string) for number_string in values])
        for key, values in numbers.iteritems()
    }

    print letter_count
    print sum([totals for key, totals in letter_count.iteritems()])

main()
