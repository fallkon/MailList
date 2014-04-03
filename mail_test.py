import unittest
import mail
from mail_list_factory import MailListFactory


class TestMail(unittest.TestCase):

    def setUp(self):
        self.list = []
        self.maillist_factory = MailListFactory()
        self.list.append(self.maillist_factory.create("imperatorski"))
        self.list[0].add_user("sar.Peio", "sarpeio@imperia.com")
        self.list[0].add_user("sar.Oleg", "saroleg@imperia.com")

    def test_update_subscriber(self):
        mail.update_subscriber(self.list, 1, 1, "sar.PeioIII", "")
        self.assertEqual("sar.PeioIII", self.list[0].users[0].take_name())
        self.assertEqual("sarpeio@imperia.com", self.list[0].users[0].
                         take_email())

    def test_remove_subscriber(self):
        mail.remove_subscriber(self.list, 1, 1)
        expected = "[1] sar.Oleg - saroleg@imperia.com"
        self.assertEqual(expected, self.list[0].print_user())

    def test_search_email(self):
        mail.search_email(self.list, 1, "sarpeio@imperia")
        self.assertTrue(self.list[0].users[1].take_email())


if __name__ == '__main__':
    unittest.main()
