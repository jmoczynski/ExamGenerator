import tkinter as tk

class View:

    def __init__(self):
        self._window = tk.Tk()
        self._window.geometry("1024x980")
        self._title = self._window.title("ExamGenerator")

    def view(self):
        self._window.mainloop()