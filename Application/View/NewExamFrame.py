import tkinter as tk
from tkinter import Frame
from Application.View import App as app
from Application.Controller import AppController

class NewExamFrame(Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="64", weight="bold")
        label = tk.Label(self, text="New Exam", font=self.title_font)
        label.pack(side="top", fill="x", pady=16)