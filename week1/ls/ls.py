"""
Recreate the ‘ls’ command from scratch and add some modern twists. Colorize the output to make it easier to read,
show all extended attributes, allow the “long view” attributes to display multiple columns if the terminal is
wide enough. The ‘ls’ command does a LOT, so implement as much of it as you can

Advanced Stretch Goal: Use asyncio to concurrently gather extended attributes of each file and improve performance.
"""
import argparse
import os

from contents import DirectoryContents


def main(args):
    # Let's split this into steps -
    # 1. Implement a simple ls, no arguments (other than directory)
    # 2. Implement argument parsing. Add --help
    # 3. Implement 55 options (bloody hell)
    # 4. output formatting
    # 5. Custom options (directory size?)
    # 6. Stretch goal
    dc = DirectoryContents(args.path)
    dc.print_contents()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extended ls command')
    parser.add_argument('path', nargs='?', type=str, default=os.getcwd(),
                        help='The directory for which contents should be shown')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    main(args)