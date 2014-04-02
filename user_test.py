import user
import unittest


class UserTest(unittest.TestCase):
    def setUp(self):
        name = 'Ivan Ivanov'
        email = 'ivan@gmail.com'
        self.user = user.User(name, email)

    def test_get_name(self):
        self.assertEqual('Ivan Ivanov', self.user.take_name())

    def test_get_email(self):
        self.assertEqual('ivan@gmail.com', self.user.take_email())

    def test_update_user_name_changed(self):
        self.user.update_user("Ivan Ivanov", "ivan@gmail.com")
        exp_1 = "Ivan Ivanov"
        exp_2 = "ivan@gmail.com"

        self.assertEqual(exp_1, self.user.take_name())
        self.assertEqual(exp_2, self.user.take_email())

if __name__ == '__main__':
    unittest.main()
