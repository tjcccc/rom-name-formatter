from typing import TypedDict
from tkinter import ttk
from tkinter import filedialog
from models.game_file import GameFile
from services.game_files_service import get_game_files
from services.config_service import ConfigService
from styles.app import Layout


class IndexedFile(TypedDict):
    index: int
    file: GameFile


class FilesList(ttk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.indexed_files: [IndexedFile] = []

        style = ttk.Style()
        style.configure('Treeview', rowheight=Layout.component_height(2))
        # style.configure('Treeview.Heading', padding=(Layout.spacing(), Layout.spacing()))

        self.columnconfigure(0, weight=1)

        self.container = ttk.Treeview(self, columns=('id', 'folder', 'rom_file'), show='headings', style='Treeview', height=Layout.component_height(2))
        self.container.configure(yscrollcommand=ttk.Scrollbar(self, orient='vertical', command=self.container.yview).set)
        self.container.heading('id', text='ID', anchor='w')
        self.container.column('id', minwidth=Layout.component_width(8), width=Layout.component_width(8), stretch=False, anchor='w')
        self.container.heading('folder', text='FOLDER', anchor='w')
        self.container.column('folder', minwidth=Layout.component_width(8), width=Layout.component_width(16), stretch=False, anchor='w')
        self.container.heading('rom_file', text='FILE', anchor='w')
        self.container.grid(column=0, row=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.container.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.container.config(yscrollcommand=scrollbar.set)

    def update_list(self, roms_root_path, rom_files: [GameFile], on_click=None):
        # Clear the tree
        for i in self.container.get_children():
            self.container.delete(i)
        if len(rom_files) == 0:
            return
        for index, file in enumerate(rom_files):
            self.indexed_files.append({'index': index, 'file': file})
            self.container.insert('', 'end', values=(index + 1, file.get_relative_path(roms_root_path), file.get_file_fullname()))
        if on_click:
            self.container.bind('<ButtonRelease-1>', on_click)

    def get_file_by_index(self, index: int) -> GameFile:
        # find the file by index in indexed_files
        return next((indexed_file['file'] for indexed_file in self.indexed_files if indexed_file['index'] == index), None)
