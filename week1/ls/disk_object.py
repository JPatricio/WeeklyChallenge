class DiskObject(object):
    def __init__(self, full_path):
        self.full_path = full_path
        # Everything after the last / is the file name
        self.name = full_path.split('/')[-1]

    def __str__(self):
        return self.name


class LsFile(DiskObject):
    pass


class LsDirectory(DiskObject):
    pass