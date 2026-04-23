import csv
import os

file_name = "assets/users.csv"
header = ["id", "name", "role", "status"]

data = []
for i in range(1, 51):
    data.append([i, f"User_{i}", "Developer", "Active"])

if os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    print("CSV file created successfully")
else:
    print("File not found!")
