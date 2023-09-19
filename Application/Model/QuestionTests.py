import unittest

from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion
from Question import Question
import Question as q

class QuestionTests(unittest.TestCase):
    def test_constructors_and_accessors(self):
        testQ1 = Question()
        self.assertIsNone(testQ1.get_question())

    def test_mutators(self):
        testQ1 = Question()
        testQuestion1_1 = ""
        testQuestion1_2 = "What is the question?"
        self.assertRaises(ValueError, testQ1.set_question, testQuestion1_1)
        testQ1.set_question(testQuestion1_2)
        self.assertEqual(testQuestion1_2, testQ1.get_question())

    def test_compare_questions(self):
        testQ1_question = "What is the question?"
        testQ1_answers = ["A", "B", "C"]
        testQ1_solutions = [0]
        testQ1 = MCQuestion(question=testQ1_question, answers=testQ1_answers, solutions=testQ1_solutions)

        testQ2_question = "What is the question 2?"
        testQ2_answers = ["A", "B", "C"]
        testQ2_solutions = [1]
        testQ2 = MCQuestion(question=testQ2_question, answers=testQ2_answers, solutions=testQ2_solutions)

        testQ3_question = "What is the question?"
        testQ3_answers = ["A", "B", "C", "D"]
        testQ3_solutions = [0, 1]
        testQ3 = MCQuestion(question=testQ3_question, answers=testQ3_answers, solutions=testQ3_solutions)

        testQ4_question = "What is the question?"
        testQ4_answers = ["A", "B", "C", "D"]
        testQ4_solutions = [0, 1]
        testQ4 = MCQuestion(question=testQ4_question, answers=testQ4_answers, solutions=testQ4_solutions)

        testQ5_question = "What is the question?"
        testQ5_solution = "Solution"
        testQ5 = ORQuestion(question=testQ5_question, suggested_solution=testQ5_solution)

        testQ6_question = "What is the question?"
        testQ6_solution = "Solution 2"
        testQ6 = ORQuestion(question=testQ6_question, suggested_solution=testQ6_solution)

        testQ7_question = "What is the question?"
        testQ7_solution = "Solution"
        testQ7 = ORQuestion(question=testQ7_question, suggested_solution=testQ7_solution)

        self.assertNotEquals(q.compare_questions(testQ1, testQ2), 0)
        self.assertNotEquals(q.compare_questions(testQ1, testQ3), 0)
        self.assertNotEquals(q.compare_questions(testQ1, testQ4), 0)
        self.assertNotEquals(q.compare_questions(testQ2, testQ3), 0)
        self.assertNotEquals(q.compare_questions(testQ2, testQ4), 0)
        self.assertEqual(q.compare_questions(testQ3, testQ4), 0)

        self.assertNotEquals(q.compare_questions(testQ1, testQ5))
        self.assertNotEquals(q.compare_questions(testQ5, testQ6))
        self.assertNotEquals(q.compare_questions(testQ6, testQ7))
        self.assertEqual(q.compare_questions(testQ5, testQ7), 0)

        self.assertEqual(q.compare_questions(testQ1, testQ1), 0)
        self.assertEqual(q.compare_questions(testQ5, testQ5), 0)
    def test_same_question(self):
        testQ1_question = "What is the question?"
        testQ1_answers = ["A", "B", "C"]
        testQ1_solutions = [0]
        testQ1 = MCQuestion(question=testQ1_question, answers=testQ1_answers, solutions=testQ1_solutions)

        testQ2_question = "What is the question 2?"
        testQ2_answers = ["A", "B", "C"]
        testQ2_solutions = [1]
        testQ2 = MCQuestion(question=testQ2_question, answers=testQ2_answers, solutions=testQ2_solutions)

        testQ3_question = "What is the question?"
        testQ3_answers = ["A", "B", "C", "D"]
        testQ3_solutions = [0, 1]
        testQ3 = MCQuestion(question=testQ3_question, answers=testQ3_answers, solutions=testQ3_solutions)

        testQ4_question = "What is the question?"
        testQ4_answers = ["A", "B", "C", "D"]
        testQ4_solutions = [0, 1]
        testQ4 = MCQuestion(question=testQ4_question, answers=testQ4_answers, solutions=testQ4_solutions)

        testQ5_question = "What is the question?"
        testQ5_solution = "Solution"
        testQ5 = ORQuestion(question=testQ5_question, suggested_solution=testQ5_solution)

        testQ6_question = "What is the question?"
        testQ6_solution = "Solution 2"
        testQ6 = ORQuestion(question=testQ6_question, suggested_solution=testQ6_solution)

        testQ7_question = "What is the question?"
        testQ7_solution = "Solution"
        testQ7 = ORQuestion(question=testQ7_question, suggested_solution=testQ7_solution)

        self.assertFalse(q.same_question(testQ1, testQ2))
        self.assertFalse(q.same_question(testQ1, testQ3))
        self.assertFalse(q.same_question(testQ1, testQ4))
        self.assertFalse(q.same_question(testQ2, testQ3))
        self.assertFalse(q.same_question(testQ2, testQ4))
        self.assertTrue(q.same_question(testQ3, testQ4))

        self.assertFalse(q.same_question(testQ5, testQ6))
        self.assertFalse(q.same_question(testQ6, testQ7))
        self.assertTrue(q.same_question(testQ5, testQ7))

        self.assertTrue(q.same_question(testQ1, testQ1))
        self.assertTrue(q.same_question(testQ5, testQ5))

if __name__ == '__main__':
    unittest.main()
