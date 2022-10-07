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
        # gives the ability to quit the app with the Escape key
        self.window.bind("<Escape>", self.quit_app)
        #hides the cursor
        self.window.config(cursor="none")

        self.window.bind("<Key>", self.keyboard_event)

        self.sidebar = customtkinter.CTkFrame(self.window, border_width=1)
        self.sidebar.pack(side="left", fill="y", expand=False)

        self.toggle_editor_button = customtkinter.CTkButton(self.sidebar, width=self.button_size, height=self.button_size, text="on", command=self.toggle_editor)
        self.storage_button = customtkinter.CTkButton(self.sidebar, width=self.button_size, height=self.button_size, text="use", command=self.toggle_storage)
        self.toggle_editor_button.pack(anchor="center", padx=self.padding, pady=(self.padding, 0))
        self.storage_button.pack(anchor="center", padx=self.padding, pady=(self.padding, 0))


        self.latex_render_window = customtkinter.CTkFrame(self.window, border_width=1)
        self.latex_render_window.pack(side="right", fill="both", expand=True)
        self.tex = customtkinter.CTkLabel(self.latex_render_window, text="moin", wraplength=1200)
        self.tex.pack(side="left", padx=self.padding, pady=(self.padding, 0))
        # image = self.converter.make_image("\\alpha")
        # test = Button(self.latex_render, image=image)
        # test.pack(side="left", padx=self.padding, pady=(self.padding, 0))
        self.setup_editor_variables()
        self.window.update()

    def setup_editor_variables(self):
        self.set_storage = False
        self.active_editor = True
    
    def toggle_editor(self):
        if self.active_editor:
            self.active_editor = False
            self.toggle_editor_button.set_text("off")
        else:
            self.active_editor = True
            self.toggle_editor_button.set_text("on")

    def toggle_storage(self):
        if self.set_storage:
            self.set_storage = False
            self.storage_button.set_text("use")
            self.edit.clear()
        else:
            self.set_storage = True
            self.storage_button.set_text("save")

    def latex_render(self, tex_string=""):
        self.tex['text'] = tex_string

    def arrows(self):
        pass

    def number_space(self):
        pass
    
    def keyboard_event(self, key):
        if self.active_editor:
            self.edit.add_element(others.KeyboardText(key.char))
        else:
            write(key.char)

    def quit_app(self, event):
        self.window.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)


class LatexToImage:
    filepath = "conversion_file"
    quality = 1000
    
    # schreibt den string in ein Latex file
    def write_to_latex_file(self, tex_string):
        # oeffnet das Latex file und trennt den Formel Teil heraus (Teil zwischen $ und $)
        with open(f"{self.filepath}.tex", "r") as f:
            content = f.read()
            begin, _, end = content.split("$")
        # schreibt den Latex string in das Dokument und behaelt Anfang und Ende bei.
        with open(f"{self.filepath}.tex", "w") as f:
            f.writelines(f"{begin}${tex_string}${end}")

    # erstellt ein Bild aus dem Latex file
    def convert(self):
        # fuehrt einen Terminal Befehl aug um ein Pdf aus dem Tex file zu erstellen
        os.system(f"pdflatex -interaction=batchmode {self.filepath}.tex")
        # erstellt mit einem Terminal Befehl ein Bild aus dem Pdf
        os.system(f"pdftoppm {self.filepath}.pdf {self.filepath} -png -r {self.quality}")

    # erstellt das Bild und gibt es zurueck
    def make_image(self, tex_string):
        global image
        self.write_to_latex_file(tex_string)
        self.convert()
        # das Bild muss noch im richtigen Format zur Darstellung eingelesen werden.
        image = ImageTk.PhotoImage(file = "conversion_file-1.png")
        return image




if __name__ == '__main__':
    app = Window()
    time.sleep(6)
    print("moin")