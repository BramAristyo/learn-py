import csv
import os

file_name = "assets/users.csv"
if os.path.exists(file_name):
    with open("assets/users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"ID: {row['id']} | Name: {row['name']} | Role: {row['role']}")
