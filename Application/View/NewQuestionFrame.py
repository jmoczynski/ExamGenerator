import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
from Application.View import App

class NewQuestionFrame(Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,  background="White")

        self.canvas = tk.Canvas(self)
        self.canvas.config(scrollregion=(0,0,1024,980*16), width=1024, height=980*8)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

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
        self.question_button = tk.Button(question_frame, text="Update Question")
        self.question_button.config(command=lambda: self.update_question())
        self.question_button.pack(side="top", anchor="nw")
        self.question = ""

        self.num_answers_button = None

        self.answers_button = None
        self.answers_label = None
        self.answer_frame = None
        self.answer_message = None
        self.answer_boxes = []
        self.answer_values = []

        self.mc_solutions_frame = None
        self.or_solution_frame = None

        self.solutions = dict()
        self.solutions_button = None

        self.suggested_solution_button = None

    def update_question(self):
        if self.check_question():
            self.question = self.question_text.get("1.0", "end-1c")
            print(self.question)


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

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
        if not result and self.num_answers_button is not None:
            self.num_answers_button.config(state="disabled")
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
            self.num_answers_button = tk.Button(self.answer_frame, text="Enter Choice Amount", state="disabled", command=lambda: self.set_choices_entry(num_answers.get()))
            self.num_answers_button.pack(side="top", anchor="nw")
        elif self.or_solution_frame is not None:
            tk.Label(self.or_solution_frame, text="Enter suggested solution.").pack(side="top", anchor="nw")
            suggested_solution = tk.Text(self.or_solution_frame, height=5)
            suggested_solution.pack(side="top", anchor="nw")
            self.suggested_solution_button = tk.Button(self.or_solution_frame, command=self.create_or_question(suggested_solution))
            self.suggested_solution_button.pack(side="top", anchor="nw")

        self.previous_selection = result
    def choices_count_validation(self, p):
        if (str.isnumeric(p) and int(p, 10) <= 10) or p == "":
            return True
        return False

    def set_choices_entry(self, num_answers):
        if num_answers != "" and int(num_answers) > 1:
            self.answer_message.config(text="Amount of Choices is valid.", fg="Green")
            self.num_answers_button.config(state="disabled")
            self.answer_boxes = []
            for i in range(int(num_answers)):
                answer_field = tk.Text(self.answer_frame, height=5)
                tk.Label(self.answer_frame, text=str(i+1) + ".").pack(side="top", anchor="nw")
                answer_field.pack(side="top", anchor="nw", expand="no")
                self.answer_boxes.append(answer_field)
            self.answers_button = tk.Button(self.answer_frame, text="Enter Answers", command=lambda: self.check_answers(self.answer_boxes))
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
        self.canvas.create_window(0, 2000, window=self.mc_solutions_frame, anchor="nw")

        tk.Label(self.mc_solutions_frame, text="Question: " + self.question_text.get("1.0", "end")).pack(side="top", anchor="nw")
        for i in range(len(answers)):
            a_str = answers[i].get(index1="1.0", index2="end-1c")
            self.answer_values.append(a_str)
            a_label = str(i+1) + ". " + a_str
            tk.Label(self.mc_solutions_frame, text=a_label, fg="Black").pack(side="top", anchor="nw")

        self.check_solutions()

    def solutions_count_validation(self, p):
        if (str.isnumeric(p) and int(p, 10) <= 10) or p == "":
            return True
        return False

    def check_solutions(self):
        self.question_button.config(state="disabled")
        for i in range(len(self.answer_boxes)):
            self.solutions[str(i)] = tk.IntVar()
            solution_choice_box = tk.Checkbutton(self.mc_solutions_frame, variable=self.solutions[str(i)], text=self.answer_boxes[i].get("1.0", "end-1c"), onvalue=1, offvalue=0)
            solution_choice_box.config(command=lambda: self.print_solutions())
            solution_choice_box.pack(side="top", anchor="nw")
        self.solutions_button = tk.Button(self.mc_solutions_frame, text="Submit Solutions", command=lambda: self.create_mc_question())
        self.solutions_button.pack(side="top", anchor="nw")

    def print_solutions(self):
        for j in range(len(self.solutions)):
            print(str(j+1) + ": " + str(self.solutions[str(j)].get()))

    def create_mc_question(self):
        solutions_list = []
        for s in self.solutions.keys():
            if self.solutions.get(s).get() == 1:
                solutions_list.append(s)
        try:
            question = self.controller.create_mc_question(self.question, self.answer_values, solutions_list)
            self.solutions_button.config(state="disabled")
            if question is not None:
                tk.messagebox.showinfo(message="Question created successfully.")
            else:
                tk.messagebox.showerror(message="Cannot create Question.")
                return
        except (Exception):
            tk.messagebox.showerror(message="Cannot create Question.")
            return

    def create_or_question(self, suggested_solution_field: tk.Text):
        try:
            solution = suggested_solution_field.get("1.0", "end-1c").strip()
            if len(solution) < 1:
                raise Exception("Cannot have an empty suggested solution.")
            self.suggested_solution_button.config(state="disabled")
            question = self.controller.create_or_question(self.question, solution)
        except (Exception):
            tk.messagebox.showerror(message="Cannot create Question.")
        return

    def check_question(self):
        result = False
        question = self.question_text.get("1.0", "end-1c")
        if len(question) < 1 or len(question.strip()) < 1:
            self.question_check.config(text="Question must not be empty.", fg="Red")
            self.question_check.pack(side="top", anchor="nw")
            if self.num_answers_button is not None:
                self.num_answers_button.config(state="disabled")
        else:
            self.question_check.config(text="Question is valid.", fg="Green")
            self.question_check.pack(side="top", anchor="nw")
            if self.num_answers_button is not None:
                self.num_answers_button.config(state="active")
            result = True
        return result