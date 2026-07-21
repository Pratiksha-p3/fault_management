# syntax_runtime_errors.py

import os
import sqlite3

API_KEY = "secret-key"

# Syntax Error 1
def get_user(name)
    print(name)


# Syntax Error 2
def calculate(a, b):
    if a > b
        return a
    else:
        return b


# Syntax Error 3
for i in range(10)
    print(i)


# Runtime Error 1
def divide(a, b):
    return a / b


# Runtime Error 2
def get_item():
    data = [1, 2, 3]
    return data[10]


# Runtime Error 3
def print_name():
    print(username)


# Logic Error 1
def is_adult(age):
    if age >= 18:
        return False
    return True


# Logic Error 2
def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n - 1)


# SQL Injection
def get_user_db(username):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{username}'"
    return conn.execute(query)


# Command Injection
def run_command(cmd):
    os.system(cmd)


# Syntax Error 4
class UserService

    def __init__(self):
        self.name = "admin"


# Syntax Error 5
try:
    print("hello")
except
    print("error")


# Runtime Error 4
def read_file():
    with open("missing.txt") as f:
        return f.read()


if __name__ == "__main__":

    print(divide(10, 0))

    print(get_item())

    print_name()

    read_file()
