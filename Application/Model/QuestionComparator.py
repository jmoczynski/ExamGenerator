import collections

from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion
from Application.Model.Question import Question


class QuestionComparator:

    def __init__(self, q1: Question, q2: Question):
        self._q1 = q1
        self._q2 = q2

    def compare_questions(self):
        if self._q1.__class__ != self._q2.__class__:
            return -4
        if self._q1.__class__ == MCQuestion:
            if self._q1.get_question() != self._q2.get_question():
                return -3
            if collections.Counter(self._q1.get_answers()) != collections.Counter(self._q2.get_answers()):
                return -2
            if collections.Counter(self._q1.get_solutions()) != collections.Counter(self._q2.get_solutions()):
                return -1
            return 0

        if self._q1.__class__ == ORQuestion:
            if self._q1.get_question() != self._q2.get_question():
                return -2
            if self._q1.get_suggested_solution() != self._q2.get_suggested_solution():
                return -1
            return 0


    def same_question(self):
        if self._q1.__class__ != self._q2.__class__:
            return False
        if self._q1.__class__ == MCQuestion:
            if self._q1.get_question() != self._q2.get_question():
                return False
            if collections.Counter(self._q1.get_answers()) != collections.Counter(self._q2.get_answers()):
                return False
            if collections.Counter(self._q1.get_solutions()) != collections.Counter(self._q2.get_solutions()):
                return False
            return True

        if self._q1.__class__ == ORQuestion:
            if self._q1.get_question() != self._q2.get_question():
                return False
            if self._q1.get_suggested_solution() != self._q2.get_suggested_solution():
                return False
            return True