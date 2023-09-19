from Application.Model.Question import Question
from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion
from Application.Model.QuestionComparator import QuestionComparator


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
        for Q in self.get_question_list():
            comparator = QuestionComparator(Q, question)
            if comparator.same_question():
                raise ValueError("Cannot add a question to the QuestionList multiple times.")
        self._question_list.append(question)

    def modify_question(self, index: int):
        pass

    def _modify_MCQuestion(self, question: MCQuestion):
        pass

    def _modify_ORQuestion(self, question: ORQuestion):
        pass

    def delete_question(self, index: int):
        if index >= len(self.get_question_list()) or index < 0:
            raise ValueError("Cannot delete question from outside of QuestionList index range.")
        if len(self.get_question_list()) == 1:
            raise ValueError("Cannot delete the 1 remaining question from QuestionList.")
        self._question_list.pop(index)

    def randomize_questions(self):
        pass