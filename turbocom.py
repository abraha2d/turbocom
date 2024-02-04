#!/usr/bin/env python3

import sys


def main(stream):
    while len(c := stream.read(1)):
        if c != b'~':
            continue
        length = stream.read(1)[0]
        stream.read(2)
        print(stream.read(length).decode())


if __name__ == "__main__":
    main(sys.stdin.buffer)
