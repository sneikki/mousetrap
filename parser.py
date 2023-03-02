import itertools
from flag import find_flag
from exception import ArityException, UnknownFlagException


def parse(tokens):
    try:
        head = next(tokens)
    except StopIteration:
        return

    if head.type == "flag":
        parse_flag(head, tokens)

    parse(tokens)


def parse_flag(current, rest):
    flag = find_flag(current.value)
    if not flag:
        raise UnknownFlagException(
            f"""No flag called "{current.literal}" exists.""")

    arity = flag["arity"]
    args = itertools.islice(rest, arity)

    parse_flag_args(current, arity, args)


def parse_flag_args(flag, arity, args):
    args_processed = 0

    for arg in args:
        if arg.type == "flag":
            raise ArityException(
                f"""Flag "{flag.literal}" is missing "{arity}" {
                "arguments" if arity > 1 else "argument"}.""")

        args_processed += 1

    if args_processed < arity:
        raise ArityException(
            f"""Unexpected end of input, flag "{flag.literal}" is missing {arity} {
            "arguments" if arity > 1 else "argument"}.""")
