from os import path


class RomFile:
    def __init__(self, filepath, full_filename, path_level=0):
        self.path = filepath
        self.folder = path.basename(filepath)
        self.name = full_filename
        self.path_level = path_level

    def __str__(self):
        return path.join(self.path, self.name)

    def get_path(self):
        return path.join(self.path, self.name)

    def get_full_dir(self):
        return self.path

    def get_relative_path(self, root_path):
        return path.relpath(self.path, root_path)

    def get_dir(self):
        if self.path_level == 0:
            return ''
        else:
            return self.folder

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
        return self.path_level

