import unittest
from mail_list_factory import MailListFactory


class TestMailListFactory(unittest.TestCase):

    def setUp(self):
        self.maillist_factory = MailListFactory()

    def test_next_id(self):
        self.assertEqual(1, self.maillist_factory.next_id())
        self.assertEqual(2, self.maillist_factory.current_id)

    def test_create(self):
        maillist = self.maillist_factory.create("hack")
        self.assertEqual(1, maillist.list_id)
        self.assertEqual("hack", maillist.name)

if __name__ == '__main__':
    unittest.main()
