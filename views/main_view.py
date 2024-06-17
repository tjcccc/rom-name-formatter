import tkinter as tk
from tkinter import ttk
from views.directories_form import DirectoriesForm
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

        main_frame = ttk.Frame(self.root, padding=Layout.spacing(2))
        main_frame.grid(sticky='nsew')
        main_frame.columnconfigure(0, weight=1)

        self.directories_form_container = DirectoriesForm(main_frame, self.config_service, self.directories_on_change)
        self.directories_form_container.grid(column=0, row=0, padx=Layout.spacing(2), sticky='ew')

        test_label = ttk.Label(main_frame, textvariable=self.roms_directory)
        test_label.grid(column=0, row=1, sticky='nsew', padx=Layout.spacing(2))

        self.root.mainloop()

    def directories_on_change(self):
        config = self.config_service.load_config()
        self.roms_directory.set(config.roms_directory)
