#!/usr/bin/env python3
import sys
from tokenizer import tokenize
from parser import parse
from exception import MousetrapException

if __name__ == "__main__":
    tokens = tokenize(sys.argv[1:])

    try:
        parse(tokens)
    except MousetrapException as error:
        print(error.message, file=sys.stderr)
        exit(error.exit_code)
