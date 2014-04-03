#import json
#import os
#from maillist import MailList
#from maillist_factory import MailListFactory


def update_subscriber(lists, list_id, user_id, user_name, user_email):
    for item in lists:
        if list_id == item.list_id:
            item.users[user_id - 1].update_user(user_name, user_email)
            return True
    return False


def remove_subscriber(lists, list_id, user_id):
    for item in lists:
        if list_id == item.list_id:
            item.users = item.users[:user_id - 1] + item.users[user_id:]


def search_email(lists, list_id, email):
    for item in lists:
        if list_id == item.list_id:
            item.search_email(email)
