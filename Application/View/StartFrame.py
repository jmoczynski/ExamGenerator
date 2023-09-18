import tkinter as tk
from tkinter import Frame

class StartFrame(Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="White", width="1024", height="980")
        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        label = tk.Label(self, text="Welcome to ExamGenerator", font=self.title_font)
        label.pack(side="top", fill="both")