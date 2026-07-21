import sqlite3
import os
Use the 'subprocess' module with caution and consider using a safer alternative like 'shutil' or 'pathlib' for file operations.
from typing import List, Tuple, Optional

# Read secrets from environment variables
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")


class UserService:
    """
    User service with security, performance,
    bug fixes, and improved code quality.
    """

    def __init__(self, db_path: str = "users.db"):
        # Database connection injected/configurable
        self.conn = sqlite3.connect(db_path)
        self.age: Optional[int] = None

    # Fixed: Parameterized query (prevents SQL injection)
    def get_user(self, username: str) -> List[Tuple]:
        query = "SELECT * FROM users WHERE username = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (username,))
        return cursor.fetchall()

    # Fixed: Division-by-zero validation
    def calculate_average(self, total: float, count: int) -> float:
        if count <= 0:
            raise ValueError("Count must be greater than zero.")
        return total / count

    # Removed duplicate logic
    def _calculate_reward(self, salary: float) -> float:
        return salary * 0.10 if salary > 50000 else salary * 0.05

    def calculate_bonus(self, salary: float) -> float:
        return self._calculate_reward(salary)

    def calculate_incentive(self, salary: float) -> float:
        return self._calculate_reward(salary)

    # Fixed: Prevent command injection
    def ping_server(self, host: str) -> None:
        subprocess.run(
            ["ping", host],
            check=False,
            shell=False
        )

    # Fixed: Input validation
    def update_user_age(self, age: int) -> None:
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")

        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")

        self.age = age

    # Fixed: Execute query only once
    def get_all_users(self) -> List[Tuple]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    def close(self) -> None:
        self.conn.close()


if __name__ == "__main__":
    service = UserService()

    try:
        print(service.get_user("admin"))

        print(service.calculate_average(100, 5))

        service.ping_server("google.com")

        service.update_user_age(25)

        print(service.get_all_users())

    finally:
        service.close()
