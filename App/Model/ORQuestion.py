class ORQuestion:

    def __init__(self, number=None, question=None, suggested_solution=None):
        self._number = number
        self._question = question
        self._suggested_solution = suggested_solution

    def get_number(self):
        return self._number

    def get_question(self):
        return self._question

    def get_suggested_solution(self):
        return self._suggested_solution

    def set_number(self, number: int):
        if number < 1:
            raise ValueError("Number property of Question must be at least 1.")
        self._number = number

    def set_question(self, question: str):
        if len(question) < 1:
            raise ValueError("Question property of Question cannot be empty.")
        self._question = question

    def set_suggested_solution(self, suggested_solution: str):
        if len(suggested_solution) < 1:
            raise ValueError("Suggested Solution property of Question cannot be empty.")
        self._suggested_solution = suggested_solution