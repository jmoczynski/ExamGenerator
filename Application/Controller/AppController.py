import tkinter as tk

class AppController:

    def __init__(self, frames: list()):
        container = tk.Frame()
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight="2")
        container.grid_columnconfigure(0, weight="2")

        self.frames = {}
        for F in (frames):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0)

        self.show_frame("NewExamFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()