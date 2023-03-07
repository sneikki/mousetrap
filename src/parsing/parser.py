import itertools

from exception import ArityException, UnknownFlagException
from flag import Flag, find_flag_declaration
from util import safe_head


def parse(tokens, state):
    current_token = safe_head(tokens)

    if not current_token:
        return state
    elif current_token.type == "flag":
        state["flags"].append(parse_flag(current_token, tokens))
    elif current_token.type == "identifier":
        if not state.get("command"):
            state["command"] = current_token.value
        else:
            state["args"].append(current_token.value)

    return parse(tokens, state)


def parse_flag(flag_token, tokens):
    flag_details = find_flag_declaration(flag_token.value)
    if not flag_details:
        raise UnknownFlagException(flag_token.literal)

    flag_arity = flag_details.get("arity", 0)
    flag_args = parse_flag_args(
        flag_token.literal,
        flag_arity,
        itertools.islice(tokens, flag_arity)
    )

    return Flag(flag_token.value, flag_args)


def parse_flag_args(flag_literal, flag_arity, arg_tokens):
    valid_args = []

    for arg_token in arg_tokens:
        if arg_token.type == "flag":
            break
        valid_args.append(arg_token)

    if len(valid_args) < flag_arity:
        raise ArityException(flag_literal, flag_arity, len(valid_args))

    return valid_args
