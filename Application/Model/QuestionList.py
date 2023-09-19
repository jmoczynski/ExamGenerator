from Application.Model.Question import Question
from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion

class QuestionList:

    def __init__(self, name: str, questions: list[Question]):
        if len(name) < 1:
            raise ValueError("Name property of QuestionList must not be empty.")
        if len(questions) < 1:
            raise ValueError("Question List property of QuestionList must not be empty.")
        self._name = name
        self._question_list = questions

    def get_question_list(self):
        return self._question_list

    def set_question_list(self, questions: list[Question]):
        if len(questions) < 1:
            raise ValueError("Question List property of QuestionList must not be empty.")
        self._question_list = questions

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        if len(name) < 1:
            raise ValueError("Name property of QuestionList must not be empty.")
        self._name = name

    def add_question(self, question: Question):
        pass

    def modify_question(self, index: int):
        pass

    def _modify_MCQuestion(self, question: MCQuestion):
        pass

    def _modify_ORQuestion(self, question: ORQuestion):
        pass

    def delete_question(self, index: int):
        pass

    def randomize_questions(self):
        pass