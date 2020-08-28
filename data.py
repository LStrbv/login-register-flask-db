"""Import flask and jason."""
from flask import Flask
import json


class UsersDatabase:
    """Open users database."""

    data = {}

    with open('database.json', encoding='utf=8') as json_string:
        dictionary = json.load(json_string)
        print(dictionary)
