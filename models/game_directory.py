import os
from models.game_file import GameFile, GameFileType


class GameDirectory:

    def __init__(self, files_path, file_type=GameFileType.UNKNOWN):
        if not os.path.exists(files_path) or files_path == '':
            print(f'Invalid path: {files_path}')
            pass

        self.dir_path = files_path

        files = []
        sub_directories = []

        # Get current path all files
        for file in os.listdir(files_path):
            if os.path.isfile(os.path.join(files_path, file)):
                files.append(GameFile(files_path, file, file_type))
            # Get the subdirectories of current path
            if os.path.isdir(os.path.join(files_path, file)):
                sub_directories.append(GameDirectory(os.path.join(files_path, file), file_type))

        if len(files) > 0:
            files.sort(key=lambda x: x.get_filename())

        if len(sub_directories) > 0:
            sub_directories.sort(key=lambda x: x.dir_path)

        self.files = files
        self.sub_directories = sub_directories


    def get_path(self):
        return self.dir_path


    def get_relative_path(self, root_path):
        return os.path.relpath(self.dir_path, root_path)


    def get_folder_name(self):
        return os.path.basename(self.dir_path)


    def debug_print(self, level=0, root_path=None):
        current_relative_path = str(self.get_relative_path(root_path))
        print(f'{'│' * (level - 1) + ' ' * (level - 1) + ('├ ' if level != 0 else '')}{current_relative_path}/ ({self.dir_path})')
        for index, sub_directory in enumerate(self.sub_directories):
            sub_directory.debug_print(level + 1, os.path.join(root_path, current_relative_path))
        for index, file in enumerate(self.files):
            print(f'{('│ ' if level != 0 else '') + '│' * (level - 1) + ' ' * (level - 1) + '├'} {file.get_file_fullname()} ({file.get_file_type()})') if file else None
