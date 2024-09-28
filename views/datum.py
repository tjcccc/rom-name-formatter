import tkinter as tk
from tkinter import ttk
from tkinter import font
from styles.app import Layout


class Datum(ttk.Frame):
    def __init__(self, root, key, value, padding=0):
        super().__init__(master=root, padding=padding)
        self.columnconfigure(1, weight=1)

        self.key_label = ttk.Label(self, text=key, anchor='w', width=Layout.component_width())
        self.key_label.grid(column=0, row=0, sticky='w')
        self.value_label = ttk.Entry(self, width=Layout.component_width(6))
        self.value_label.grid(column=1, row=0, padx=Layout.spacing(), sticky='ew')
        self.value_label.insert(0, value)
        self.value_label.configure(state='readonly')

        default_font = font.nametofont("TkDefaultFont").actual()
        self.value_label.configure(font=f'"{default_font['family']}" {default_font['size']} bold')

        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label='Copy', command=self.copy_value)
        self.value_label.bind("<Button-3>", self.show_context_menu)


    def get_value(self):
        return self.value_label.get()


    def set_value(self, value):
        self.value_label.configure(state='normal')
        self.value_label.delete(0, 'end')
        self.value_label.insert(0, value)
        self.value_label.configure(state='readonly')


    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)


    def copy_value(self):
        self.value_label.event_generate("<<Copy>>")

