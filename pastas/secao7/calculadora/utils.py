import re

NUMBER_OR_DOT_REGEX = re.compile(r'^[0-9.]^$')


def is_number_or_dot(string: str):
    return bool(NUMBER_OR_DOT_REGEX.search(string))


def convert_to_number(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


def is_valid_number(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def is_empty(string: str):
    return len(string) == 0
