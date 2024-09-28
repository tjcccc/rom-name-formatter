from os import path
from enum import Enum


class GameFileType(Enum):
    UNKNOWN = 'Unknown'
    ROM = 'Rom'
    SAVE = 'Save'
    STATE = 'SaveState'


class GameFile:
    def __init__(self, filepath, full_filename, file_type: GameFileType = GameFileType.UNKNOWN):
        self.path = filepath
        self.folder = path.basename(filepath)
        self.name = full_filename
        self.file_type = file_type

    def __str__(self):
        return path.join(self.path, self.name)

    def get_path(self):
        return path.join(self.path, self.name)

    def get_full_dir(self):
        return self.path

    def get_relative_path(self, root_path):
        return path.relpath(self.path, root_path)

    def get_file_fullname(self):
        return self.name

    def get_filename(self):
        return path.splitext(self.name)[0]

    def get_file_extension(self):
        if len(path.splitext(self.name)[1]) == 0:
            return ''
        rest_of_filename = path.splitext(self.name)[1]
        if rest_of_filename[0] == '.':
            return rest_of_filename[1:]
        return rest_of_filename

    def get_file_type(self):
        return str(self.file_type.value)
