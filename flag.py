import re


FLAGS = [
    {"test": "h(elp)?", "arity": 0},
    {"test": "v(ersion)?", "arity": 0},
    {"test": "verbose", "arity": 0},
    {"test": "name", "arity": 2},
]


def find_flag(query):
    try:
        return next(filter(lambda flag: re.fullmatch(
            flag["test"], query), FLAGS))
    except StopIteration:
        return None
