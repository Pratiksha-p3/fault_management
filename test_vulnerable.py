import os
import sqlite3
import hashlib
import secrets
import tempfile
import requests
import yaml
import bcrypt
from pathlib import Path


# Environment Variables
API_KEY = os.getenv("API_KEY")
JWT_SECRET = os.getenv("JWT_SECRET")
DB_PASSWORD = os.getenv("DB_PASSWORD")


class UserService:

    def __init__(self):
        self.conn = sqlite3.connect("users.db")

    # Safe SQL Query
    def get_user(self, username):
        query = "SELECT * FROM users WHERE username = ?"
        cursor = self.conn.execute(query, (username,))
        return cursor.fetchall()

    # Safe Delete
    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = ?"
        self.conn.execute(query, (user_id,))
        self.conn.commit()

    # Safe Ping
    def ping_host(self, host):
        import subprocess

        result = subprocess.run(
            ["ping", host],
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout

    # Restricted Commands
    def run_command(self, command):
        allowed_commands = ["ls", "dir"]

        if command not in allowed_commands:
            raise ValueError("Command not allowed")

        return os.popen(command).read()

    # Strong Password Hashing
    def hash_password(self, password):
        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

    # Secure Token Generation
    def generate_token(self):
        return secrets.token_hex(32)

    # Safe Calculator
    def calculate(self, a, b):
        return a + b

    # Disabled Dangerous Execution
    def execute_python(self, code):
        raise NotImplementedError(
            "Dynamic code execution is disabled"
        )

    # Safe YAML Loader
    def load_yaml(self, file_path):
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    # Prevent Path Traversal
    def read_file(self, filename):
        base_dir = Path("./data").resolve()

        file_path = (base_dir / filename).resolve()

        if not str(file_path).startswith(str(base_dir)):
            raise ValueError("Invalid file path")

        return file_path.read_text()

    # Prevent Arbitrary File Writes
    def write_file(self, filename, content):
        base_dir = Path("./data").resolve()

        file_path = (base_dir / filename).resolve()

        if not str(file_path).startswith(str(base_dir)):
            raise ValueError("Invalid file path")

        file_path.write_text(content)

    # Secure Token
    def get_token(self):
        return secrets.token_hex(32)

    # No Environment Exposure
    def dump_env(self):
        return {
            "APP_MODE": os.getenv("APP_MODE", "production")
        }

    # No Secret Disclosure
    def get_database_password(self):
        return "Access Restricted"

    # Secure Temporary File
    def create_temp_file(self):
        fd, path = tempfile.mkstemp()
        os.close(fd)
        return path

    # SSRF Protection
    def fetch_url(self, url):
        allowed_domains = [
            "api.github.com",
            "example.com"
        ]

        from urllib.parse import urlparse

        domain = urlparse(url).hostname

        if domain not in allowed_domains:
            raise ValueError("URL not allowed")

        return requests.get(
            url,
            timeout=5
        ).text

    # Secure OTP
    def generate_otp(self):
        return secrets.randbelow(900000) + 100000

    # Proper Authentication
    def login(self, username, password):
        user = self.get_user(username)

        if not user:
            return False

        stored_hash = user[0][2]

        return bcrypt.checkpw(
            password.encode(),
            stored_hash.encode()
        )

    # Safe Update Query
    def update_profile(self, user_input, user_id):
        query = """
            UPDATE users
            SET profile = ?
            WHERE id = ?
        """

        self.conn.execute(
            query,
            (user_input, user_id)
        )

        self.conn.commit()

    # Safe Logging
    def log_user(self, username):
        print(f"User Login: {username}")

    # Open Redirect Protection
    def redirect_user(self, url):
        allowed_domains = [
            "example.com"
        ]

        from urllib.parse import urlparse

        domain = urlparse(url).hostname

        if domain not in allowed_domains:
            raise ValueError("Invalid redirect")

        return f"Redirecting to {url}"

    # Secure Session ID
    def create_session(self):
        return secrets.token_urlsafe(32)

    # Disabled Arbitrary Execution
    def run_script(self, script):
        raise NotImplementedError(
            "Script execution disabled"
        )

    # Remove Hardcoded Credentials
    def admin_login(self, username, password):
        return self.login(username, password)
