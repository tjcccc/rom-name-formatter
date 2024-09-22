import tkinter as tk
from tkinter import ttk
from styles.app import Layout


class FormInput(ttk.Frame):
    def __init__(self, root, label_text, input_width, padding=0, state='normal', on_change=None):
        super().__init__(master=root, padding=padding)
        self.columnconfigure(1, weight=1)

        self.label = ttk.Label(self, text=label_text, anchor='w', width=Layout.component_width())
        self.label.grid(column=0, row=0, sticky='w')
        self.input = ttk.Entry(self, width=input_width, state=state, )
        self.input.grid(column=1, row=0, padx=Layout.spacing(), sticky='ew')

        if on_change:
            self.input.bind('<KeyRelease>', on_change)

    def get_input(self):
        return self.input.get()

    def set_input(self, value):
        self.input.config(state='normal')
        self.input.delete(0, tk.END)
        self.input.insert(0, value)
        self.input.config(state='disabled')
