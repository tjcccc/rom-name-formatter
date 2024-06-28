from tkinter import ttk
from tkinter import font
from styles.app import Layout


class Datum(ttk.Frame):
    def __init__(self, root, key, value, padding=0):
        super().__init__(master=root, padding=padding)
        self.columnconfigure(1, weight=1)

        self.key_label = ttk.Label(self, text=key, anchor='w', width=Layout.component_width())
        self.key_label.grid(column=0, row=0, sticky='w')
        self.value_label = ttk.Label(self, text=value,  width=Layout.component_width(6))
        self.value_label.grid(column=1, row=0, padx=Layout.spacing(), sticky='ew')

        default_font = font.nametofont("TkDefaultFont").actual()
        self.value_label.configure(font=f'"{default_font['family']}" {default_font['size']} bold')

    def get_value(self):
        return self.value_label['text']

    def set_value(self, value):
        self.value_label.config(text=value)
