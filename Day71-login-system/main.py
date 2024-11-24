import hashlib
import random

from replit import db


def show_menu():
  print("🌟 Login System 🌟")
  print()
  print("1. Add User, 2. Login")
  print()


def get_menu_input():
  while True:
    try:
      menu_input = int(input("Input > "))
      if menu_input in [1, 2]:
        return menu_input
      else:
        print("Invalid input. Please enter 1 or 2.")
    except ValueError:
      print("Invalid input. Please enter 1 or 2.")


def hash_password(password, salt):
  return hashlib.sha256(f"{password}{salt}".encode()).hexdigest()


while True:
  show_menu()
  menu_input = get_menu_input()
  if menu_input == 1:
    username = input("Username: > ")
    password = input("Password: > ")
    salt = str(random.randint(1000, 9999))
    hashed_password = hash_password(password, salt)
    db[username] = {"password": hashed_password, "salt": salt}
    print("\nDetails stored.\n")
  elif menu_input == 2:
    username = input("Username: > ")
    password = input("Password: > ")
    salt = db[username]["salt"]
    hashed_password = hash_password(password, salt)
    if hashed_password == db[username]["password"]:
      print("\nLogin successful!\n")
    else:
      print("\nLogin failed.\n")
