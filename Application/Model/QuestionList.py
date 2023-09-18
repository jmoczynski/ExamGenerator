from Application.Model.Question import Question
from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion

class QuestionList:

    def __init__(self, name: str, questions: list[Question]):
        self._name = name
        self._question_list = questions

    def get_question_list(self):
        pass

    def set_question_list(self, questions: list[Question]):
        pass

    def get_name(self):
        pass

    def set_name(self, name: str):
        pass

    def add_question(self, question: Question):
        pass

    def modify_question(self, question: Question):
        pass

    def _modify_MCQuestion(self, question: MCQuestion):
        pass

    def _modify_ORQuestion(self, question: ORQuestion):
        pass