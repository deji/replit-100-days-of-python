"""
data structures:
- a kV store where the key is the username and it's value is the type of user
- a secret store where the key is PASSWORD_<username> and it's value is the password

logic - log in:
- check if the username exists in the kV store
- if it does, get the kind of user it is
- check if the password matches that stored in secret PASSWORD_<username>
- if it does, log in and output message depending on user type
"""

import os
import sys
from replit import db


def load_users():
    db["USERNAME_deji"] = "admin"
    db["USERNAME_jason"] = "normal"


def login(username, password):

    if f"USERNAME_{username}" not in db:
        return "User not found"

    if password != os.environ['PASSWORD_' + username]:
        return "Wrong password"

    user_type = "admin" if db[f"USERNAME_{username}"].lower(
    ) == "admin" else "normie"
    return f"Welcome {username}! You are a {user_type}"


load_users()

print("🌟 Login System 🌟")
print()
username = input("Username > ")
password = input("Password > ")
print()

result = login(username, password)
print(result)
