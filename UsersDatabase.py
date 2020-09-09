"""Import json and flash."""
import json
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash


class UsersDatabase:
    """Modify users database."""

    def __init__(self):
        """Modify users database from json to python dictionary."""
        with open('UsersDatabase.json', encoding='utf=8') as json_string:
            users = json.load(json_string)
        self.users = users

    def exists_user(self, username):
        """Control if user exists."""
        users_name = self.users.keys()
        if username in users_name:
            return username
        else:
            flash('Uživatel neexistuje.')

    def add_user(self, username, password):
        """Add new user to the dictionary."""
        self.username = username
        self.password = password
        if (self.username, self.password not in self.users.items()):
            self.users.update({self.username: generate_password_hash(self.password)})
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)

    def remove_user(self, username):
        """Remove user from the dictionary."""
        self.username = username
        if (self.username in self.users.keys()):
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
        self.password = password
        if self.password in self.users.values():
            check_password_hash(self.password, password)

    def users_list(self):
        """Return list of users names."""
        users_list = []
        for names in self.users.keys():
            users_list.append(names)
        users_string = [str(element) for element in users_list]
        joined_string_users = ", ".join(users_string)
        return joined_string_users

    def get_id(self, username):
        """Return username as user id."""
        self.username = username
        if (self.username in self.users.keys()):
            return self.username
     
    def is_active(self):
        return True

# user = UsersDatabase()
