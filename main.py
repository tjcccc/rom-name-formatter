import os
import tkinter as tk
from models.rom_file import RomFile


def get_files(path, level=0):
    if not os.path.exists(path) or path == '':
        return None

    rom_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if len(dirs) > 0:
                for sub_path in dirs:
                    get_files(os.path.join(root, sub_path), level)
                    rom_files.append(RomFile(root, file, level))
            else:
                rom_files.append(RomFile(root, file, 0))

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
    my_rom_files = get_files('')

    if my_rom_files is None:
        print('No files')
        exit(0)

    for rom_file in my_rom_files:
        print(f'{rom_file.get_dir_level()} - {rom_file}')
        # if rom_file.get_filename() == "ne_game":
        #     rename_file(rom_file, "renamed_game")
