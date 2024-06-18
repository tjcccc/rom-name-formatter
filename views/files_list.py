from tkinter import ttk
from tkinter import filedialog
from models.game_file import GameFile
from services.game_files_service import get_game_files
from services.config_service import ConfigService
from styles.app import Layout


class FilesList(ttk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        style = ttk.Style()
        style.configure('Treeview', rowheight=Layout.component_height(2))
        # style.configure('Treeview.Heading', padding=(Layout.spacing(), Layout.spacing()))

        self.columnconfigure(0, weight=1)

        self.container = ttk.Treeview(self, columns=('id', 'rom_file'), show='headings', style='Treeview', height=Layout.component_height(2))
        self.container.configure(yscrollcommand=ttk.Scrollbar(self, orient='vertical', command=self.container.yview).set)
        self.container.heading('id', text='ID', anchor='w')
        self.container.column('id', minwidth=Layout.component_width(8), width=Layout.component_width(8), stretch=False, anchor='w')
        self.container.heading('rom_file', text='FILE', anchor='w')
        self.container.grid(column=0, row=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.container.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.container.config(yscrollcommand=scrollbar.set)

    def update_list(self, rom_files: [GameFile]):
        # Clear the tree
        for i in self.container.get_children():
            self.container.delete(i)
        if len(rom_files) == 0:
            return
        for index, file in enumerate(rom_files):
            self.container.insert('', 'end', values=(index, file))
