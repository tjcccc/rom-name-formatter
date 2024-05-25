import os
from models.game_directory import GameDirectory


def rename_game_directory_name(game_directory: GameDirectory, new_name: str):
    dir_path = game_directory.get_path()
    new_dir_path = os.path.join(os.path.dirname(dir_path), new_name)
    os.rename(dir_path, new_dir_path)
    game_directory.dir_path = new_dir_path
