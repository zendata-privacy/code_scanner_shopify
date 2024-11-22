import requests
import sqlite3
import logging
import csv


def send_data_to_google_analytics(user_id, email, transaction_id, amount):
    url = "https://www.google-analytics.com/collect"
    payload = {
        "v": "1",  # API Version
        "tid": "UA-12345678-1",  # Tracking ID
        "cid": user_id,  # Client ID
        "t": "event",  # Event type
        "ec": "purchase",  # Event category
        "ea": "transaction",  # Event action
        "el": email,  # Email (Sensitive PII)
        "ev": amount,  # Event value (amount spent)
        "ti": transaction_id  # Transaction ID
    }
    response = requests.post(url, data=payload)
    return response.status_code

# Example usage
send_data_to_google_analytics(
    user_id="user123",
    email="john.doe@example.com",
    transaction_id="TXN456789",
    amount=99.99
)


def store_sensitive_info(name, email, credit_card, ssn):
    connection = sqlite3.connect("sensitive_data.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            email TEXT,
            credit_card TEXT,
            ssn TEXT
        )
    """)
    cursor.execute("INSERT INTO users (name, email, credit_card, ssn) VALUES (?, ?, ?, ?)", 
                   (name, email, credit_card, ssn))
    connection.commit()
    connection.close()

store_sensitive_info(
    name="John Doe",
    email="john.doe@example.com",
    credit_card="4111111111111111",  
    ssn="123-45-6789" 
)


logging.basicConfig(filename='app_debug.log', level=logging.DEBUG)

def log_sensitive_info(user_id, email, ssn):
    logging.debug(f"Debug Info - User ID: {user_id}, Email: {email}, SSN: {ssn}")

log_sensitive_info(
    user_id="user123",
    email="john.doe@example.com",
    ssn="123-45-6789"
)

def retrieve_user_data(api_key, user_id):
    url = f"https://api.example.com/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve user data"}

# Example usage
user_data = retrieve_user_data(api_key="dummy_api_key_123", user_id="user123")
print(user_data)


def read_sensitive_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


sensitive_data = read_sensitive_data("users.csv")
for data in sensitive_data:
    print(data)


def fetch_sensitive_info():
    connection = sqlite3.connect("sensitive_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name, email, credit_card, ssn FROM users")
    results = cursor.fetchall()
    connection.close()
    return results

# Example usage
user_info = fetch_sensitive_info()
for user in user_info:
    print(f"Name: {user[0]}, Email: {user[1]}, Credit Card: {user[2]}, SSN: {user[3]}")
