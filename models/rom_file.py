from os import path


class RomFile:
    def __init__(self, filepath, full_filename, level=0):
        self.path = filepath
        self.name = full_filename
        self.level = level

    def __str__(self):
        return path.join(self.path, self.name)

    def get_path(self):
        return path.join(self.path, self.name)

    def get_dir(self):
        return self.path

    def get_file_fullname(self):
        return self.name

    def get_filename(self):
        return path.splitext(self.name)[0]

    def get_file_extension(self):
        # if file does not have extension
        if len(path.splitext(self.name)[1]) == 0:
            return ''
        return path.splitext(self.name)[1]

    def get_dir_level(self):
        return self.level
