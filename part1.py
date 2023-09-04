#!/usr/bin/env python3

eecs388 = b"\x03\x08\x08"


def str_to_bytes(s: str) -> bytes:
    # convert a string to bytes
    arr = s.encode("ascii")
    return arr


def hex_to_bytes(s: str) -> bytes:
    # convert a hex string to bytes
    arr = bytes.fromhex(s)
    return arr


def int_to_bytes(n: int) -> bytes:
    # convert an int to bytes
    arr = n.to_bytes(4, "big")
    return arr


def set_end_to_zero(b):
    # set the last byte of b to 0 (zero)
    b[-1] = 0


# Feel free to edit the main function however you like to help you debug, it won't be graded
#
# Run this script with the command: python3 part1.py
# or select "Part 1" from the VS Code debugger
def main():
    print(eecs388)

    bytes1 = str_to_bytes("Hello, world!")
    print(bytes1)

    bytes2 = hex_to_bytes("a2f295ac")
    print(bytes2)

    bytes3 = int_to_bytes(100599730)
    print(bytes3)

    b = bytearray(b"\x01\x02\x03\x04\x05")
    set_end_to_zero(b)
    print(b)


if __name__ == "__main__":
    main()
