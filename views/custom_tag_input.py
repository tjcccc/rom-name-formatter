import tkinter as tk
from tkinter import ttk
from styles.app import Layout


class CustomTagInput(ttk.Frame):
    def __init__(self, root, tag, padding=0):
        super().__init__(master=root, padding=padding)
        self.columnconfigure(1, weight=1)

        self.tag = ttk.Entry(self, width=Layout.component_width(2))
        self.tag.grid(column=0, row=0, sticky='w')
        self.input = ttk.Entry(self, width=Layout.component_width(3))
        self.input.grid(column=1, row=0, padx=Layout.spacing(), sticky='w')

        self.tag.insert(0, tag)
