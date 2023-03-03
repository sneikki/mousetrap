import re

from util import safe_head

flag_declarations = [
    {"name": "help", "match": "h(elp)?"},
    {"name": "version", "match": "v(ersion)?"},
    {"name": "verbose", "match": "verbose"},
    {"name": "name", "match": "name", "arity": 1},
]


class Flag:
    def __init__(self, name, args):
        self.name = name
        self.args = args


def find_flag_declaration(query):
    return safe_head(
        filter(
            lambda flag: re.fullmatch(flag["match"], query),
            flag_declarations
        )
    )
