class NewQuestionController:

    def __init__(self):
        self._question_type_selection = 0

    def get_question_type_selection(self):
        return self._question_type_selection

    def set_question_type_selection(self, value):
        self._question_type_selection = value

    def selection(self, value):
        self.set_question_type_selection(value)
        print(self.get_question_type_selection())

    def is_valid_question(self, value):
        if len(value) < 1: return False
        return True

    def create_mc_question(self, question: str, answers: list[str], solutions: list[int]):
        pass

    def create_or_question(self, question: str, suggested_solution: str):
        pass