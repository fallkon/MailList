from mailList import MailList


class MailListFactory():
    """docstring for MailListFactory"""
    def __init__(self):
        self.current_id = 1

    def next_id(self):
        current_id_ = self.current_id
        self.current_id += 1
        return current_id_

    def create(self, name):
        return MailList(self.next_id(), name)
