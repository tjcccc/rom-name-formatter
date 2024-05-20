import os
import sys
import tkinter as tk
from models.rom_file import RomFile
from models.rom_directory import RomDirectory


def generate_roms_directory(path):
    if not os.path.exists(path) or path == '':
        return None
    roms_directory = RomDirectory(path)
    return roms_directory


def get_files(path, path_level=0):
    if not os.path.exists(path) or path == '':
        return None

    rom_files = []

    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            rom_files.append(RomFile(root, file, path_level))

        if len(dirs) > 0:
            path_level += 1
            for sub_path in dirs:
                get_files(os.path.join(root, sub_path), path_level)

    return rom_files


def rename_file(rom_file: RomFile, new_name: str):
    file_extension = rom_file.get_file_extension()
    new_file_fullname = new_name + file_extension
    os.rename(rom_file.get_path(), os.path.join(rom_file.get_dir(), new_file_fullname))


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
    rom_directory = generate_roms_directory(root_path)
    rom_directory.debug_print(0, root_path)

