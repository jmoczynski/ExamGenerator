from Application.View.App import App
from Application.Model.TestSuite import run_test_suite


def view_tests():
    result = run_test_suite()
    if result:
        view = App()
        view.view()
    exit(1)


if __name__ == "__main__":
    view_tests()
