from user import User

class MailList():

	def __init__(self, name,id_list):
		self.name = name
		self.id = id_list
		self.users = []

	def getName(self):
		return self.name

	def getId(self):
		return self.id


	def addUser(self, userName, userEmail):
		newUser = User(userName, userEmail)
		self.users.append(newUser)

	def printUser(self):
		result = []
		index = 1
		for item in self.users:
			result.append('[{0}]  {1} - {2}'.format(index, item.name, item.email))
			index += 1
		return '\n'.join(result)

	def searchEmail(self, email):
		for item in self.users:
			if email == item.email:
				return True
			return False

    def search_name(self, name):
        for item in self.users:
            if name == item.name:
                return True
        return False
