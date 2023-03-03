import re

from util import safe_head

flag_declarations = [
    {
        "name": "help",
        "match": "h(elp)?",
        "description": "show this guide"
    },
    {
        "name": "version",
        "match": "v(ersion)?",
        "description": "show the version that this program is running"
    },
    {
        "name": "verbose",
        "match": "verbose",
        "description": "more output is generated"
    }
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
