import tkinter as tk
from tkinter import Frame

class StartFrame(Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="White")
        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        title = tk.Label(self, text="Welcome to ExamGenerator", font=self.title_font)
        title.pack(side="top", fill="x")