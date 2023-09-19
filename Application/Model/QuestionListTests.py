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
        self.assertTrue(False)

    def test_modify_question(self):
        self.assertTrue(False)

    def test_delete_question(self):
        self.assertTrue(False)

    def test_randomize_questions(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
