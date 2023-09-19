import unittest

from Application.Model.ORQuestion import ORQuestion


class ORQuestionsTests(unittest.TestCase):

    def test_constructors_and_accessors(self):
        testQ1 = ORQuestion()
        self.assertEqual(testQ1.get_question(), "Question?")
        self.assertIsNone(testQ1.get_suggested_solution())

        testQ2Question = "What is the question?"
        testQ2Solution = "Suggested solution."
        testQ2 = ORQuestion(testQ2Question, testQ2Solution)
        self.assertEqual(testQ2Question, testQ2.get_question())
        self.assertEqual(testQ2Solution, testQ2.get_suggested_solution())

    def test_mutators(self):

        testQ1 = ORQuestion()

        testQuestion1_1 = ""
        testQuestion1_2 = "What is the question?"
        self.assertRaises(ValueError, testQ1.set_question, testQuestion1_1)
        testQ1.set_question(testQuestion1_2)
        self.assertEqual(testQuestion1_2, testQ1.get_question())

        testSolution1_1 = ""
        testSolution1_2 = "Suggested solution."
        self.assertRaises(ValueError, testQ1.set_suggested_solution, testSolution1_1)
        testQ1.set_suggested_solution(testSolution1_2)
        self.assertEqual(testSolution1_2, testQ1.get_suggested_solution())


if __name__ == '__main__':
    unittest.main()
