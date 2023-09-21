from Application.Controller.DBController import DBController


class EditQuestionController:

    def __init__(self, db_controller: DBController):
        self.current_question = None
        self.questions = {}
        self._db_controller = db_controller

    def get_questions(self):
        questions_list = self._db_controller.get_questions()
        if questions_list is not None:
            for q in questions_list:
                print(q)
                self.questions[q[0]] = q[1]
            return self.questions
        else:
            return {}

    def get_question(self):
        pass