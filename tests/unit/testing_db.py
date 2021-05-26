from unittest import TestCase
from website.models import db
from website.models import Note, Work ,Team ,User

class Test_database(TestCase):
    def test_note_table(self):
        note = Note(id = 1, data = "Odwa", date = 2020/5/21, user_id = 1)
        self.assertEqual(note.id, 1)
        self.assertEqual(note.data, "Odwa")
        self.assertEqual(note.date, 2020/5/21)
        self.assertEqual(note.user_id, 1)

    def test_work_table(self):
        work = Work(id = 2, title = 'TheDyans', description = 'No_work_no_pay', date = 2020/5/20, user_id = 1,
                    status = "In", points = 100)

        self.assertEqual(work.id, 2)
        self.assertEqual(work.title, 'TheDyans')
        self.assertEqual(work.description, 'No_work_no_pay')
        self.assertEqual(work.date, 2020/5/20)
        self.assertEqual(work.user_id, 1)
        self.assertEqual(work.status, "In")
        self.assertEqual(work.points, 100)

    def test_users_table(self):
        user = User(id = 3, email = "odwa@gmail.com", password = "10111",first_name = "odwa",)

        self.assertEqual(user.id, 3)
        self.assertEqual(user.email, "odwa@gmail.com")
        self.assertEqual(user.password, "10111")
        self.assertEqual(user.first_name, "odwa")

    def test_team_table(self):
        team = Team(id = 1, name = "Mighty")

        self.assertEqual(team.id, 1)
        self.assertEqual(team.name, "Mighty")
