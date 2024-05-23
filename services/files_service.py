import os
from models.rom_file import RomFile


excluded_system_files = ['desktop.ini', 'Thumbs.db', '.DS_Store', '.localized', '.gitignore']
excluded_image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
excluded_media_extension = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpg', '.mpeg', '.m4v', '.3gp']
excluded_execution_extensions = ['.exe', '.bat', '.sh', '.cmd', '.com', '.msi', '.jar', '.app', '.apk', '.ipa', '.deb', '.rpm', '.dmg', '.pkg']

excluded_files = excluded_system_files
excluded_extensions = excluded_image_extensions + excluded_media_extension + excluded_execution_extensions


def get_files(path, path_level=0):
    if not os.path.exists(path) or path == '':
        return None

    rom_files = []

    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file not in excluded_files and not file.endswith(tuple(excluded_extensions)):
                rom_files.append(RomFile(root, file, path_level))

        if len(dirs) > 0:
            path_level += 1
            for sub_path in dirs:
                get_files(os.path.join(root, sub_path), path_level)

    return rom_files

