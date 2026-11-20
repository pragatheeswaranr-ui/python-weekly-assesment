
import csv
import json
import requests
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("API_KEY")

# Read employee data
employees = []

with open("../data/employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(line for line in file if line.strip())

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

print("Rows read:", len(employees))

# Save employee data as JSON
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

# Find high earners
high_earners = []

for employee in employees:
    if employee["salary"] > 50000:
        high_earners.append(employee)

print("High earners:", len(high_earners))

# Save high earners in CSV
with open("high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

# Get users from API
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    for user in users[:3]:
        print(user["id"], "-", user["name"], "-", user["email"])

    # Read nested JSON field
    user_details = []

    for user in users:
        user_details.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "company": user.get("company", {}).get("name")
        })

    # Save users in JSON
    with open("users.json", "w") as file:
        json.dump(user_details, file, indent=4)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

# Check 404 error
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet")
