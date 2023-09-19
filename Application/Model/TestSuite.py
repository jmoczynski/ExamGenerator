import unittest

from Application.Model.Tests.MCQuestionTests import MCQuestionTests
from Application.Model.Tests.ORQuestionTests import ORQuestionsTests
from Application.Model.Tests.QuestionComparatorTests import QuestionComparatorTests
from Application.Model.Tests.QuestionListTests import QuestionListTests
from Application.Model.Tests.QuestionTests import QuestionTests

def run_test_suite():

    test_classes = [MCQuestionTests, ORQuestionsTests, QuestionComparatorTests, QuestionListTests, QuestionTests]
    loader = unittest.TestLoader()
    test_list = []
    for c in test_classes:
        suite = loader.loadTestsFromTestCase(c)
        test_list.append(suite)

    suite = unittest.TestSuite(test_list)
    runner = unittest.TextTestRunner()
    results = runner.run(suite)

if __name__ == "__main__":
    run_test_suite()