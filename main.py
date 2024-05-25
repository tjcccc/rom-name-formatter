import os
import sys
import tkinter as tk
from models.game_file import GameFile, GameFileType
from models.game_directory import GameDirectory
from services.game_directories_service import rename_game_directory_name
from services.game_files_service import get_game_files, rename_game_files


def generate_files_directory(path, file_type=GameFileType.ROM):
    if not os.path.exists(path) or path == '':
        return None
    game_directory = GameDirectory(path, file_type)
    return game_directory


# def get_files(path, path_level=0):
#     if not os.path.exists(path) or path == '':
#         return None
#
#     rom_files = []
#
#     for root, dirs, files in os.walk(path, topdown=True):
#         for file in files:
#             rom_files.append(RomFile(root, file, path_level))
#
#         if len(dirs) > 0:
#             path_level += 1
#             for sub_path in dirs:
#                 get_files(os.path.join(root, sub_path), path_level)
#
#     return rom_files


def rename_file(game_file: GameFile, new_name: str):
    file_extension = game_file.get_file_extension()
    new_file_fullname = new_name + file_extension
    os.rename(game_file.get_path(), os.path.join(game_file.get_full_dir(), new_file_fullname))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello, Tkinter!")
        self.geometry("300x150")
        self.label = tk.Label(self, text="Hello, Tkinter!", font=("Helvetica", 24))
        self.label.pack(padx=20, pady=20)


if __name__ == "__main__":
    # app = App()
    # app.mainloop()

    # test
    args = sys.argv[1:]
    if len(args) == 0:
        print('Please provide a path.')
        exit(0)
    root_path = os.path.expanduser(args[0]) if args[0][0] == '~' else args[0]
    if not os.path.exists(root_path):
        print(f'Invalid path: {root_path}')
        exit(0)

    game_files_directory = generate_files_directory(root_path)
    game_files_directory.debug_print(0, root_path)

    old_dir_name = 'ss game'
    new_dir_name = 'saturn'

    ss_game_directory: GameDirectory
    if game_files_directory.get_folder_name() == old_dir_name:
        rename_game_directory_name(game_files_directory, new_dir_name)
        # game_files_directory = generate_files_directory(root_path)
        game_files_directory.debug_print(0, root_path)
    else:
        for sub_game_directory in game_files_directory.sub_directories:
            if sub_game_directory.get_folder_name() == old_dir_name:
                rename_game_directory_name(sub_game_directory, new_dir_name)
                # game_files_directory = generate_files_directory(root_path)
                game_files_directory.debug_print(0, root_path)
                break


    # game_files = get_game_files(root_path)
    # for game_file in game_files:
    #     print(game_file.get_file_fullname())
    # print(f'Found {len(game_files)} files.')

    # search_files = get_game_files(root_path, specific_name='game')
    # for search_file in search_files:
    #     print(search_file.get_file_fullname())
    # print(f'Found {len(search_files)} files.')

    # rename_game_files(search_files, 'new game')
    # print('Renamed files.')
    # game_files = get_game_files(root_path)
    # for game_file in game_files:
    #     print(game_file.get_file_fullname())
    # print(f'Found {len(game_files)} files.')
