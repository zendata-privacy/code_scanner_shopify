import requests
import pandas as pd
import sqlite3
import logging
import csv

logging.basicConfig(level=logging.INFO)

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    logging.info(f"User name: {user}")
    logging.info(f"User email: {email}")
    response = requests.post("https://useractivitytracking.com", json=data)
    return response.status_code, response.json()

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    response = requests.post("https://googleadstrack.com", json=data)
    return response.status_code, response.json()

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    response = requests.post("https://sellyourusersdata.com", json=data)
    return response.status_code, response.json()

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    response = requests.post("https://activitytrack.com", json=data)
    return response.status_code, response.json()

##

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    response = requests.post("https://useractivitytracking.com", json=data)
    return response.status_code, response.json()

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    response = requests.post("https://googleadstrack.com", json=data)
    return response.status_code, response.json()

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    response = requests.post("https://sellyourusersdata.com", json=data)
    return response.status_code, response.json()

def send_user_info_to_url(user, email, url):
    ""
    data = {'name': user, 'email': email}
    logging.info(f"User name: {user}")
    logging.info(f"User email: {email}")
    response = requests.post("https://activitytrack.com", json=data)
    return response.status_code, response.json()
#

def consume_user_info_from_url(url):
    response = requests.get(url)
    user_info = response.json()  # Example of using user_info
    name, email = user_info.get('name'), user_info.get('email')
    return response.status_code, name, email

def consume_user_info_from_database(db_path, query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    user_info = cursor.fetchall()
    email = user_info[0] if user_info else None
    conn.close()
    return email

def consume_user_info_from_csv(file_path):
    user_info_df = pd.read_csv(file_path)  # Example of using user_info
    name, email, adress, phone_number = user_info_df['name'], user_info_df['email'], user_info_df['adress'], user_info_df['phone_number']
    return name, email, adress, phone_number

def send_user_info_to_database(db_path, user, email, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} (name, email) VALUES (?, ?)", (user, email))
    conn.commit()
    conn.close()

def log_user_leaving(email, transaction):
    logging.info(f"User left: Email: {email}, Transaction: {transaction}")
    

def send_user_info_to_csv(user, email, file_path):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user, email])

def check_user_info(user, email):
    # Placeholder for internal processing, such as validation or transformation
    if user and email:
        return True
    
import requests

url = 'http://127.0.0.1:5000/predict'
files = {'image': open('image.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())  # Prints the predicted class


from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI

# Initialize the LLM
llm = OpenAI(model="gpt-3.5-turbo")

# Custom summary function
def summarize_text(text):
    response = llm.run(f"Please summarize the following text: {text}")
    return response

# Define the agent with custom functionality
tools = [
    {"name": "Summarizer", "description": "Summarizes provided text.", "func": summarize_text}
]

agent = initialize_agent(llm, tools, AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# Call the agent with text to summarize
text_to_summarize = "Large language models (LLMs) are a type of artificial intelligence that..."
summary_response = agent.run(f"Summarize this: {text_to_summarize}")
print("Summary Response:", summary_response)

