from Application.Controller.DBController import DBController
from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion


class NewQuestionController:

    def __init__(self, db_controller: DBController):
        self._question_type_selection = 0
        self.db_controller = db_controller

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
        try:
            question_obj = MCQuestion(question, answers, solutions)
            result = self.db_controller.create_mc_question(question, answers, solutions)
            if not result:
                raise Exception("Error in creating question.")
            return question_obj
        except (Exception):
            return None

    def create_or_question(self, question: str, solution: str):
        try:
            question_obj = ORQuestion(question, solution)
            result = self.db_controller.create_or_question(question, solution)
            if not result:
                raise Exception("Error in creating question.")
            return question_obj
        except (Exception):
            return None

    def create_or_question(self, question: str, suggested_solution: str):
        pass