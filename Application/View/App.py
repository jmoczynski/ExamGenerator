import tkinter as tk
from tkinter import font
from Application.Controller.AppController import AppController
from Application.Controller.DBController import DBController
from Application.View.AboutFrame import AboutFrame
from Application.View.AddQuestionListFrame import AddQuestionListFrame
from Application.View.DeleteQuestionFrame import DeleteQuestionFrame
from Application.View.DeleteQuestionListFrame import DeleteQuestionListFrame
from Application.View.ModifyQuestionFrame import ModifyQuestionFrame
from Application.View.EditQuestionListFrame import EditQuestionListFrame
from Application.View.ExportExamFrame import ExportExamFrame
from Application.View.HelpFrame import HelpFrame
from Application.View.ImportCSVFrame import ImportCSVFrame
from Application.View.NewQuestionFrame import NewQuestionFrame
from Application.View.OpenExamFrame import OpenExamFrame
from Application.View.NewExamFrame import NewExamFrame
from Application.View.PreviewExamFrame import PreviewExamFrame
from Application.View.RandomizeQuestionsFrame import RandomizeQuestionsFrame
from Application.View.SaveExamAsFrame import SaveExamAsFrame
from Application.View.SaveExamFrame import SaveExamFrame
from Application.View.StartFrame import StartFrame

class App:

    def __init__(self, *args, **kwargs):
        self._window = tk.Tk()
        self._frame_list = [StartFrame, NewExamFrame, OpenExamFrame, SaveExamFrame, SaveExamAsFrame,
                            PreviewExamFrame, ExportExamFrame, NewQuestionFrame, ModifyQuestionFrame,
                            DeleteQuestionFrame, AddQuestionListFrame, EditQuestionListFrame,
                            DeleteQuestionListFrame, ImportCSVFrame, RandomizeQuestionsFrame, HelpFrame, AboutFrame]
        self.controller = AppController(frames=self._frame_list)
        self.db_controller = DBController()

        self._menubar = tk.Menu(self._window)
        self.__set_menu()

        self.__set_window()
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
        file.add_command(label="Save Exam", command=lambda: self.controller.show_frame("SaveExamFrame"))
        file.add_command(label="Save Exam As", command=lambda: self.controller.show_frame("SaveExamAsFrame"))
        file.add_command(label="Preview Exam", command=lambda: self.controller.show_frame("PreviewExamFrame"))
        file.add_command(label="Export Exam", command=lambda: self.controller.show_frame("ExportExamFrame"))
        file.add_command(label="Exit", command=lambda: self.exit())

        edit = tk.Menu(self._menubar, tearoff=0)
        self._menubar.add_cascade(label="Edit", menu=edit)
        edit.add_command(label="New Question", command=lambda: self.controller.show_frame("NewQuestionFrame"))
        edit.add_command(label="Modify Question", command=lambda: self.controller.show_frame("ModifyQuestionFrame"))
        edit.add_command(label="Delete Question", command=lambda: self.controller.show_frame("DeleteQuestionFrame"))
        edit.add_command(label="New Question List", command=lambda: self.controller.show_frame("AddQuestionListFrame"))
        edit.add_command(label="Edit Question List", command=lambda: self.controller.show_frame("EditQuestionListFrame"))
        edit.add_command(label="Delete Question List", command=lambda: self.controller.show_frame("DeleteQuestionListFrame"))
        edit.add_command(label="Import CSV", command=lambda: self.controller.show_frame("ImportCSVFrame"))
        edit.add_command(label="Randomize Questions", command=lambda: self.controller.show_frame("RandomizeQuestionsFrame"))

        help = tk.Menu(self._menubar, tearoff=0)
        self._menubar.add_cascade(label="Help", menu=help)
        help.add_command(label="Help", command=lambda: self.controller.show_frame("HelpFrame"))
        help.add_command(label="About", command=lambda: self.controller.show_frame("AboutFrame"))

    def view(self):
        self._window.mainloop()

    def exit(self):
        self.db_controller.close()
        exit(0)

