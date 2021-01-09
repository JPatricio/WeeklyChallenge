import os
import stat
from argparse import Namespace
from datetime import datetime

from grp import getgrgid
from pwd import getpwuid
from jls.utils.ansi_color_sequences import BColors


class DiskObject(object):
    IS_FILE = 1
    IS_DIR = 2
    IS_LINK = 3

    def __init__(self, full_path: str):
        self.full_path = full_path
        # Everything after the last / is the file name
        self.name = full_path.split('/')[-1]
        self.file_type = self.IS_LINK if os.path.islink(full_path) else \
            self.IS_DIR if os.path.isdir(full_path) else self.IS_FILE

    def __str__(self, length: int = None, args: Namespace = None) -> str:
        if args.clarify:
            self.name += '/' if self.file_type == self.IS_DIR else ''
            self.name += '@' if self.file_type == self.IS_LINK else ''
            self.name += '*' if self.file_type == self.IS_FILE and os.access(self.full_path, os.X_OK) else ''

        if args.detailed:
            details = os.stat(self.full_path)
            mod_timestamp = datetime.fromtimestamp(details.st_mtime)
            return f"{stat.filemode(details.st_mode)} " \
                   f"{str(details.st_nlink).rjust(2, ' ')} " \
                   f"{getpwuid(details.st_uid).pw_name} " \
                   f"{getgrgid(details.st_gid)[0]} " \
                   f"{str(details.st_size).rjust(4, ' ')} " \
                   f"{mod_timestamp.strftime('%b')} " \
                   f"{mod_timestamp.strftime('%d')} " \
                   f"{mod_timestamp.strftime('%H:%M')} " \
                   f"{BColors.OKCYAN if self.file_type == self.IS_DIR else ''}" \
                   f"{BColors.MAGENTA if self.file_type == self.IS_LINK else ''}" \
                   f"{BColors.BOLD if self.file_type == self.IS_DIR or self.IS_LINK else ''}" \
                   f"{self.name}" \
                   f"{BColors.ENDC if self.file_type == self.IS_DIR or self.IS_LINK else ''}" \
                   f"{' -> ' + os.readlink(self.full_path) if self.file_type == self.IS_LINK else ''}"

        if not length:
            length = len(self.name)+1

        # Directories should show blue, links magenta
        return f"{BColors.OKCYAN if self.file_type == self.IS_DIR else ''}" \
               f"{BColors.MAGENTA if self.file_type == self.IS_LINK else ''}" \
               f"{BColors.BOLD if self.file_type == self.IS_DIR or self.IS_LINK else ''}" \
               f"{self.name.ljust(length, ' ')}" \
               f"{BColors.ENDC if self.file_type == self.IS_DIR or self.IS_LINK else ''}"\
