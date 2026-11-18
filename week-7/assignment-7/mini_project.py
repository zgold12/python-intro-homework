import os
import csv
from datetime import datetime
now = datetime.now()

if os.path.exists("week-7/data/expenses.csv"):
    print("expenses.csv found.")
    with open("week-7/data/expenses.csv", "r") as file:
        records = list(csv.DictReader(file))
        for item in records:
            item["amount"] = float(item["amount"])
        food_items = [item for item in records if item["category"] == "Food"]
        total_value = sum(item["amount"] for item in food_items)
    with open("week-7/assignment-7/food_report.txt", "w") as file:
        file.write(f"\nFood Expense Report — generated {now.strftime("%B %d, %Y")}")
        for row in food_items:
           file.write(f"\n{row["date"]}: ${row["amount"]}")
        file.write(f"\nTotal: ${total_value:.2f}")
else:
    print("expenses.csv not found.")
    
