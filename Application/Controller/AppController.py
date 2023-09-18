import tkinter as tk

class AppController:

    def __init__(self, frames: list()):
        self.container = tk.Frame()
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight="2")
        self.container.grid_columnconfigure(0, weight="2")

        self.frames = {}
        for F in (frames):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="n")

        self.show_frame("StartFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()