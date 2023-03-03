import re
from token import Token


def is_flag_token(arg):
    return bool(re.fullmatch("-\\w|--(\\w{2,}-?)+", arg))


def get_token_type(arg):
    return "flag" if is_flag_token(arg) else "identifier"


def scan_token(arg):
    token_type = get_token_type(arg)
    token_value = (arg.lstrip("-") if token_type == "flag"
                   else arg)

    return Token(token_type, token_value, arg)


def tokenize(args):
    return map(scan_token, args)
