import tkinter as tk

from Application.Controller.DBController import DBController
from Application.Controller.EditQuestionController import EditQuestionController
from Application.Controller.NewQuestionController import NewQuestionController


class AppController:

    def __init__(self, frames: list(), db_controller: DBController):
        self.container = tk.Frame()
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight="2")
        self.container.grid_columnconfigure(0, weight="2")

        self.newquestion_controller = NewQuestionController(db_controller=db_controller)
        self.modifyquestion_controller = EditQuestionController(db_controller=db_controller)

        self.frames = {}
        for F in (frames):
            page_name = F.__name__
            if page_name == "NewQuestionFrame":
                frame = F(parent=self.container, controller=self.newquestion_controller)
            elif page_name == "ModifyQuestionFrame":
                frame = F(parent=self.container, controller=self.modifyquestion_controller)
            else:
                frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()