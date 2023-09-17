# Question class
class Question:

    # constructor for Question
    def __init__(self, number=None, question=None, answers=None, solution=None):
        self._number = number
        self._question = question
        self._answers = answers
        self._solution = solution

    # accessor for number property of Question
    def get_number(self):
        return self._number

    # accessor for question property of Question
    def get_question(self):
        return self._question

    # accessor for answers property of Question
    def get_answers(self):
        return self._answers

    # accessor for solution property of Question
    def get_solution(self):
        return self._solution

    # mutator for number property of Question
    def set_number(self, number: int):
        if number < 1:
            raise ValueError("Number property of Question must be at least 1.")
        self._number = number

    # mutator for question property of Question
    def set_question(self, question: str):
        if len(question) < 1:
            raise ValueError("Question property of Question must have a length of at least 1.")
        self._question = question

    # mutator for answers property of Question
    def set_answers(self, answers: list):
        if len(answers) < 1:
            raise ValueError("There must be at least 1 item in the Answer property of Question.")
        self._answers = answers

    # mutator for solution property of Question
    def set_solution(self, solution: int):
        answers = self.get_answers()
        if solution < 0 or solution >= len(answers):
            raise ValueError("Solution property of Question must be within indices of Answers property of Question.")
        self._solution = solution
