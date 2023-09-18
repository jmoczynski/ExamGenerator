import unittest
from MCQuestion import MCQuestion

class QuestionTests(unittest.TestCase):

    def test_constructors_and_accessors(self):
        testQ1 = MCQuestion()
        self.assertEqual(testQ1.get_question(), "Question?")
        self.assertEqual(testQ1.get_answers(), None)
        self.assertEqual(testQ1.get_solutions(), None)

        testQuestion2 = "What is the question?"
        testAList2 = ["A", "B", "C", "D"]
        testQ2 = MCQuestion(testQuestion2, testAList2, testAList2[0])
        self.assertEqual(testQ2.get_question(), testQuestion2)
        self.assertEqual(testQ2.get_answers(), testAList2)
        self.assertEqual(testQ2.get_solutions(), testAList2[0])

    def test_mutators(self):
        testQ1 = MCQuestion()
        testQuestion1_1 = ""
        testQuestion1_2 = "What is the question?"
        self.assertRaises(ValueError, testQ1.set_question, testQuestion1_1)
        testQ1.set_question(testQuestion1_2)
        self.assertEqual(testQ1.get_question(), testQuestion1_2)
        testAList1_1 = []
        testAList1_2 = ["A", "B", "C", "D"]
        self.assertRaises(ValueError, testQ1.set_answers, testAList1_1)
        testQ1.set_answers(testAList1_2)
        self.assertEqual(testQ1.get_question(), testQuestion1_2)
        self.assertEqual(testQ1.get_answers(), testAList1_2)
        testSolution1_1= {-10}
        testSolution1_2 = {-1}
        testSolution1_3 = {0}
        testSolution1_4 = {1}
        testSolution1_5 = {3}
        testSolution1_6 = {4}
        testSolution1_7 = {10}
        testSolution1_8 = {}
        testSolution1_9 = {0, 1, 2, 3, 4}
        testSolution1_10 = {0, 1, 2, 3}
        self.assertRaises(ValueError, testQ1.set_solutions, testSolution1_1)
        self.assertRaises(ValueError, testQ1.set_solutions, testSolution1_2)
        self.assertRaises(ValueError, testQ1.set_solutions, testSolution1_6)
        self.assertRaises(ValueError, testQ1.set_solutions, testSolution1_7)
        self.assertRaises(ValueError, testQ1.set_solutions, testSolution1_8)
        self.assertRaises(ValueError, testQ1.set_solutions, testSolution1_9)
        testQ1.set_solutions(testSolution1_3)
        self.assertEqual(testQ1.get_question(), testQuestion1_2)
        self.assertEqual(testQ1.get_answers(), testAList1_2)
        self.assertEqual(testQ1.get_solutions(), testSolution1_3)
        testQ1.set_solutions(testSolution1_4)
        self.assertEqual(testQ1.get_solutions(), testSolution1_4)
        testQ1.set_solutions(testSolution1_5)
        self.assertEqual(testQ1.get_solutions(), testSolution1_5)
        testQ1.set_solutions(testSolution1_10)
        self.assertEquals(testQ1.get_solutions(), testSolution1_10)


if __name__ == '__main__':
    unittest.main()
