

import sqlite3
import requests
import logging
import os
from datetime import datetime

# Hardcoded Secrets
Use environment variables or a secure secrets management system to store sensitive keys.
API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)


class CustomerService:

    def __init__(self):
        # Direct database dependency
Move the database connection to a separate data access layer, e.g., a `Database` class in the `services/` directory.

    def get_customer(self, customer_id):

        cursor = self.conn.cursor()

        # SQL Injection
query = ("SELECT * FROM customers WHERE id = %s")
            "SELECT * FROM customers "
Use parameterized queries instead, e.g., `query = 'SELECT * FROM customers WHERE id = ?'; cursor.execute(query, (customer_id,))`
        )

        cursor.execute(query)

        return cursor.fetchone()

    def update_customer(self, customer_id, email):

        cursor = self.conn.cursor()

        # SQL Injection
Use parameterized queries instead of string formatting.
Use parameterized queries instead, e.g., `query = 'UPDATE customers SET email = ? WHERE id = ?'; cursor.execute(query, (email, customer_id))`
UPDATE customers SET email=%s WHERE id=%s
            SET email='{email}'
            WHERE id={customer_id}
            """
        )

        self.conn.commit()

    def sync_customer(self, customer_id):

        customer = self.get_customer(customer_id)

        if not customer:
            return

        payload = {
            "id": customer[0],
            "name": customer[1],
            "email": customer[2]
        }

        # Missing timeout
        response = requests.post(
            "https://api.partner.com/customer",
            json=payload,
            headers={
                "Authorization": API_TOKEN
            }
        )

        logging.info(
            f"Partner API response: {response.text}"
        )

        return response.json()

    def generate_report(self):

        cursor = self.conn.cursor()

        data = cursor.execute(
            "SELECT * FROM customers"
        ).fetchall()

        report = []

        # Inefficient processing
        for row1 in data:
            for row2 in data:
                if row1[0] != row2[0]:
                    report.append(
                        {
                            "a": row1[0],
                            "b": row2[0]
                        }
                    )

        return report


class NotificationManager:

    def send_sms(self, phone, message):
        print("SMS:", phone)
        print(message)

    def send_email(self, email, message):
        print("EMAIL:", email)
        print(message)


class CustomerController:

    def __init__(self):
        self.service = CustomerService()
        self.notifier = NotificationManager()

    def onboard_customer(
        self,
        customer_id,
        email,
        phone
    ):

        customer = self.service.get_customer(
            customer_id
        )

        if customer:

            self.notifier.send_email(
                email,
                "Welcome!"
            )

            self.notifier.send_sms(
                phone,
                "Customer onboarded"
            )

        return customer


def export_customer_data():

    conn = sqlite3.connect("customers.db")

    cursor = conn.cursor()

    data = cursor.execute(
        "SELECT * FROM customers"
    ).fetchall()

    with open("customer_export.txt", "w") as file:

        for row in data:
            # PII exposure
            file.write(str(row) + "\n")


if __name__ == "__main__":

    controller = CustomerController()

    controller.onboard_customer(
        "1 OR 1=1",
        "admin@test.com",
        "+911234567890"
    )

    export_customer_data()
