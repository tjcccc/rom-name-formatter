import tkinter as tk
from tkinter import ttk
from models.game_directory import GameDirectory
from models.game_file import GameFile, GameFileType
from views.directories_form import DirectoriesForm
from views.files_list import FilesList
from services.config_service import ConfigService
from styles.app import Layout


class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x1000')
        self.root.title('Rom Name Formatter')
        self.root.columnconfigure(0, weight=1)

        self.config_service = ConfigService('./config.json')
        config = self.config_service.load_config()

        self.roms_directory = tk.StringVar(value=config.roms_directory)
        # self.saves_directory = tk.StringVar(value=self.config.saves_directory)
        # self.states_directory = tk.StringVar(value=self.config.states_directory)

        self.selected_file: GameFile | None = None

        main_frame = ttk.Frame(self.root, padding=Layout.spacing(2))
        main_frame.grid(sticky='nsew')
        main_frame.columnconfigure(0, weight=1)

        # Directories of Roms, Saves, and States
        self.directories_form_container = DirectoriesForm(main_frame, self.config_service, self.directories_on_change)
        self.directories_form_container.grid(column=0, row=0, padx=Layout.spacing(2), sticky='ew')

        # Clear and Load Directories and Buttons
        button_group = ttk.Frame(main_frame)
        button_group.grid(column=0, row=1, sticky='ew')
        button_group.columnconfigure(0, weight=1)
        button_group.columnconfigure(3, weight=1)
        clear_button = ttk.Button(button_group, text='CLEAR', command=self.directories_form_container.clear)
        clear_button.grid(column=1, row=1, pady=Layout.spacing(2))
        load_roms_directory_button = ttk.Button(button_group, text='LOAD', command=self.load_roms_directory)
        load_roms_directory_button.grid(column=2, row=1, pady=Layout.spacing(2))

        # Rom Files List
        self.files_list = FilesList(main_frame)
        self.files_list.grid(column=0, row=2, padx=Layout.spacing(), pady=Layout.spacing(), sticky='nsew')

        self.root.mainloop()

    def directories_on_change(self):
        pass
        # config = self.config_service.load_config()
        # self.roms_directory.set(config.roms_directory)

    def load_roms_directory(self):
        config = self.config_service.load_config()
        roms_path = config.roms_directory
        roms_files = self.directories_form_container.load_roms_directory()
        # game_directory = GameDirectory(config.roms_directory, file_type=GameFileType.ROM)
        self.files_list.update_list(roms_path, roms_files, self.on_click_the_file)

    def on_click_the_file(self, event):
        if event.type != '5':
            return
        item = self.files_list.container.selection()[0]
        file_index = int(self.files_list.container.item(item, 'values')[0]) - 1
        file = self.files_list.get_file_by_index(file_index)
        self.selected_file = file
        print(file.get_path())
