"""from user import User"""

class MailList():

	def __init__(self, name):
		self.name = name
		self.users = []

	def getName(self):
		return self.name


	def addUser(self, userName, userEmail):
		newUser = User(userName, userEmail)
		self.users.append(newUser)

	def printUser(self):
		res = []
		indx = 1
		for item in self.users:
			res.append('[{0}]  {1} - {2}'.format(indx, item.name, item.email))
			indx += 1
		return '\n'.join(res)

	def searchEmail(self, email):
		for item in self.users:
			if email == item.email:
				return True
			return False