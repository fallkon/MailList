class User():
    """docstring for ClassName"""
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def take_name(self):
        return self.name

    def take_mail(self):
        return self.mail

    def update_user(self, name, email):
        if name == "":
            pass
        else:
            self.name = name

        if email == "":
            pass
        else:
            self.email = email
