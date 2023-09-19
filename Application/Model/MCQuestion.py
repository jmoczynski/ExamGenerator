# Question class
from Question import Question
class MCQuestion(Question):

    # constructor for Question
    def __init__(self, question="Question?", answers=None, solutions=None):
        super().__init__()
        self.set_question(question)
        self._answers = answers
        self._solutions = solutions

    # accessor for question property of Question
    def get_question(self):
        return self._question

    # accessor for answers property of Question
    def get_answers(self):
        return self._answers

    # accessor for solution property of Question
    def get_solutions(self):
        return self._solutions

    # mutator for question property of Question
    def set_question(self, question: str):
        if len(question) < 1:
            raise ValueError("Question property of Question must have a length of at least 1.")
        super().set_question(question)

    # mutator for answers property of Question
    def set_answers(self, answers: list[str]):
        if len(answers) < 1:
            raise ValueError("There must be at least 1 item in the Answer property of Question.")
        self._answers = answers

    # mutator for solution property of Question
    def set_solutions(self, solutions: set[int]):
        answers = self.get_answers()
        if len(solutions) > len(answers) or len(solutions) < 1:
            raise ValueError("Solutions property of Question must have at least 1 element and a size within indices of Answers property of Question.")
        for i in solutions:
            if i < 0 or i >= len(answers):
                raise ValueError("Each element of Solutions property of Question must be within indices of Answers property of Question.")
        self._solutions = solutions

    def __repr__(self):
        rep_str = ""
        rep_str = rep_str + self.get_question()
        answers = self.get_answers()
        for i in range(len(answers)):
            rep_str = rep_str + "\n\t" + str(i+1) + ". " + answers[i]
        rep_str = rep_str + "\nSolution(s):"
        solutions = self.get_solutions()
        for i in solutions:
            rep_str = rep_str + "\n\t" + str(i+1) + ". " + answers[i]
        rep_str = rep_str + "\n"
        return rep_str
