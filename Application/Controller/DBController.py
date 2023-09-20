import sqlite3
import os

class DBController:

    def __init__(self):
        self._db_con = sqlite3.connect(os.path.abspath("../data/db/data.db"))
        command = ('CREATE TABLE IF NOT EXISTS Question('
                   'id INTEGER NOT NULL PRIMARY KEY,'
                   'question_text TEXT NOT NULL'
                   ');')
        self._db_con.execute(command)
        command = ('CREATE TABLE IF NOT EXISTS MCQuestionAnswer('
                   'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                   'answer_text TEXT NOT NULL,'
                   'question_id INTEGER NOT NULL,'
                   'FOREIGN KEY(question_id) REFERENCES Question(id)'
                   ');')
        self._db_con.execute(command)
        command = ('CREATE TABLE IF NOT EXISTS MCQuestionSolution('
                   'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                   'mcquestion_answer_id INTEGER NOT NULL,'
                   'question_id INTEGER NOT NULL,'
                   'FOREIGN KEY(question_id) REFERENCES Question(id), '
                   'FOREIGN KEY(mcquestion_answer_id) REFERENCES MCQuestionAnswer(id)'
                   ');')
        self._db_con.execute(command)
        command = ('CREATE TABLE IF NOT EXISTS ORQuestion('
                   'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                   'question_id INTEGER NOT NULL,'
                   'suggested_solution text NOT NULL,'
                   'FOREIGN KEY(question_id) REFERENCES Question(id)'
                   ');')
        self._db_con.execute(command)
        command = ('CREATE TABLE IF NOT EXISTS QuestionList('
                   'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                   'list_name TEXT NOT NULL'
                   ');')
        self._db_con.execute(command)
        command = ('CREATE TABLE IF NOT EXISTS QuestionsToQuestionList('
                   'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                   'question_id INTEGER NOT NULL,'
                   'questionlist_id INTEGER NOT NULL,'
                   'FOREIGN KEY (question_id) REFERENCES Question(id),'
                   'FOREIGN KEY (questionlist_id) REFERENCES QuestionList(id)'
                   ');')
        self._db_con.execute(command)
        self._db_con.commit()

    def close(self):
        self._db_con.close()

    def create_mc_question(self, question: str, answers: list[str], solutions: list[int]):
        try:
            cursor = self._db_con.cursor()
            command = """INSERT INTO Question(question_text) VALUES(?);"""
            cursor.execute(command, (question))
            self._db_con.commit()

            question_id = None
            questions = cursor.execute("SELECT * FROM Question;").fetchall()
            for q in questions:
                if q[1] == question:
                    question_id = q[0]
                    break

            if question_id is None:
                raise Exception("Error in retrieving question.")

            for a in answers:
                command = """INSERT INTO MCQuestionAnswer(answer_text, question_id) VALUES (?,?);"""
                cursor.execute(command, (a, question_id))
            self._db_con.commit()

            answer_ids = []
            answers = cursor.execute("SELECT * FROM MCQuestionAnswer;").fetchall()
            for a in answers:
                if a[1] == question:
                    answer_ids.append(a[0])
                    break

            for s in solutions:
                command = """INSERT INTO MCQuestionSolution(mcquestion_answer_id, question_id) VALUES (?,?);"""
                cursor.execute(command, (s, question_id))
            self._db_con.commit()

            return True

        except (Exception):
            return False

    def create_or_question(self, question: str, solution: str):
        cursor = self._db_con.cursor()
        try:
            command = """INSERT INTO Question(question_text) VALUES(?);"""
            cursor.execute(command, (question))
            self._db_con.commit()

            question_id = None
            questions = cursor.execute("SELECT * FROM Question;").fetchall()
            for q in questions:
                if q[1] == question:
                    question_id = q[0]
                    break
            command = """INSERT INTO ORQuestion(question_id, suggested_solution) VALUES(?, ?);"""
            cursor.execute(command, (question_id, solution))

            return True
        except(Exception):
            return False