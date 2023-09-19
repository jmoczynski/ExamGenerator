import collections
import unittest

from Application.Model.MCQuestion import MCQuestion
from Application.Model.ORQuestion import ORQuestion
from Application.Model.QuestionList import QuestionList


class QuestionListTests(unittest.TestCase):
    def test_constructors_and_accessors(self):
        testQList1_name = "test1"
        testQList1_questions = []
        self.assertRaises(ValueError, QuestionList, "", testQList1_questions)
        self.assertRaises(ValueError, QuestionList, testQList1_name, [])

        testQList2_name = "test2"
        testQList2_questions_question = MCQuestion("question", ["a", "b", "c"], [1])
        testQList2_questions = [testQList2_questions_question]
        testQList2 = QuestionList(testQList2_name, testQList2_questions)
        self.assertEqual(testQList2.get_name(), testQList2_name)
        self.assertEqual(testQList2.get_question_list(), testQList2_questions)

    def test_mutators(self):
        testQList1_name = "test1"
        testQList1_questions_question = MCQuestion("question", ["a", "b", "c"], [1])
        testQList1_questions = [testQList1_questions_question]
        testQList1 = QuestionList(testQList1_name, testQList1_questions)
        self.assertRaises(ValueError, testQList1.set_name, "")
        self.assertRaises(ValueError, testQList1.set_question_list, [])
        testQList1_name2 = "test2"
        testQList1.set_name(testQList1_name2)
        self.assertEqual(testQList1.get_name(), testQList1_name2)
        testQList1_questions_question1 = MCQuestion("question", ["a", "b", "c"], [1])
        testQList1_questions_question2 = ORQuestion("question", "solution")
        testQList1_questions = [testQList1_questions_question1, testQList1_questions_question2]
        testQList1.set_question_list(testQList1_questions)
        self.assertEqual(testQList1.get_question_list(), testQList1_questions)

    def test_add_question(self):
        testQList2_name = "test2"
        testQList2_questions_question1 = MCQuestion("question", ["a", "b", "c"], [1])
        testQList2_questions_question2 = MCQuestion("question", ["a", "b", "c"], [1])
        testQList2_questions_question3 = MCQuestion("question", ["a", "b", "c", "d"], [1])
        testQList2_questions_question4 = MCQuestion("question", ["a", "b", "c"], [1, 2])
        testQList2_questions = [testQList2_questions_question1]
        testQList2 = QuestionList(testQList2_name, testQList2_questions)
        self.assertRaises(ValueError, testQList2.add_question, testQList2_questions_question1)
        self.assertRaises(ValueError, testQList2.add_question, testQList2_questions_question2)
        testQList2.add_question(testQList2_questions_question3)
        self.assertEqual(collections.Counter([testQList2_questions_question1, testQList2_questions_question3]), collections.Counter(testQList2.get_question_list()))
        testQList2.add_question(testQList2_questions_question4)
        self.assertEqual(collections.Counter([testQList2_questions_question1, testQList2_questions_question3, testQList2_questions_question4]), collections.Counter(testQList2.get_question_list()))

    def test_delete_question(self):
        testQList2_name = "test2"
        testQList2_questions_question1 = MCQuestion("question", ["a", "b", "c"], [1])
        testQList2_questions_question3 = MCQuestion("question", ["a", "b", "c", "d"], [1])
        testQList2_questions_question4 = MCQuestion("question", ["a", "b", "c"], [1, 2])
        testQList2_questions = [testQList2_questions_question1, testQList2_questions_question3, testQList2_questions_question4]
        testQList2 = QuestionList(testQList2_name, testQList2_questions)
        self.assertRaises(ValueError, testQList2.delete_question, -10)
        self.assertRaises(ValueError, testQList2.delete_question, -1)
        self.assertRaises(ValueError, testQList2.delete_question, 3)
        self.assertRaises(ValueError, testQList2.delete_question, 10)
        testQList2.delete_question(0)
        self.assertEqual(collections.Counter(testQList2.get_question_list()), collections.Counter([testQList2_questions_question3, testQList2_questions_question4]))
        testQList2.delete_question(1)
        self.assertEqual(collections.Counter(testQList2.get_question_list()), collections.Counter([testQList2_questions_question3]))
        self.assertRaises(ValueError, testQList2.delete_question, 0)

    def test_randomize_questions(self):
        testQList2_name = "test2"
        testQList2_questions_question1 = MCQuestion("question", ["a", "b", "c"], [1])
        testQList2_questions_question3 = MCQuestion("question", ["a", "b", "c", "d"], [1])
        testQList2_questions_question4 = MCQuestion("question", ["a", "b", "c"], [1, 2])
        testQList2_questions = [testQList2_questions_question1, testQList2_questions_question3, testQList2_questions_question4]
        testQList2 = QuestionList(testQList2_name, testQList2_questions)
        testQList2.randomize_questions()
        print(testQList2.get_question_list().__repr__())
        self.assertEqual(collections.Counter(testQList2.get_question_list()), collections.Counter(testQList2.get_question_list()))
        testQList2.randomize_questions()
        print(testQList2.get_question_list().__repr__())
        self.assertEqual(collections.Counter(testQList2.get_question_list()), collections.Counter(testQList2.get_question_list()))
        testQList2.randomize_questions()
        print(testQList2.get_question_list().__repr__())
        self.assertEqual(collections.Counter(testQList2.get_question_list()), collections.Counter(testQList2.get_question_list()))
        testQList2.randomize_questions()
        print(testQList2.get_question_list().__repr__())
        self.assertEqual(collections.Counter(testQList2.get_question_list()), collections.Counter(testQList2.get_question_list()))


if __name__ == '__main__':
    unittest.main()
