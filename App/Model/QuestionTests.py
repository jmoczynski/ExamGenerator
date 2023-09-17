import unittest
from Question import Question

class QuestionTests(unittest.TestCase):

    def test_constructors_and_accessors(self):
        testQ1 = Question()
        self.assertEqual(testQ1.get_number(), None)
        self.assertEqual(testQ1.get_question(), None)
        self.assertEqual(testQ1.get_answers(), None)
        self.assertEqual(testQ1.get_solution(), None)

        testQuestion2 = "What is the question?"
        testAList2 = ["A", "B", "C", "D"]
        testQ2 = Question(1, testQuestion2, testAList2, testAList2[0])
        self.assertEqual(testQ2.get_number(), 1)
        self.assertEqual(testQ2.get_question(), testQuestion2)
        self.assertEqual(testQ2.get_answers(), testAList2)
        self.assertEqual(testQ2.get_solution(), testAList2[0])

if __name__ == '__main__':
    unittest.main()
