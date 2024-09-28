import tkinter as tk
from tkinter import ttk
from tkinter import font
from styles.app import Layout


class FormInput(ttk.Frame):
    def __init__(self, root, label_text, input_width, padding=0, state='normal', on_change=None):
        super().__init__(master=root, padding=padding)
        self.columnconfigure(1, weight=1)

        self.label = ttk.Label(self, text=label_text, anchor='w', width=Layout.component_width())
        self.label.grid(column=0, row=0, sticky='w')
        self.input = ttk.Entry(self, width=input_width, state=state)
        self.input.grid(column=1, row=0, padx=Layout.spacing(), sticky='ew')

        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label='Copy', command=self.copy_value)
        self.context_menu.add_command(label='Paste', command=self.paste_value)
        self.input.bind("<Button-3>", self.show_context_menu)

        if on_change:
            self.input.bind('<KeyRelease>', on_change)


    def use_mono_font(self):
        mono_font = ''
        if 'Consolas' in font.families():
            mono_font = 'Consolas'
        elif 'SF Mono' in font.families():
            mono_font = 'SF Mono'
        elif 'Menlo' in font.families():
            mono_font = 'Menlo'
        elif 'Noto Mono' in font.families():
            mono_font = 'Noto Mono'
        elif 'Monospace' in font.families():
            mono_font = 'Monospace'
        self.input.configure(font=(mono_font, 9))


    def get_input(self):
        return self.input.get()


    def set_readonly_input(self, value):
        self.input.config(state='normal')
        self.input.delete(0, tk.END)
        self.input.insert(0, value)
        self.input.config(state='disabled')


    def set_input(self, value):
        self.input.config(state='normal')
        self.input.delete(0, tk.END)
        self.input.insert(0, value)


    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)


    def copy_value(self):
        self.input.event_generate("<<Copy>>")


    def paste_value(self):
        self.input.event_generate("<<Paste>>")
