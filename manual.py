from datetime import datetime
import sys
import collections

USAGE = f"""
Usage: python {sys.argv[0]} [command args]
    -i      Show `Hello ...!`
    -d      Show the current datetime
"""


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print(USAGE)
        exit(0)

    argument_from_queue = collections.deque(args)
    while argument_from_queue:
        argument = argument_from_queue.popleft()
        if argument in ["-h", "--help"]:
            print(USAGE)
            sys.exit(0)
        elif argument == "-i":
            name = argument_from_queue.popleft()
            print(f"Hello {name}!")
        elif argument == "-d":
            print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))


if __name__ == "__main__":
    main()
