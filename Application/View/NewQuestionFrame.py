import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
from Application.View import App

class NewQuestionFrame(Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,  background="White")

        self.canvas = tk.Canvas(self)
        self.canvas.config(scrollregion=(0,0,1024,980*16), width=1024, height=980*8)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.scrollbar = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(expand="yes", side="top", fill="both", anchor="nw")

        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        title = tk.Label(self.canvas, text="New Question", font=self.title_font, padx=4, pady=4, background="White")
        title.pack(side="top", fill="both", anchor="n")
        self.canvas.create_window(0, 0, window=title, anchor="nw")


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")