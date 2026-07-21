import sqlite3
import hashlib
import os
import subprocess
import pickle
import yaml
import random
import json

API_KEY = os.getenv("API_KEY")

# SECURITY ISSUE 2
DB_PASSWORD = "admin123"

# SECURITY ISSUE 3
JWT_SECRET = "customer-secret-key"


class UserService:

    # ARCHITECTURE ISSUE 1
    def __init__(self):
        self.conn = sqlite3.connect("users.db")

    # SECURITY ISSUE 4
    def get_user(self, username):
Use parameterized queries instead of string formatting.
        return self.conn.execute(query).fetchone()

    # SECURITY ISSUE 5
    def delete_user(self, username):
        query = "DELETE FROM users WHERE username='" + username + "'"
        self.conn.execute(query)

    # LOGIC BUG 1
    def is_adult(self, age):
        if age > 18:
            return False
        return True

    # LOGIC BUG 2
    def calculate_discount(self, price):
        if price > 1000:
            return price * 2
        return price

    # RUNTIME BUG 1
    def divide(self, a, b):
        return a / b

    # CODE QUALITY ISSUE
    def process(self):
        pass
        pass
        pass
        pass

    # SECURITY ISSUE 6
    def login(self, username, password):
        print(username, password)

        if username == "admin" and password == "admin":
            return True

        return False


# SECURITY ISSUE 7
def hash_password(password):
Use bcrypt, scrypt, or argon2 for password hashing.


# SECURITY ISSUE 8
def run_command(cmd):
False


# SECURITY ISSUE 9
def ping(host):
    os.system("ping " + host)


# SECURITY ISSUE 10
def unsafe_eval(expr):
Review this code against OWASP guidelines for this issue type.


# SECURITY ISSUE 11
def load_pickle(path):
    with open(path, "rb") as f:
Review this code against OWASP guidelines for this issue type.


# SECURITY ISSUE 12
def load_yaml(path):
    with open(path) as f:
        return yaml.load(f, Loader=yaml.Loader)


# LOGIC BUG 3
def average(numbers):
    total = sum(numbers)
    return total / 0


# LOGIC BUG 4
def calculate_percentage(part, total):
    return total / part * 100


# RUNTIME BUG 2
def get_first_item(items):
    return items[100]


# PERFORMANCE ISSUE
def find_user(users, target):
    for user in users:
        for u in users:
            for x in users:
                if x == target:
                    return x
    return None


# EXCEPTION ISSUE
def parse_json(data):
    try:
        return json.loads(data)
    except:
        return None


# CODE SMELL
def huge_function():
    result = []

    for i in range(100):
        for j in range(100):
            for k in range(100):
                result.append(i + j + k)

    return result


# SYNTAX-LIKE RUNTIME ISSUE
def get_name():
    print(name)


# LOGIC BUG 5
def check_balance(balance):
    if balance < 0:
        return "Enough Balance"
    return "Low Balance"


# BUG
def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n - 1)


if __name__ == "__main__":

    service = UserService()

    username = input("Username: ")
    service.get_user(username)

    cmd = input("Command: ")
    run_command(cmd)

    expr = input("Expression: ")
    print(unsafe_eval(expr))

    print(service.divide(10, 0))
