import tkinter as tk
from tkinter import ttk
from models.tag_value import TagValue
from styles.app import Layout


class CustomTagInput(ttk.Frame):
    def __init__(self, root, tag_value: TagValue, on_changed_callback, padding=0):
        super().__init__(master=root, padding=padding)

        self.tag_value = tag_value
        self.on_tag_changed_callback = on_changed_callback
        self.on_input_changed_callback = on_changed_callback

        self.columnconfigure(1, weight=1)

        self.tag = ttk.Entry(self, width=Layout.component_width(2))
        self.tag.grid(column=0, row=0, sticky='w')
        self.tag.bind('<KeyRelease>', self.on_tag_changed)
        self.input = ttk.Entry(self, width=Layout.component_width(3))
        self.input.grid(column=1, row=0, padx=Layout.spacing(), sticky='w')
        self.input.bind('<KeyRelease>', self.on_value_changed)

        self.tag.insert(0, tag_value.tag)

        self.tag_context_menu = tk.Menu(self, tearoff=0)
        self.tag_context_menu.add_command(label='Copy', command=self.copy_tag_value)
        self.tag_context_menu.add_command(label='Paste', command=self.paste_tag_value)
        self.tag.bind("<Button-3>", self.show_tag_context_menu)

        self.input_context_menu = tk.Menu(self, tearoff=0)
        self.input_context_menu.add_command(label='Copy', command=self.copy_input_value)
        self.input_context_menu.add_command(label='Paste', command=self.paste_input_value)
        self.input.bind("<Button-3>", self.show_input_context_menu)

    def show_tag_context_menu(self, event):
        self.tag_context_menu.post(event.x_root, event.y_root)

    def copy_tag_value(self):
        self.tag.event_generate("<<Copy>>")

    def paste_tag_value(self):
        self.tag.event_generate("<<Paste>>")

    def show_input_context_menu(self, event):
        self.input_context_menu.post(event.x_root, event.y_root)

    def copy_input_value(self):
        self.input.event_generate("<<Copy>>")

    def paste_input_value(self):
        self.input.event_generate("<<Paste>>")

    def on_tag_changed(self, event):
        tag = event.widget.get()
        self.tag_value.tag = tag
        self.on_tag_changed_callback()

    def on_value_changed(self, event):
        value = event.widget.get()
        self.tag_value.value = value
        self.on_input_changed_callback()
