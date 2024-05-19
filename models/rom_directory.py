import json
from models.rom_file import RomFile


class RomDirectory:
    def __init__(self, rom_files: [RomFile], dir_level=0):
        self.dir_level = dir_level
        self.rom_files = filter(lambda x: x.get_dir_level() == dir_level, rom_files)
        self.dir_path = rom_files[0].get_full_dir() if (len(rom_files) > 0) else ''

        next_dir_level = dir_level + 1
        max_dir_level = max(map(lambda x: x.get_dir_level(), rom_files))
        if next_dir_level <= max_dir_level:
            self.sub_rom_directory = RomDirectory(rom_files, next_dir_level)
        else:
            self.sub_rom_directory = None

    def to_json(self):
        return json.dumps({
            'dir_level': self.dir_level,
            'dir_path': self.dir_path,
            'rom_files': [rom_file.get_path() for rom_file in self.rom_files],
            'sub_rom_directory': self.sub_rom_directory.to_json() if self.sub_rom_directory else None
        })

    def debug_print(self):
        print(f'dir level: {self.dir_level}')
        print(f'dir path: {self.dir_path}')
        for rom_file in self.rom_files:
            print(rom_file)
        self.sub_rom_directory.debug_print() if self.sub_rom_directory else None
