import json
import os
from maillist import MailList
from maillist_factory import MailListFactory

def show_list(lists, id_list):
    for list in lists:
        if list.get_id() == id_list:
            return list.print_()
    return False


def show_lists(lists):
    result = []
    for list in lists:
        result.append('[{0}] - {1}'.format(list.get_id(), list.get_name()))
    result = sorted(result)
    return '\n'.join(result)


def create_new_list(lists, creating_new, new_list):
    lists.append(creating_new.create(new_list))
    print('New list <{0}> was created!'.format(new_list))


def add_new_user(lists, id_list, name, email):
    for i in range(len(lists)):
        if lists[i].get_id() == list_id:
            lists[i].add_user(name, email)
            return True
    print('List with unique identifier {} was not found!'.format(id_list))
    return False


def search_email(lists, list_id, email):
    for item in lists:
        if list_id == item.list_id:
            item.search_email(email)
