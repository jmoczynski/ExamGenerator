import tkinter as tk

class View:

    def __init__(self):
        self._window = tk.Tk()

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
        file.add_command(label="New Exam", command=None)
        file.add_command(label="Open Exam", command=None)
        file.add_command(label="Save Exam", command=None)
        file.add_command(label="Save Exam As", command=None)
        file.add_command(label="Preview Exam", command=None)
        file.add_command(label="Export Exam", command=None)
        file.add_command(label="Exit", command=None)

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