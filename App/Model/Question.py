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
        return None

    # accessor for question property of Question
    def get_question(self):
        return None

    # accessor for answers property of Question
    def get_answers(self):
        return None

    # accessor for solution property of Question
    def get_solution(self):
        return None

    # mutator for number property of Question
    def set_number(self, number: int):
        pass

    # mutator for question property of Question
    def set_question(self, question: str):
        pass

    # mutator for answers property of Question
    def set_answers(self, answers: list):
        pass


    # mutator for solution property of Question
    def set_solution(self, solution: int):
        pass

