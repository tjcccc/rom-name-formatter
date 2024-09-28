import os
from models.game_file import GameFile


excluded_system_files = ['desktop.ini', 'Thumbs.db', '.DS_Store', '.localized', '.gitignore']
excluded_image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
excluded_media_extension = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpg', '.mpeg', '.m4v', '.3gp']
excluded_execution_extensions = ['.exe', '.bat', '.sh', '.cmd', '.com', '.msi', '.jar', '.app', '.apk', '.ipa', '.deb', '.rpm', '.dmg', '.pkg']

excluded_files = excluded_system_files
excluded_extensions = excluded_image_extensions + excluded_media_extension + excluded_execution_extensions


def get_game_files(path, specific_name=None):
    if not os.path.exists(path) or path == '':
        return []

    game_files = []

    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file not in excluded_files and not file.endswith(tuple(excluded_extensions)):
                game_file = GameFile(root, file)
                if specific_name is None or specific_name == game_file.get_filename():
                    game_files.append(game_file)

        if len(dirs) > 0:
            for sub_path in dirs:
                get_game_files(os.path.join(root, sub_path), specific_name)

    return game_files


def rename_game_file(game_file: GameFile, new_name: str):
    file_extension = game_file.get_file_extension()
    new_file_fullname = new_name + file_extension
    os.rename(game_file.get_path(), os.path.join(game_file.get_full_dir(), new_file_fullname))


def rename_game_files(game_files: list, new_name: str):
    for game_file in game_files:
        rename_game_file(game_file, new_name)


def get_formatted_filename_by_tags(tag_values: list, raw_filename: str, original_filename: GameFile | None):
    formatted_filename = raw_filename
    for tag_value in tag_values:
        formatted_filename = formatted_filename.replace('{' + tag_value.tag + '}', tag_value.value)

    if original_filename is None:
        return formatted_filename

    original_filename_without_extension = original_filename.get_filename()
    extension = original_filename.get_file_extension()
    formatted_filename = formatted_filename.replace('{old_name}', original_filename_without_extension)
    formatted_filename = formatted_filename.replace('{ext}', extension)
    return formatted_filename
