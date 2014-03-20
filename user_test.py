import user
import unittest

class UserTest(unittest.TestCase):
	def setUp(self):
		name = 'Ivan Ivanov'
		email = 'ivan@gmail.com'
		self.user = user.User(name, email)


	def test_get_name(self):
		self.assertEqual('Ivan Ivanov', self.user.get_name())

	def test_get_email(self):
		self.assertEqual('ivan@gmail.com', self.user.get_email())

	