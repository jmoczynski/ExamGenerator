import unittest

from ORQuestion import ORQuestion


class MyTestCase(unittest.TestCase):

    def test_constructors_and_accessors(self):
        testQ1 = ORQuestion()
        self.assertIsNone(testQ1.get_number())
        self.assertIsNone(testQ1.get_question())
        self.assertIsNone(testQ1.get_suggested_solution())

        testQ2Number = 1
        testQ2Question = "What is the question?"
        testQ2Solution = "Suggested solution."
        testQ2 = ORQuestion(testQ2Number, testQ2Question, testQ2Solution)
        self.assertEqual(testQ2Number, testQ2.get_number())
        self.assertEqual(testQ2Question, testQ2.get_question())
        self.assertEqual(testQ2Solution, testQ2.get_suggested_solution())

    def test_mutators(self):

        testQ1 = ORQuestion()

        testNumber1_1 = -10
        testNumber1_2 = -1
        testNumber1_3 = 0
        testNumber1_4 = 1
        testNumber1_5 = 10
        self.assertThrows(ValueError, testQ1.set_number, testNumber1_1)
        self.assertThrows(ValueError, testQ1.set_number, testNumber1_2)
        self.assertThrows(ValueError, testQ1.set_number, testNumber1_3)
        testQ1.set_number(testNumber1_4)
        self.assertEqual(testNumber1_4, testQ1.get_number())
        testQ1.set_number(testNumber1_5)
        self.assertEqual(testNumber1_5, testQ1.get_number())

        testQuestion1_1 = ""
        testQuestion1_2 = "What is the question?"
        self.assertThrows(ValueError, testQ1.set_question, testQuestion1_1)
        testQ1.set_question(testQuestion1_2)
        self.assertEqual(testQuestion1_2, testQ1.get_question())

        testSolution1_1 = ""
        testSolution1_2 = "Suggested solution."
        self.assertThrows(ValueError, testQ1.set_suggested_solution, testSolution1_1)
        testQ1.set_question(testSolution1_2)
        self.assertEqual(testSolution1_2, testQ1.get_suggested_solution())


if __name__ == '__main__':
    unittest.main()
