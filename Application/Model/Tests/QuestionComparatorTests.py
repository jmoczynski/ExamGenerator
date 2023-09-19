import unittest

from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion
from Application.Model.QuestionComparator import QuestionComparator


class QuestionComparatorTests(unittest.TestCase):
    def test_constructors_and_accessors(self):
        testQ1_question = "What is the question?"
        testQ1_answers = ["A", "B", "C"]
        testQ1_solutions = [0]
        testQ1 = MCQuestion(question=testQ1_question, answers=testQ1_answers, solutions=testQ1_solutions)

        testQ2_question = "What is the question 2?"
        testQ2_answers = ["A", "B", "C"]
        testQ2_solutions = [1]
        testQ2 = MCQuestion(question=testQ2_question, answers=testQ2_answers, solutions=testQ2_solutions)

        testQ3_question = "What is the question?"
        testQ3_solution = "Solution 2"
        testQ3 = ORQuestion(question=testQ3_question, suggested_solution=testQ3_solution)

        testQ4_question = "What is the question?"
        testQ4_solution = "Solution"
        testQ4 = ORQuestion(question=testQ4_question, suggested_solution=testQ4_solution)

        testQC1 = QuestionComparator(testQ1, testQ2)
        self.assertEqual(testQ1,testQC1.get_q1())
        self.assertEqual(testQ2,testQC1.get_q2())
        testQC2 = QuestionComparator(testQ3, testQ4)
        self.assertEqual(testQ3,testQC2.get_q1())
        self.assertEqual(testQ4,testQC2.get_q2())
        testQC3 = QuestionComparator(testQ1, testQ3)
        self.assertEqual(testQ1,testQC3.get_q1())
        self.assertEqual(testQ3,testQC3.get_q2())
        testQC4 = QuestionComparator(testQ4, testQ2)
        self.assertEqual(testQ4,testQC4.get_q1())
        self.assertEqual(testQ2,testQC4.get_q2())

    def test_mutators(self):
        testQ1_question = "What is the question?"
        testQ1_answers = ["A", "B", "C"]
        testQ1_solutions = [0]
        testQ1 = MCQuestion(question=testQ1_question, answers=testQ1_answers, solutions=testQ1_solutions)

        testQ2_question = "What is the question 2?"
        testQ2_answers = ["A", "B", "C"]
        testQ2_solutions = [1]
        testQ2 = MCQuestion(question=testQ2_question, answers=testQ2_answers, solutions=testQ2_solutions)

        testQ3_question = "What is the question?"
        testQ3_solution = "Solution 2"
        testQ3 = ORQuestion(question=testQ3_question, suggested_solution=testQ3_solution)

        testQ4_question = "What is the question?"
        testQ4_solution = "Solution"
        testQ4 = ORQuestion(question=testQ4_question, suggested_solution=testQ4_solution)

        testQC1 = QuestionComparator(testQ1, testQ2)
        testQC1.set_q1(testQ4)
        self.assertEqual(testQ4, testQC1.get_q1())
        testQC1.set_q2(testQ3)
        self.assertEqual(testQ3, testQC1.get_q2())

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

        self.assertNotEqual(QuestionComparator(testQ1, testQ2).compare_questions(), 0)
        self.assertNotEqual(QuestionComparator(testQ1, testQ3).compare_questions(), 0)
        self.assertNotEqual(QuestionComparator(testQ1, testQ4).compare_questions(), 0)
        self.assertNotEqual(QuestionComparator(testQ2, testQ3).compare_questions(), 0)
        self.assertNotEqual(QuestionComparator(testQ2, testQ4).compare_questions(), 0)
        self.assertEqual(QuestionComparator(testQ3, testQ4).compare_questions(), 0)

        self.assertNotEqual(QuestionComparator(testQ1, testQ5).compare_questions(), 0)
        self.assertNotEqual(QuestionComparator(testQ5, testQ6).compare_questions(), 0)
        self.assertNotEqual(QuestionComparator(testQ6, testQ7).compare_questions(), 0)
        self.assertEqual(QuestionComparator(testQ5, testQ7).compare_questions(), 0)

        self.assertEqual(QuestionComparator(testQ1, testQ1).compare_questions(), 0)
        self.assertEqual(QuestionComparator(testQ5, testQ5).compare_questions(), 0)

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

        self.assertFalse(QuestionComparator(testQ1, testQ2).same_question())
        self.assertFalse(QuestionComparator(testQ1, testQ3).same_question())
        self.assertFalse(QuestionComparator(testQ1, testQ4).same_question())
        self.assertFalse(QuestionComparator(testQ2, testQ3).same_question())
        self.assertFalse(QuestionComparator(testQ2, testQ4).same_question())
        self.assertTrue(QuestionComparator(testQ3, testQ4).same_question())

        self.assertFalse(QuestionComparator(testQ5, testQ6).same_question())
        self.assertFalse(QuestionComparator(testQ6, testQ7).same_question())
        self.assertTrue(QuestionComparator(testQ5, testQ7).same_question())

        self.assertTrue(QuestionComparator(testQ1, testQ1).same_question())
        self.assertTrue(QuestionComparator(testQ5, testQ5).same_question())

if __name__ == "__main__":
    unittest.main()