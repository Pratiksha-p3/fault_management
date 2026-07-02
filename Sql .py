# vulnerable_sql.py

import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
        AND password = '{password}'
    """

    print("Executing:", query)

    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    return result


if __name__ == "__main__":
    user = input("Username: ")
    pwd = input("Password: ")

    if login(user, pwd):
        print("Login successful")
    else:
        print("Invalid credentials")
