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
            print(users)
        self.users = users
        self.id = self.users.keys()
        # Hodily by se ti tu dvě metody, jedna která načte data ze souboru a druhá,
        # která bude ukládat.
        # Osobně bych zrušil self.users, udržovat to synchronizavné s tím co je v
        # souboru je zbytečná komplikace.
        # V metodá bys potom vlastně měla
        # users = self.load()
        # ...
        # a když bys potom potřebovala uložit, tak
        # self.save(users)

    def exists_user(self, username):
        """Control if user exists."""
        if username in self.users:
            return True

    def add_user(self, username, password):
        """Add new user to the dictionary."""
        if self.exists_user(username) is not True:
            self.users[username] = {"username": username, "password": password}
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)

    def remove_user(self, username):
        """Remove user from the dictionary."""
        if self.exists_user(username):
            self.users.pop(username)
            data = self.users
            with open("UsersDatabase.json", "w", encoding='utf=8') as outfile:
                json.dump(data, outfile)

    def generate_password(self, password):
        """Create hashed password."""
        return generate_password_hash(password, method='sha256')

    def check_password(self, username, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    # Mělo by se kontrolovat heslo konkrétního uživatele. Takže ta metoda bude
    # potřebovat i username uživatel jehož heslo se kontroluje. To si (zahashované)
    # načte a zkontroluje pomocí check_password_hash

    def get_by_id(self, username):
        """Return username as user id."""
        if self.exists_user(username):
            print(self.users[username])
