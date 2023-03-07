import sys
import collections

USAGE = f"""
Usage: python {sys.argv[0]} [command args]
    -i      Display `Hello ...!`
"""


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print(USAGE)
        exit(0)

    arguments = collections.deque(args)
    while arguments:
        arguments = arguments.popleft()
        if arguments in ["-h", "--help"]:
            print(USAGE)
            sys.exit(0)
        elif arguments == "-i":
            name = arguments.popleft()
            print(f"Hello {name}!")


if __name__ == "__main__":
    main()
