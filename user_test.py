import user
import unittest

class UserTest(unittest.TestCase):
    """docstring for UserTest"""

    def setUp(self):
        self.user = user.User("Ivan Ivanov","ivanivanov@gmail.com")


    def test_init_user(self):
        self.assertTrue(self.user.name is not None)
        self.assertTrue(self.user.mail is not None)

    def test_take_name(self):
        self.assertEqual("Ivan Ivanov", self.user.take_name())

    def test_take_email(self):
        self.assertEqual("ivanivanov@gmail.com", self.user.take_mail())

    def test_update_user_name_changed(self):
        self.user.update_user("Petyr Petrov", "petyrpetrov@gmail.com")
        self.assertEqual("Petyr Petrov", self.user.take_name())
        self.assertEqual("petyrpetrov@gmail.com", self.user.take_mail())

    def test_update_user_name_untouched(self):
        self.user.update_user("", "ivanivanov@gmail.com")
        self.assertEqual("Ivan Ivanov", self.user.take_name())
        self.assertEqual("ivanivanov@gmail.com", self.user.take_mail())
        

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
