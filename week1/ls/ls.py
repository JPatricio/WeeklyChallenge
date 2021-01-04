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
    # 1. Implement a simple ls, no arguments (other than directory) [DONE]
    # 2. Implement argument parsing. Add --help [DONE]
    # 3. Implement 55 options (bloody hell) [3/37]
    # 4. Custom options (directory size?)
    # 5. Set up files for packaging
    # 6. Stretch goal

    dc = DirectoryContents(args)
    dc.print_contents()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extended ls command')
    parser.add_argument('path', nargs='?', type=str, default=os.getcwd(),
                        help='The directory for which contents should be shown')
    all_group = parser.add_mutually_exclusive_group(required=False)
    all_group.add_argument('-a', '--all', dest='all', action='store_const',
                        const=True, default=False,
                        help='do not ignore entries starting with .')
    all_group.add_argument('-A', '--almost-all', dest='almost_all', action='store_const',
                        const=True, default=False,
                        help='do not list implied . and ..')
    all_group.add_argument('-l', dest='detailed', action='store_const',
                        const=True, default=False,
                        help='do not list implied . and ..')
    args = parser.parse_args()
    main(args)

# TODO: Fix the final % being printed (wtf)
# TODO: Fix the coloring for links
# TODO: Remove hardcoded column sizes on -l option
