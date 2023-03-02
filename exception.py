class MousetrapException(Exception):
    def __init__(self, message, exit_code):
        super().__init__(f"Mousetrap has encountered an error!\n{message}")

        self.exit_code = exit_code


class ArityException(MousetrapException):
    def __init__(self, message, exit_code=2):
        super().__init__(message, exit_code)


class UnknownFlagException(MousetrapException):
    def __init__(self, message, exit_code=2):
        super().__init__(message, exit_code)
