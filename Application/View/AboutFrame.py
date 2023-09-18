import tkinter as tk
from tkinter import Frame

class AboutFrame(Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,  background="White")
        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        title = tk.Label(self, text="About", font=self.title_font, anchor="n")
        title.pack(side="top", fill="x")