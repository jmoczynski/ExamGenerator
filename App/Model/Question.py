class Question:

    def __init__(self, question=None):
        self._question = question

    def get_question(self):
        return self._question

    def set_question(self, question: str):
        if len(question) < 1:
            raise ValueError("Question property of Question cannot be empty.")
        self._question = question