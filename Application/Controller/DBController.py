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
                   'answer text NOT NULL,'
                   'question_id INTEGER NOT NULL,'
                   'FOREIGN KEY(question_id) REFERENCES Question(id)'
                   ');')
        self._db_con.execute(command)
        command = ('CREATE TABLE IF NOT EXISTS MCQuestionSolution('
                   'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                   'mcquestionanswer_id INTEGER NOT NULL,'
                   'question_id INTEGER NOT NULL,'
                   'FOREIGN KEY(question_id) REFERENCES Question(id), '
                   'FOREIGN KEY(mcquestionanswer_id) REFERENCES MCQuestionAnswer(id)'
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