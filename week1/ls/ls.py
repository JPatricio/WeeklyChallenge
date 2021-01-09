"""
Recreate the ‘ls’ command from scratch and add some modern twists. Colorize the output to make it easier to read,
show all extended attributes, allow the “long view” attributes to display multiple columns if the terminal is
wide enough. The ‘ls’ command does a LOT, so implement as much of it as you can

Advanced Stretch Goal: Use asyncio to concurrently gather extended attributes of each file and improve performance.
"""
import argparse
import os

from contents import DirectoryContents


def main(args: argparse.Namespace):
    # Let's split this into steps -
    # 1. Implement a simple ls, no arguments (other than directory) [DONE]
    # 2. Implement argument parsing. Add --help [DONE]
    # 3. Implement 55 options (bloody hell) [7/36]
    # 4. Testing
    # 5. Custom options (directory size?)
    # 6. Set up files for packaging
    # 7. Stretch goal

    dc = DirectoryContents(args)
    dc.print_contents()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extended ls command')
    parser.add_argument('path', nargs='?', type=str, default=os.getcwd(),
                        help='The directory for which contents should be shown')
    parser.add_argument('-1', '--one', dest='one', action='store_const',
                        const=True, default=False,
                        help='(The numeric digit "one")  Force output to be one entry per line.\n'
                             'This is the default when output is not to a terminal.')
    all_group = parser.add_mutually_exclusive_group(required=False)
    all_group.add_argument('-a', '--all', dest='all', action='store_const',
                           const=True, default=False,
                           help='do not ignore entries starting with .')
    all_group.add_argument('-A', '--almost-all', dest='almost_all', action='store_const',
                           const=True, default=False,
                           help='do not list implied . and ..')
    parser.add_argument('-d', '--dir-as-files', dest='dir_as_files', action='store_const',
                        const=True, default=False,
                        help='Directories are listed as plain files (not searched recursively).')
    parser.add_argument('-f', '--no-sort', dest='no_sort', action='store_const',
                        const=True, default=False,
                        help='Directories are listed as plain files (not searched recursively).')
    parser.add_argument('-F', '--clarify', dest='clarify', action='store_const',
                        const=True, default=False,
                        help='Display a slash / immediately after each pathname that is a directory'
                             'an asterisk * after each that is executable, an at sign @ after each symbolic link,'
                             'an equals sign = after each socket, a percent sign % after each whiteout, and a'
                             'vertical bar | after each that is a FIFO.')
    parser.add_argument('-H', '--follow-links', dest='follow_links', action='store_const',
                        const=True, default=False,
                        help='Symbolic links on the command line are followed.'
                             'This option is assumed if none of the -F, -d, or -l options are specified')
    parser.add_argument('-l', dest='detailed', action='store_const',
                        const=True, default=False,
                        help='do not list implied . and ..')
    args = parser.parse_args()
    main(args)

# TODO: Remove hardcoded column sizes on -l option
# TODO: Add missing flags on -F option
