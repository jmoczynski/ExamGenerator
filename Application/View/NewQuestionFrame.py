import tkinter as tk
from tkinter import Frame
from Application.View import App

class NewQuestionFrame(Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,  background="White")

        self.canvas = tk.Canvas(self)
        self.canvas.config(scrollregion=(0,0,1024,980*16), width=1024, height=980*8)

        self.scrollbar = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(expand="yes", side="top", fill="both", anchor="nw")

        self.controller = controller
        self.title_font = tk.font.Font(family="Helvetica", size="32", weight="bold")
        title = tk.Label(self.canvas, text="New Question", font=self.title_font, anchor="n", padx=4, pady=4, background="White")
        title.pack(side="top", fill="both")
        self.canvas.create_window(0, 0, window=title, anchor="nw")

        self.question_type_frame = tk.LabelFrame(self.canvas, text="1. Question Type", background="White")
        self.question_type_frame.pack(expand="no", side="top", fill="both")
        self.canvas.create_window(0, 200, window=self.question_type_frame, anchor="nw")
        tk.Label(self.question_type_frame, text="Please choose the Question type.", background="White").pack(side="top", anchor="nw")

        self.radio_var = tk.IntVar(self.question_type_frame)
        self.previous_selection = self.controller.get_question_type_selection()

        self.radio_mc = tk.Radiobutton(self.question_type_frame, text="Multiple Choice", variable=self.radio_var, value=1, fg="Black", background="White", command=lambda: self.selection(disable=True))
        self.radio_mc.pack(side="top", anchor="nw")
        self.radio_or = tk.Radiobutton(self.question_type_frame, text="Open Response", variable=self.radio_var, value=2, fg="Black", background="White", command=lambda: self.selection(disable=True))
        self.radio_or.pack(side="top", anchor="nw")

        question_frame = tk.LabelFrame(self.canvas, text="2. Question", background="White")
        question_frame.pack(expand="no", side="top", fill="both")
        self.canvas.create_window(0, 400, window=question_frame, anchor="nw")
        tk.Label(question_frame, text="Please enter the Question.", background="White").pack(side="top", anchor="nw")

        self.question_text = tk.Text(question_frame, background="White", height=5)
        self.question_text.pack(side="top", fill="x", anchor="nw")

        self.question_check = tk.Label(question_frame, fg="Red")
        self.question_check.config(text="Please check your question using the button below.", fg="Red")
        self.question_check.pack(side="top", anchor="nw")

        self.answer_frame = None
        self.answer_message = None

        self.mc_solutions_frame = None
        self.or_solution_frame = None


    def selection(self, disable=False):
        selected = self.radio_var.get()
        if disable:
            self.radio_mc.config(state="disabled")
            self.radio_or.config(state="disabled")

        self.controller.selection(selected)
        if self.previous_selection == 0:
            self.previous_selection = self.controller.selection(selected)
        result = self.check_question()
        print(result)
        if self.controller.get_question_type_selection() == 1:
            if self.answer_frame is None:
                self.answer_frame = tk.LabelFrame(self.canvas, text="3. Multiple Choice Answers", background="White")
                self.answer_frame.pack(expand="no", side="top", fill="both")
                self.canvas.create_window(0, 600, window=self.answer_frame, anchor="nw")
        elif self.controller.get_question_type_selection() == 2:
            if self.or_solution_frame is None:
                self.or_solution_frame = tk.LabelFrame(self.canvas, text="4. Open Response Suggested Solution", background="White")
                self.or_solution_frame.pack(expand="no", side="top", fill="both")
                self.canvas.create_window(0, 600, window=self.answer_frame, anchor="nw")


        if self.answer_frame is not None:
            vcmd = self.register(self.choices_count_validation)
            tk.Label(self.answer_frame, text="Number of choices:").pack(side="top", anchor="nw")
            num_answers = tk.Entry(self.answer_frame, validate="all", validatecommand=(vcmd, "%P"))
            num_answers.pack(side="top", anchor="nw")
            self.answer_message = tk.Label(self.answer_frame, fg="Red", background="White")
            self.answer_message.config(text="Amount of Choices cannot be empty or 0.")
            self.answer_message.pack(side="top", anchor="nw")
            self.num_answers_button = tk.Button(self.answer_frame, text="Enter Choice Amount", command=lambda: self.set_choices_entry(num_answers.get()))
            self.num_answers_button.pack(side="top", anchor="nw")
        elif self.or_solution_frame is not None:
            tk.Label(self.or_solution_frame, text="Enter suggested solution.").pack(side="top", anchor="nw")
            suggested_solution = tk.Text(self.or_solution_frame, height=5).pack(side="top", anchor="nw")

        self.previous_selection = result
    def choices_count_validation(self, p):
        if (str.isnumeric(p) and int(p, 10) <= 10) or p == "":
            return True
        return False

    def set_choices_entry(self, num_answers):
        if num_answers != "" and int(num_answers) > 1:
            self.answer_message.config(text="Amount of Choices is valid.", fg="Green")
            self.num_answers_button.config(state="disabled")
            self.answers = []
            for i in range(int(num_answers)):
                answer_field = tk.Text(self.answer_frame, height=5)
                tk.Label(self.answer_frame, text=str(i+1) + ".").pack(side="top", anchor="nw")
                answer_field.pack(side="top", anchor="nw", expand="no")
                self.answers.append(answer_field)
            self.answers_button = tk.Button(self.answer_frame, text="Enter Answers", command=lambda: self.check_answers(self.answers))
            self.answers_label = tk.Label(self.answer_frame, text="Answers Status")
            self.answers_label.pack(side="top", anchor="nw")
            self.answers_button.pack(side="top", anchor="nw")
        else:
            self.answer_message.config(text="Amount of Choices cannot be empty or 0 or 1.", fg="Red")

    def check_answers(self, answers: list[tk.Text]):
        for a in answers:
            a_str = a.get("1.0", "end-1c")
            if len(a_str) < 1:
                self.answers_label.config(text="At least 1 answer is empty, which is not allowed.", fg="Red")
                return
        self.answers_label.config(text="Answers are accepted.", fg="Green")
        self.answers_button.config(state="disabled")
        self.mc_solutions_frame = tk.LabelFrame(self.canvas, text="4. Multiple Choice Solutions", background="white")
        self.mc_solutions_frame.pack(side="top", expand="no", fill="both", anchor="nw")
        self.canvas.create_window(0, 1200, window=self.mc_solutions_frame, anchor="nw")

        tk.Label(self.mc_solutions_frame, text="Question: " + self.question_text.get("1.0", "end")).pack(side="top", anchor="nw")
        for i in range(len(answers)):
            a_str = answers[i].get(index1="1.0", index2="end-1c")
            a_label = str(i+1) + ". " + a_str
            tk.Label(self.mc_solutions_frame, text=a_label, fg="Black").pack(side="top", anchor="nw")

        self.num_solutions = tk.Entry(self.mc_solutions_frame, text="Enter the number of solutions.")
        self.num_solutions.pack(side="top", anchor="nw")
        self.num_solutions_button = tk.Button(self.mc_solutions_frame, text="Check Number", command=lambda: self.check_solutions())
        self.num_solutions_button.pack(side="top", anchor="nw")

        self.num_solutions_label = None

    def check_solutions(self):
        if len(self.answers) < int(self.num_solutions.get(), 10) or int(self.num_solutions.get(), 10) < 1 or self.num_solutions.get() == "":
            if self.num_solutions_label is None:
                self.num_solutions_label = tk.Label(self.mc_solutions_frame, text="Number of solutions must be between 1 and " + str(len(self.answers)), fg="Red")
                self.num_solutions_label.pack(side="top", anchor="nw")
            else:
                self.num_solutions_label.config(text="Number of solutions must be between 1 and " + str(len(self.answers)))
        else:
            if self.num_solutions_label is None:
                self.num_solutions_label = tk.Label(self.mc_solutions_frame, text="Number of solutions is accepted.", fg="Green")
                self.num_solutions_label.pack(side="top", anchor="nw")
            else:
                self.num_solutions_label.config(text="Number of solutions is accepted.", fg="Green")
                self.num_solutions_label.pack(side="top", anchor="nw")
                self.num_solutions_button.config(state="disabled")

    def check_question(self):
        result = False
        question = self.question_text.get("1.0", "end-1c")
        if len(question) < 1 or len(question.strip()) < 1:
            self.question_check.config(text="Question must not be empty.", fg="Red")
            self.question_check.pack(side="top", anchor="nw")
        else:
            self.question_check.config(text="Question is valid.", fg="Green")
            self.question_check.pack(side="top", anchor="nw")
            result = True
        return result