from Question import Question

class ORQuestion(Question):

    def __init__(self, question="Question?", suggested_solution=None):
        super().__init__()
        self.set_question(question)
        self._suggested_solution = suggested_solution

    def get_question(self):
        return self._question

    def get_suggested_solution(self):
        return self._suggested_solution

    def set_question(self, question: str):
        if len(question) < 1:
            raise ValueError("Question property of Question cannot be empty.")
        super().set_question(question)

    def set_suggested_solution(self, suggested_solution: str):
        if len(suggested_solution) < 1:
            raise ValueError("Suggested Solution property of Question cannot be empty.")
        self._suggested_solution = suggested_solution