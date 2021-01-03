import glob
import os

from disk_object import LsFile, LsDirectory


class DirectoryContents(object):

    def __init__(self, path: str):
        """
        Will gather and store contents of a certain directory
        :param path: Path must be absolute
        """
        self.contents = list()
        for object_full_path in glob.iglob(f'{path}/*', recursive=False):
            if os.path.isfile(object_full_path):
                self.contents.append(LsFile(object_full_path))
            else:
                self.contents.append(LsDirectory(object_full_path))

    def print_contents(self):
        """

        :return:
        """
        # By default, sort contents by name property
        for file in sorted(self.contents, key=lambda disk_object: disk_object.name.lower()):
            print(file)
