from user import User


class MailList():

    def __init__(self, list_id, name):
        self.list_id = list_id
        self.name = name
        self.users = []

    def get_name(self):
        return self.name

    def add_user(self, userName, userEmail):
        newUser = User(userName, userEmail)
        self.users.append(newUser)

    def print_user(self):
        res = []
        indx = 1
        for item in self.users:
            res.append('[{0}] {1} - {2}'.format(indx, item.name, item.email))
            indx += 1
        return '\n'.join(res)

    def search_email(self, email):
        for item in self.users:
            if email == item.email:
                return True
        return False

    def search_name(self, name):
        for item in self.users:
            if name == item.name:
                return True
        return False
