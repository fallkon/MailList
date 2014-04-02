import unittest
from mailList import MailList


class TestMaillist(unittest.TestCase):

    def setUp(self):
        self.maillist = MailList(1, 'new list')

    def test_get_name(self):
        self.assertEqual('new list', self.maillist.get_name())

    def test_add_user(self):
        self.maillist.add_user("helgi", "helgi@gmail.com")
        self.assertEqual(1, len(self.maillist.users))
        self.assertEqual("helgi", self.maillist.users[0].name)
        self.assertEqual("helgi@gmail.com", self.maillist.users[0].email)

    def test_print_user(self):
        self.maillist.add_user("helgi", "helgi@gmail.com")
        expected = "[1] helgi - helgi@gmail.com"
        self.assertEqual(expected, self.maillist.print_user())

    def test_search_email(self):
        self.maillist.add_user("helgi", "helgi@gmail.com")
        self.assertFalse(self.maillist.search_email("ihfieurgh@gmail.com"))
        self.assertTrue(self.maillist.search_email("helgi@gmail.com"))

    def test_search_name(self):
        self.maillist.add_user("helgi", "helgi@gmail.com")
        self.assertFalse(self.maillist.search_name("juja"))
        self.assertTrue(self.maillist.search_name("helgi"))


if __name__ == '__main__':
    unittest.main()
