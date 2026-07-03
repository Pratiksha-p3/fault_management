import sqlite3
import os

# SECURITY ISSUE: Hardcoded secret
API_KEY = "super_secret_api_key_123"

# SECURITY ISSUE: Hardcoded password
DB_PASSWORD = "admin123"


class UserService:

    # ARCHITECTURE ISSUE:
    # Database connection created directly inside service
    def __init__(self):
        self.conn = sqlite3.connect("users.db")

    # SQL Injection Vulnerability
    def get_user(self, username):
        query = f"SELECT * FROM users WHERE username='{username}'"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    # Bug: division by zero possible
    def calculate_average(self, total, count):
        return total / count

    # Code Quality Issue: duplicate logic
    def calculate_bonus(self, salary):
        if salary > 50000:
            return salary * 0.10
        else:
            return salary * 0.05

    def calculate_incentive(self, salary):
        if salary > 50000:
            return salary * 0.10
        else:
            return salary * 0.05

    # Security Issue: command injection
    def ping_server(self, host):
        os.system("ping " + host)

    # Bug: no validation
    def update_user_age(self, age):
        self.age = age

    # Performance Issue
    def get_all_users(self):
        users = []
        cursor = self.conn.cursor()

        for i in range(1000):
            cursor.execute("SELECT * FROM users")
            users.extend(cursor.fetchall())

        return users


if __name__ == "__main__":
    service = UserService()

    print(service.get_user("admin"))

    print(service.calculate_average(100, 0))

    service.ping_server("google.com")

    print(service.get_all_users())
