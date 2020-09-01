"""Import json and flash."""
import json
from flask import flash


class UsersDatabase:
    """Modify users database."""

    def __init__(self, username, password):
        """Modify users database from json to python dictionary."""
        with open('UsersDatabase.json', encoding='utf=8') as json_string:
            users = json.load(json_string)
        self.users = users
        self.username = username
        self.password = password

    def exists_user(self):
        """Control if user exists."""
        users_name = self.users.keys()
        if self.username in users_name:
            return self.username
    """  else:
            flash('Uživatel neexistuje')
    """
    def add_user(self):
        """Add new user to the dictionary."""
        if (self.username, self.password not in self.users.items()):
            self.users.update({self.username: self.password})
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)

    def remove_user(self):
        """Remove user from the dictionary."""
        if (self.username, self.password in self.users.items()):
            self.users.pop(self.username)
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)


""" user = UsersDatabase('JKrn', 'mandarinka')
user.exists_user()
user.add_user()
user.remove_user()
 """