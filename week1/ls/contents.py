import glob
import itertools
import math
import os
import sys
from argparse import ArgumentParser

from disk_object import DiskObject


class DirectoryContents(object):

    def __init__(self, args: ArgumentParser):
        """
        Will gather and store contents of a certain directory
        :param path: Path must be absolute
        """
        self.islink = os.path.islink(args.path)
        self.isdir = os.path.isdir(args.path) and not args.dir_as_files
        self.follow_link = self.islink and self.isdir and not args.detailed and not args.clarify
        self.path = os.readlink(args.path) if self.follow_link else args.path
        self.args = args
        self.contents = list()
        self.max_width_filename = 0
        objects_in_path = list()
        if self.isdir and (not self.islink or self.islink and self.follow_link):
            objects_in_path = glob.iglob(f'{self.path}/*', recursive=False)
            # if -a specified, need to include hidden objects.
            # Glob does not support one look up so separate look up needed
            if args.all:
                # lol.. cheat
                objects_in_path = itertools.chain(
                    ['.', '..'], objects_in_path, glob.iglob(f'{self.path}/.*', recursive=False)
                )

            if args.almost_all:
                objects_in_path = itertools.chain(objects_in_path, glob.iglob(f'{self.path}/.*', recursive=False))
        else:
            objects_in_path = [os.path.abspath(self.path)]

        for object_full_path in objects_in_path:
            # Add to contents
            object = DiskObject(object_full_path)
            self.contents.append(object)
            # Track max width
            self.max_width_filename = max(self.max_width_filename, len(object.name))

        # Add 1 for space after name
        self.max_width_filename += 1

    def print_contents(self):
        """

        :return:
        """
        # We'll print the files in table like fashion, using the full width of the terminal (number of characters)
        terminal_width = os.get_terminal_size().columns

        # How many objects can be print per row
        obj_per_row = math.floor(terminal_width / self.max_width_filename)

        if not self.args.detailed:
            # By default, sort contents by name property
            # TODO: ls prints order vertically, we print horizontally. Crap. Check out how to fix it later.
            printed_obj = 0
            for file in sorted(self.contents, key=lambda disk_object: disk_object.name):
                print(
                    file.__str__(length=self.max_width_filename, args=self.args),
                    end="\n" if printed_obj >= obj_per_row or self.args.one else ""
                )
                printed_obj = printed_obj + 1 if printed_obj >= obj_per_row else 0
        else:
            # This will be a detailed view.
            for file in sorted(self.contents, key=lambda disk_object: disk_object.name):
                print(file.__str__(length=None, args=self.args))

        # This fixes some weird left out buffer on print
        print("", end="")
