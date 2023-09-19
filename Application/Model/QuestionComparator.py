import collections

from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion
from Application.Model.Question import Question


class QuestionComparator:

    def __init__(self, q1: Question, q2: Question):
        self.q1 = q1
        self.q2 = q2

    def compare_questions(self):
        if self.q1.__class__ != self.q2.__class__:
            return -4
        if self.q1.__class__ == MCQuestion:
            if self.q1.get_question() != self.q2.get_question():
                return -3
            if collections.Counter(self.q1.get_answers()) != collections.Counter(self.q2.get_answers()):
                return -2
            if collections.Counter(self.q1.get_solutions()) != collections.Counter(self.q2.get_solutions()):
                return -1
            return 0

        if self.q1.__class__ == ORQuestion:
            if self.q1.get_question() != self.q2.get_question():
                return -2
            if self.q1.get_suggested_solution() != self.q2.get_suggested_solution():
                return -1
            return 0


    def same_question(self):
        if self.q1.__class__ != self.q2.__class__:
            return False
        if self.q1.__class__ == MCQuestion:
            if self.q1.get_question() != self.q2.get_question():
                return False
            if collections.Counter(self.q1.get_answers()) != collections.Counter(self.q2.get_answers()):
                return False
            if collections.Counter(self.q1.get_solutions()) != collections.Counter(self.q2.get_solutions()):
                return False
            return True

        if self.q1.__class__ == ORQuestion:
            if self.q1.get_question() != self.q2.get_question():
                return False
            if self.q1.get_suggested_solution() != self.q2.get_suggested_solution():
                return False
            return True