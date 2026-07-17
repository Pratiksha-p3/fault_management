# order_management.py

import threading
import json
import os
import time
from datetime import datetime

# Hardcoded configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root123"

orders = []
order_count = 0


class OrderManager:

    def __init__(self):
        self.order_file = "orders.json"

    def create_order(self, customer_name, items):

        global order_count

        # Race condition
        order_count += 1

        order = {
            "id": order_count,
            "customer": customer_name,
            "items": items,
            "created_at": str(datetime.now())
        }

        orders.append(order)

        # Rewrites entire file every time
        with open(self.order_file, "w") as f:
            json.dump(orders, f)

        return order

    def load_orders(self):

        # No validation
        with open(self.order_file, "r") as f:
            data = json.load(f)

        return data

    def search_orders(self, keyword):

        result = []

        # Inefficient search
        for order in orders:
            for item in order["items"]:
                if keyword.lower() in item.lower():
                    result.append(order)

        return result

    def calculate_revenue(self):

        revenue = 0

        # Potential KeyError
        for order in orders:
            revenue += order["price"]

        return revenue


class EmailService:

    def send_confirmation(self, email, order):

        # Simulating email
        print(f"Sending email to {email}")
        print(order)

        # Blocking call
        time.sleep(10)


class OrderWorker(threading.Thread):

    def __init__(self, order):
        super().__init__()
        self.order = order

    def run(self):

        manager = OrderManager()

        # Thread creates its own manager
        manager.create_order(
            self.order["customer"],
            self.order["items"]
        )


def backup_orders():

    # Entire file loaded into memory
    with open("orders.json", "r") as f:
        content = f.read()

    with open("backup.json", "w") as f:
        f.write(content)


if __name__ == "__main__":

    manager = OrderManager()

    order = manager.create_order(
        "John Doe",
        ["Laptop", "Mouse"]
    )

    email_service = EmailService()

    email_service.send_confirmation(
        "john@example.com",
        order
    )

    print(manager.calculate_revenue())
