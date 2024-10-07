import os
from views.main_view import MainView
from models.game_file import GameFile, GameFileType
from models.game_directory import GameDirectory


config_path = 'config.json'


def generate_files_directory(path, file_type=GameFileType.ROM):
    if not os.path.exists(path) or path == '':
        return None
    game_directory = GameDirectory(path, file_type)
    return game_directory


def rename_file(game_file: GameFile, new_name: str):
    file_extension = game_file.get_file_extension()
    new_file_fullname = new_name + file_extension
    os.rename(game_file.get_path(), os.path.join(game_file.get_full_dir(), new_file_fullname))


if __name__ == "__main__":
    MainView()
