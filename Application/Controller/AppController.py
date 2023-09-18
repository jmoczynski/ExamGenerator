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

        self._current_frame = None
        self.show_frame("StartFrame")

    def show_frame(self, page_name):
        if self._current_frame is not None:
            self._current_frame.destroy()
        frame = self.frames[page_name]
        self._current_frame = frame
        frame.tkraise()