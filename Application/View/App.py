import tkinter as tk
from tkinter import font
from Application.Controller.AppController import AppController
from Application.View.OpenExamFrame import OpenExamFrame
from Application.View.NewExamFrame import NewExamFrame
from Application.View.StartFrame import StartFrame

class App:

    def __init__(self, *args, **kwargs):
        self._window = tk.Tk()
        self._frame_list = [StartFrame, NewExamFrame, OpenExamFrame]
        self.controller = AppController(frames=self._frame_list)

        self._menubar = tk.Menu(self._window)
        self.__set_menu()

        self.__set_window()

        self.frame1 = None

    def __set_window(self):
        self._window.geometry("1024x980")
        self._title = self._window.title("ExamGenerator")
        self._window.config(menu=self._menubar)

    def __set_menu(self):
        file = tk.Menu(self._menubar, tearoff=0)
        self._menubar.add_cascade(label="File", menu=file)
        file.add_command(label="Back to Start", command=lambda: self.controller.show_frame("StartFrame"))
        file.add_command(label="New Exam", command=lambda: self.controller.show_frame("NewExamFrame"))
        file.add_command(label="Open Exam", command=lambda: self.controller.show_frame("OpenExamFrame"))
        file.add_command(label="Save Exam", command=None)
        file.add_command(label="Save Exam As", command=None)
        file.add_command(label="Preview Exam", command=None)
        file.add_command(label="Export Exam", command=None)
        file.add_command(label="Exit", command=lambda: exit(0))

        edit = tk.Menu(self._menubar, tearoff=0)
        self._menubar.add_cascade(label="Edit", menu=edit)
        edit.add_command(label="New Question", command=None)
        edit.add_command(label="Modify Question", command=None)
        edit.add_command(label="Delete Question", command=None)
        edit.add_command(label="Edit Question List", command=None)
        edit.add_command(label="Import CSV", command=None)
        edit.add_command(label="Randomize Questions", command=None)

        help = tk.Menu(self._menubar, tearoff=0)
        self._menubar.add_cascade(label="Help", menu=help)
        help.add_command(label="Help", command=None)
        help.add_command(label="About", command=None)

    def view(self):
        self._window.mainloop()

