"""Import json and flash."""
import json
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class UsersDatabase(UserMixin):
    """Modify users database."""

    def __init__(self):
        """Modify users database from json to python dictionary."""
        with open('UsersDatabase.json', encoding='utf=8') as json_string:
            users = json.load(json_string)
        self.users = users
        self.id = self.users.keys()

    def exists_user(self, username):
        """Control if user exists."""
        users_name = self.users.keys()
        if username in users_name:
            return True
    

    def add_user(self, username, password):
        """Add new user to the dictionary."""

        if (username, password not in self.users.items()):
            self.users.update({self.username: generate_password_hash(password)})
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)

    def remove_user(self, username):
        """Remove user from the dictionary."""
        
        if (self.username in self.users.keys()):
            self.users.pop(self.username)
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)

    def generate_password(self, password):
        """Create hashed password."""
        return generate_password_hash(password, method='sha256')
        

    def check_password(self, username, password):
        """Check hashed password."""
        if (username, password in self.users.items()):
            check_password_hash(self.password, password)

    def users_list(self):
        """Return list of users names."""
        users_list = []
        for names in self.users.keys():
            users_list.append(names)
        users_string = [str(element) for element in users_list]
        joined_string_users = ", ".join(users_string)
        return joined_string_users

    
# user = UsersDatabase()
