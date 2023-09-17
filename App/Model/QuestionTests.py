import unittest
from Question import Question

class QuestionTests(unittest.TestCase):

    def test_constructors_and_accessors(self):
        testQ1 = Question()
        self.assertEqual(testQ1.get_number(), None)
        self.assertEqual(testQ1.get_question(), None)
        self.assertEqual(testQ1.get_answers(), None)
        self.assertEqual(testQ1.get_solution(), None)

        testNumber1 = 1
        testQuestion2 = "What is the question?"
        testAList2 = ["A", "B", "C", "D"]
        testQ2 = Question(testNumber1, testQuestion2, testAList2, testAList2[0])
        self.assertEqual(testQ2.get_number(), testNumber1)
        self.assertEqual(testQ2.get_question(), testQuestion2)
        self.assertEqual(testQ2.get_answers(), testAList2)
        self.assertEqual(testQ2.get_solution(), testAList2[0])

    def test_mutators(self):
        testQ1 = Question()
        testNumber1_1 = -10
        testNumber1_2 = -1
        testNumber1_3 = 0
        testNumber1_4 = 1
        testNumber1_5 = 10
        self.assertRaises(ValueError, testQ1.set_number, testNumber1_1)
        self.assertRaises(ValueError, testQ1.set_number, testNumber1_2)
        self.assertRaises(ValueError, testQ1.set_number, testNumber1_3)
        testQ1.set_number(testNumber1_4)
        self.assertEqual(testQ1.get_number(), testNumber1_4)
        testQ1.set_number(testNumber1_5)
        self.assertEqual(testQ1.get_number(), testNumber1_5)
        testQuestion1_1 = ""
        testQuestion1_2 = "What is the question?"
        self.assertRaises(ValueError, testQ1.set_question, testQuestion1_1)
        testQ1.set_question(testQuestion1_2)
        self.assertEqual(testQ1.get_number(), testNumber1_5)
        self.assertEqual(testQ1.get_question(), testQuestion1_2)
        testAList1_1 = []
        testAList1_2 = ["A", "B", "C", "D"]
        self.assertRaises(ValueError, testQ1.set_answers, testAList1_1)
        testQ1.set_answers(testAList1_2)
        self.assertEqual(testQ1.get_number(), testNumber1_5)
        self.assertEqual(testQ1.get_question(), testQuestion1_2)
        self.assertEqual(testQ1.get_answers(), testAList1_2)
        testSolution1_1= -10
        testSolution1_2 = -1
        testSolution1_3 = 0
        testSolution1_4 = 1
        testSolution1_5 = 3
        testSolution1_6 = 4
        testSolution1_7 = 10
        self.assertRaises(ValueError, testQ1.set_solution, testSolution1_1)
        self.assertRaises(ValueError, testQ1.set_solution, testSolution1_2)
        self.assertRaises(ValueError, testQ1.set_solution, testSolution1_6)
        self.assertRaises(ValueError, testQ1.set_solution, testSolution1_7)
        testQ1.set_solution(testSolution1_3)
        self.assertEqual(testQ1.get_number(), testNumber1_5)
        self.assertEqual(testQ1.get_question(), testQuestion1_2)
        self.assertEqual(testQ1.get_answers(), testAList1_2)
        self.assertEqual(testQ1.get_solution(), testSolution1_3)
        testQ1.set_solution(testSolution1_4)
        self.assertEqual(testQ1.get_solution(), testSolution1_4)
        testQ1.set_solution(testSolution1_5)
        self.assertEqual(testQ1.get_solution(), testSolution1_5)


if __name__ == '__main__':
    unittest.main()
