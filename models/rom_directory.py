import os
from models.rom_file import RomFile


class RomDirectory:

    def __init__(self, roms_path):
        if not os.path.exists(roms_path) or roms_path == '':
            print(f'Invalid path: {roms_path}')
            pass

        self.dir_path = roms_path

        rom_files = []
        sub_rom_directories = []

        # Get current path all files
        for file in os.listdir(roms_path):
            if os.path.isfile(os.path.join(roms_path, file)):
                rom_files.append(RomFile(roms_path, file))
            # Get the subdirectories of current path
            if os.path.isdir(os.path.join(roms_path, file)):
                sub_rom_directories.append(RomDirectory(os.path.join(roms_path, file)))

        if len(rom_files) > 0:
            rom_files.sort(key=lambda x: x.get_filename())

        if len(sub_rom_directories) > 0:
            sub_rom_directories.sort(key=lambda x: x.dir_path)

        self.rom_files = rom_files
        self.sub_rom_directories = sub_rom_directories

    def get_relative_path(self, root_path):
        return os.path.relpath(self.dir_path, root_path)

    def debug_print(self, level=0, root_path=None):
        current_relative_path = str(self.get_relative_path(root_path))
        print(f'{'│' * (level - 1) + ' ' * (level - 1) + ('├ ' if level != 0 else '')}{self.get_relative_path(root_path)}/')
        for index, sub_rom_directory in enumerate(self.sub_rom_directories):
            sub_rom_directory.debug_print(level + 1, os.path.join(root_path, current_relative_path))
        for index, rom_file in enumerate(self.rom_files):
            print(f'{('│ ' if level != 0 else '') + '│' * (level - 1) + ' ' * (level - 1) + '├'} {rom_file.get_file_fullname()}') if rom_file else None
