import tkinter as tk
import customtkinter
import time
import os
import sys
from PIL import Image, ImageTk
import others
from serial_interface import write_to_computer as write

class Window:
    padding = 3
    button_size = 50
    def __init__(self, edit):
        self.converter = LatexToImage()
        self.edit = edit
        # creates the Tkinter object with some style parameters
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.window = customtkinter.CTk()
        # Makes the window full screen to use full screen size
        self.window.attributes('-fullscreen', True)  
        # gives the ability to restart the app with the Escape key
        self.window.bind("<Escape>", self.restart_app)
        #hides the cursor
        self.window.config(cursor="none")
        # listens to key pressos
        self.window.bind("<Key>", self.keyboard_event)

        # sets up the sidebar
        self.sidebar = customtkinter.CTkFrame(self.window, border_width=1)
        self.sidebar.pack(side="left", fill="y", expand=False)

        # sets up the buttons on the sidebar
        self.toggle_editor_button = customtkinter.CTkButton(self.sidebar, width=self.button_size, height=self.button_size, text="on", command=self.toggle_editor)
        self.storage_button = customtkinter.CTkButton(self.sidebar, width=self.button_size, height=self.button_size, text="use", command=self.toggle_storage)
        self.toggle_editor_button.pack(anchor="center", padx=self.padding, pady=(self.padding, 0))
        self.storage_button.pack(anchor="center", padx=self.padding, pady=(self.padding, 0))

        # sets up the part of the gui which shows the tex-string 
        self.latex_render_window = customtkinter.CTkFrame(self.window, border_width=1)
        self.latex_render_window.pack(side="right", fill="both", expand=True)
        self.tex = customtkinter.CTkLabel(self.latex_render_window, text="moin", wraplength=1200)
        self.tex.pack(side="left", padx=self.padding, pady=(self.padding, 0))
        self.setup_editor_variables()
        self.window.update()

    # sets up variables to store the state of the sidebar buttons
    def setup_editor_variables(self):
        self.set_storage = False
        self.active_editor = True
    
    # funtion to change the editor between using the editor and directly writing the tex string to the computer
    def toggle_editor(self):
        if self.active_editor:
            self.active_editor = False
            self.toggle_editor_button.set_text("off")
        else:
            self.active_editor = True
            self.toggle_editor_button.set_text("on")

    # toggles the custom programmable button between saving and using
    def toggle_storage(self):
        if self.set_storage:
            self.set_storage = False
            self.storage_button.set_text("use")
            self.edit.clear()
        else:
            self.set_storage = True
            self.storage_button.set_text("save")

    # updates the tex-string on the qui
    def latex_render(self, tex_string=""):
        self.tex['text'] = tex_string

    # placeholder function
    def arrows(self):
        pass

    # placeholder function
    def number_space(self):
        pass
    
    # adds a text element to the editor with the pressed key of the external keyboard
    def keyboard_event(self, key):
        if self.active_editor:
            self.edit.add_element(others.KeyboardText(key.char))
        else:
            write(key.char)

    # funtion to restart the app
    def restart_app(self, event):
        self.window.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)


