messages = {
    "see-help": ("Run \"mousetrap --help\" to see"
                 " all options and how they are used.")
}


def build_flag_string(flag_declaration, longest, padding, indent):
    total_padding = longest - len(flag_declaration["name"]) + padding
    return "".join([
        " " * indent,
        "--",
        flag_declaration["name"],
        " " * total_padding,
        flag_declaration["description"]
    ])


def get_flag_list(flag_declarations, indent, padding):
    longest = max(map(lambda d: len(d["name"]), flag_declarations))

    return "Flags:\n" + "\n".join(map(lambda flag: build_flag_string(
        flag, longest, indent, padding), flag_declarations))


def get_message(name):
    return messages.get(name)


def safe_head(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None
