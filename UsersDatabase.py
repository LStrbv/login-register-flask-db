"""Import json and flash."""
import json
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, username, password, picture):
        self.username = username
        self.password = password 
        self.picture = picture
    def to_dict(self):
        return {"username": self.username, "password": self.password, "picture": self.picture}

    def check_password(self, password):
        """Check hashed password."""

        return check_password_hash(self.password, password)

    def get_id(self):
        return self.username



class UsersDatabase():
    """Modify users database."""

    def __init__(self):
        """Modify users database from json to python dictionary."""
        self.file_name = 'UsersDatabase.json'

    def load(self):
        with open(self.file_name, encoding='utf=8') as json_string:
            users = json.load(json_string)
            new_dict = dict()
            for username, user in users.items():
                new_dict[user['username']] = User(user['username'], user['password'], user['picture'])
            return new_dict

    def save(self, users):
        json_dict = dict()
        for username, user in users.items():
            json_dict[username] = user.to_dict()
        with open(self.file_name, "w", encoding='utf=8') as outfile:
            json.dump(json_dict, outfile)

    def add_user(self, username, password, picture):
        """Add new user to the dictionary."""
        if not self.get_by_id(username):
            users = self.load()
            users[username] = User(username, self.generate_password(password), picture)
            self.save(users)
            return users[username]

    def remove_user(self, username):
        """Remove user from the dictionary."""
        if self.get_by_id(username):
            users = self.load()
            users.pop(username)
            self.save(users)

    def generate_password(self, password):
        """Create hashed password."""
        return generate_password_hash(password, method='sha256')

    def get_by_id(self, username):
        """Return username as user id."""
        users = self.load()
        try:
            return users[username]
        except KeyError:
            return None


