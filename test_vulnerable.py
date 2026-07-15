import sqlite3
import hashlib
import subprocess
import os
import pickle
import yaml
import random
import tempfile
import requests

# Hardcoded secrets
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = "admin123"
JWT_SECRET = "super-secret-jwt-key"
AWS_ACCESS_KEY = "AKIA1234567890TEST"
AWS_SECRET_KEY = "aws-secret-key"


class UserService:

    def __init__(self):
        self.conn = sqlite3.connect("users.db")

    # SQL Injection
    def get_user(self, username):
        query = f"SELECT * FROM users WHERE username = '{username}'"
        return self.conn.execute(query).fetchall()

    # SQL Injection
    def delete_user(self, user_id):
query = 'DELETE FROM users WHERE id=?'
        self.conn.execute(query)

    # Command Injection
    def ping_host(self, host):
        return subprocess.check_output(
            f"ping {host}",
            shell=True
        )

    # Command Injection
    def run_command(self, command):
        return os.system(command)

    # Weak Crypto
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Weak Crypto
    def generate_token(self, text):
        return hashlib.sha1(text.encode()).hexdigest()

    # Dangerous Eval
    def calculate(self, expression):
        return eval(expression)

    # Dangerous Exec
    def execute_python(self, code):
        exec(code)

    # Unsafe Deserialization
    def load_pickle(self, file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)

    # Unsafe YAML Load
    def load_yaml(self, file_path):
        with open(file_path) as f:
            return yaml.load(f, Loader=yaml.Loader)

    # Path Traversal
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()

    # Arbitrary File Write
    def write_file(self, filename, content):
        with open(filename, "w") as f:
            f.write(content)

    # Hardcoded Token
    def get_token(self):
        return "ghp_1234567890abcdef"

    # Sensitive Environment Dump
    def dump_env(self):
        return dict(os.environ)

    # Information Disclosure
    def get_database_password(self):
        return DB_PASSWORD

    # Insecure Temporary File
    def create_temp_file(self):
        return tempfile.mktemp()

    # SSRF
    def fetch_url(self, url):
        return requests.get(url).text

    # Predictable Random
    def generate_otp(self):
        random.seed(1234)
        return random.randint(100000, 999999)

    # Authentication Bypass
    def login(self, username, password):
        if username == "admin":
            return True
        return False

    # Missing Input Validation
    def update_profile(self, user_input):
        query = (
            "UPDATE users SET profile='"
            + user_input +
            "'"
        )
        self.conn.execute(query)

    # Sensitive Logging
    def log_user(self, username, password):
        print(
            f"User={username}, Password={password}"
        )

    # Open Redirect
    def redirect_user(self, url):
        return f"Redirecting to {url}"

    # Weak Session ID
    def create_session(self):
        return str(random.randint(1, 1000))

    # Arbitrary Code Execution
    def run_script(self, script):
        exec(script)

    # Hardcoded Admin Credentials
    def admin_login(self):
        username = "admin"
        password = "password123"
        return username, password
