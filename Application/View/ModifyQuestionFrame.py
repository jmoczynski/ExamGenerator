import tkinter as tk
from tkinter import Frame

class ModifyQuestionFrame(Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,  background="White")

        self.canvas = tk.Canvas(self)
        self.canvas.config(scrollregion=(0, 0, 1024, 980 * 16), width=1024, height=980 * 8)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.scrollbar = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(expand="yes", side="top", fill="both", anchor="nw")

        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        title = tk.Label(self.canvas, text="Modify Question", font=self.title_font)
        title.pack(side="top", fill="x", anchor="n")

        self.questions = self.get_questions()
        tk.Label(self.canvas, text="Question List").pack(side="top", anchor="nw")

        self.questions_listbox_update_button = tk.Button(self.canvas, text="Update Questions List", command=lambda: self.get_questions())
        self.questions_listbox_update_button.pack(side="top", anchor="nw")

        self.current_question = tk.Label(self.canvas, text="[Current Question Shows up Here]")
        self.current_question.pack(side="top", anchor="nw")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def get_questions(self):
        questions = self.controller.get_questions()
        return questions