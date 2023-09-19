import tkinter as tk
from tkinter import Frame
from Application.View import App

class NewQuestionFrame(Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,  background="White")
        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        title = tk.Label(self, text="New Question", font=self.title_font, anchor="n", padx=4, pady=4, background="White")
        title.pack(side="top", fill="both")

        question_type_frame = tk.LabelFrame(self, text="1. Question Type", background="White")
        question_type_frame.pack(expand="no", side="top", fill="both")
        tk.Label(question_type_frame, text="Please choose the Question type.", background="White").pack(side="top", anchor="nw")

        self.radio_var = tk.IntVar(question_type_frame)

        tk.Radiobutton(question_type_frame, text="Multiple Choice", variable=self.radio_var, value=1, fg="Black", background="White", command=lambda: self.selection()).pack(side="top", anchor="nw")
        tk.Radiobutton(question_type_frame, text="Open Response", variable=self.radio_var, value=2, fg="Black", background="White", command=lambda: self.selection()).pack(side="top", anchor="nw")

        question_frame = tk.LabelFrame(self, text="2. Question", background="White")
        question_frame.pack(expand="yes", side="top", fill="both")
        tk.Label(question_frame, text="Please enter the Question.", background="White").pack(side="top", anchor="nw")

        self.question_text = tk.Text(question_frame, background="White")
        self.question_text.pack(side="top", fill="x", anchor="nw")

        self.question_check = tk.Text(question_frame, fg="Red", height=1)
        self.question_check.insert(chars="Please check your question using the button below.", index="end")
        self.question_check.pack(side="top", anchor="nw")
        tk.Button(question_frame, text="Check Validity", command=lambda: self.check_question(question_frame)).pack(side="top", anchor="nw")


    def selection(self):
        selected = self.radio_var.get()
        self.controller.selection(selected)

    def check_question(self, frame):
        self.question_check.delete("1.0", "end")
        question = self.question_text.get("1.0", "end-1c")
        if len(question) < 1 or len(question.strip()) < 1:
            self.question_check.config(fg="Red")
            self.question_check.insert(chars="Question must not be empty.", index="end")
            self.question_check.pack(side="top", anchor="nw")
        else:
            self.question_check.config(fg="Green")
            self.question_check.insert(chars="Question is valid.", index="end")
            self.question_check.pack(side="top", anchor="nw")
