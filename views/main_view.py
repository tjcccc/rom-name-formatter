import math
import tkinter as tk
from tkinter import ttk
from models.game_file import GameFile, GameFileType
from models.tag_value import TagValue
from views.custom_tag_input import CustomTagInput
from views.directories_form import DirectoriesForm
from views.files_list import FilesList
from views.datum import Datum
from views.form_input import FormInput
from services.config_service import ConfigService
from services.tag_values_service import make_tag_values_by_tags, get_tags
from services.game_files_service import get_formatted_filename_by_tags
from styles.app import Layout


class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x1000')
        self.root.title('Rom Name Formatter')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)

        self.config_service = ConfigService('./config.json')
        self.config = self.config_service.load_config()
        self.tag_values = make_tag_values_by_tags(self.config.tags)

        # self.roms_directory = tk.StringVar(value=config.roms_directory)
        # self.saves_directory = tk.StringVar(value=self.config.saves_directory)
        # self.states_directory = tk.StringVar(value=self.config.states_directory)

        self.selected_file: GameFile | None = None

        main_frame = ttk.Frame(self.root, padding=Layout.spacing(2))
        main_frame.grid(row=0, sticky='nsew')
        main_frame.columnconfigure(0, weight=1)

        # Directories of Roms, Saves, and States
        self.directories_form_container = DirectoriesForm(main_frame, self.config_service, self.directories_on_change)
        self.directories_form_container.grid(column=0, row=0, sticky='ew', padx=Layout.spacing(2))

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

        # Current Selected File's Original Name
        self.selected_file_name = Datum(main_frame, 'OLD', '', padding=Layout.spacing())
        self.selected_file_name.grid(column=0, row=3, sticky='ew', padx=Layout.spacing())
        self.new_file_name_preview = Datum(main_frame, 'NEW', '', padding=Layout.spacing())
        self.new_file_name_preview.grid(column=0, row=4, sticky='ew', padx=Layout.spacing())

        # New File Name Format
        self.new_file_name_format = FormInput(main_frame, 'FORMAT', Layout.component_width(12), padding=Layout.spacing(), on_change=self.on_change_file_format)
        self.new_file_name_format.grid(column=0, row=5, sticky='ew', padx=Layout.spacing())
        self.new_file_name_format.use_mono_font()
        self.new_file_name_format.set_input(self.config.name_format)

        # Tag Input Group
        self.tags_header = ttk.Frame(main_frame)
        self.tags_header.grid(column=0, row=6, sticky='ew')
        self.tags_label = ttk.Label(self.tags_header, text='TAGS', anchor='w', width=Layout.component_width())
        self.tags_label.grid(column=0, row=6, sticky='w', padx=(Layout.spacing(2), Layout.spacing()), pady=(Layout.spacing(), 0))
        self.add_tag_input_button = ttk.Button(self.tags_header, text='+', command=self.add_custom_tag_input)
        self.add_tag_input_button.grid(column=1, row=6, sticky='w', pady=(Layout.spacing(), 0))
        self.save_tags_button = ttk.Button(self.tags_header, text='SAVE TAGS', command=self.save_tags, padding=(Layout.spacing(), 1))
        self.save_tags_button.grid(column=2, row=6, sticky='w', pady=(Layout.spacing(), 0))
        # self.tags_label.columnconfigure(0, weight=1)
        # self.add_tag_input_button.columnconfigure(1, weight=0)
        self.tags_container = ttk.Frame(main_frame)
        self.tags_container.grid(column=0, row=7, sticky='ew', padx=Layout.spacing(2))
        for index, tag_value in enumerate(self.tag_values):
            column_number = int(index % 3)
            row_number = int(math.floor(index / 3))
            custom_tag_input = CustomTagInput(self.tags_container, tag_value, self.update_new_filename, padding=Layout.spacing())
            custom_tag_input.grid(column=column_number, row=row_number, sticky='ew', padx=Layout.spacing())

        # Rename Button
        self.rename_button = ttk.Button(self.root, text='RENAME', padding=Layout.spacing(2), command=self.rename)
        self.rename_button.grid(column=0, row=1, sticky='ews', padx=Layout.spacing(2), pady=(Layout.spacing(2), Layout.spacing(4)))

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

        # Update components
        self.selected_file_name.set_value(file.get_file_fullname())
        self.new_file_name_preview.set_value(file.get_file_fullname())
        self.update_new_filename()

        print(file.get_path())


    def update_new_filename(self):
        if self.selected_file is None:
            return
        raw_new_filename = self.new_file_name_format.get_input()
        new_formatted_filename = get_formatted_filename_by_tags(self.tag_values, raw_new_filename, self.selected_file)
        self.new_file_name_preview.set_value(new_formatted_filename)
        print(new_formatted_filename)


    def on_change_file_format(self, event):
        self.update_new_filename()
        self.config.name_format = self.new_file_name_format.get_input()
        self.config_service.save_config(self.config)


    def add_custom_tag_input(self):
        if len(self.tag_values) == 24:
            return
        new_tag_value = TagValue(len(self.tag_values), '', '')
        self.tag_values.append(new_tag_value)
        tags_count = len(self.tag_values)
        new_index = tags_count - 1
        column_number = int(new_index % 3)
        row_number = int(math.floor(new_index / 3))
        new_custom_tag_input = CustomTagInput(self.tags_container, new_tag_value, self.update_new_filename, padding=Layout.spacing())
        new_custom_tag_input.grid(column=column_number, row=row_number, sticky='ew', padx=Layout.spacing())


    def save_tags(self):
        updated_tags = get_tags(self.tag_values)
        self.config.tags = updated_tags
        self.config_service.save_config(self.config)


    def rename(self):
        print(self.selected_file)
        print(self.new_file_name_preview.get_value())
