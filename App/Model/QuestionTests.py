import unittest
from Question import Question

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


if __name__ == '__main__':
    unittest.main()
