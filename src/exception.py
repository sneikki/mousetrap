from util import get_message


class MousetrapException(Exception):
    def __init__(self, name, message, exit_code):
        self.exit_code = exit_code
        self.message = f"""{name}: {message}\n\n{get_message("see-help")}"""

        super().__init__(self.message)


class ArityException(MousetrapException):
    error_name = "Wrong arity"
    exit_code = 2

    def __init__(self, receiver, expected, received):
        message = " ".join(
            map(str, [
                f'"{receiver}"', "was expecting", expected,
                ("argument" if expected == 1 else "arguments"),
                "but only", received,
                ("was" if received == 1 else "were"),
                "provided"
            ]))

        super().__init__(self.error_name, message, self.exit_code)


class UnknownFlagException(MousetrapException):
    error_name = "Unrecognized flag"
    exit_code = 2

    def __init__(self, received):
        super().__init__(
            self.error_name,
            f'"{received}"',
            self.exit_code
        )
