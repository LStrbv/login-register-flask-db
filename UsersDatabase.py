"""Import json and flash."""
import json
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash


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
            return True
        else:
            flash('Uživatel neexistuje.')

    def add_user(self):
        """Add new user to the dictionary."""
        if (self.username, self.password not in self.users.items()):
            self.users.update({self.username: generate_password_hash(self.password)})
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

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
        return self.password

    def check_password(self, password):
        """Check hashed password."""
        if self.password in self.users.values():
            return check_password_hash(self.password, password)
            

    def users_list(self):
        """Return list of users names."""
        users_list = []
        for names in self.users.keys():
            users_list.append(names)
        users_string = [str(element) for element in users_list]
        joined_string_users = ", ".join(users_string)
        return joined_string_users

""" user = UsersDatabase('LStrbv', 'banan')
user.exists_user()
user.users_list()
user.set_password('banan')
user.check_password('banan') """
