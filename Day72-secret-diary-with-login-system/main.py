import datetime
import hashlib
import os
import random
import time

from replit import db

key_prefix_entry = "entry_"


def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[key_prefix_entry + str(timestamp)] = entry


def viewEntry():
  keys = db.prefix(key_prefix_entry)
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key[len(key_prefix_entry):]}
  {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if (opt.lower()[0] == "e"):
      break

def setPassword():
  username = input("Username: > ")
  password = input("Password: > ")
  salt = str(random.randint(1000, 9999))
  hashed_password = hash_password(password, salt)
  db[username] = {"password": hashed_password, "salt": salt}
  db["password_set"] = True
  print("\nDetails stored.\n")

def hash_password(password, salt):
  return hashlib.sha256(f"{password}{salt}".encode()).hexdigest()


try:
  db["password_set"]
except KeyError:
  print("\nNo account found. Please create one.\n")
  setPassword()

print("\nLogin to proceed.\n")
username = input("Username: > ")
password = input("Password: > ")
salt = db[username]["salt"]
hashed_password = hash_password(password, salt)
if hashed_password == db[username]["password"]:
  print("\nLogin successful!\n")
else:
  print("\nLogin failed.\n")
  exit()

time.sleep(1)
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
