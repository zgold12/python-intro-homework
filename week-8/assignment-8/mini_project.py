import csv

rows_attempted = 0
rows_parsed = 0
rows_skipped = 0
skipped_rows = []
clean_data = []

try:
    with open("python-intro-homework/week-8/data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=1):
            rows_attempted = rows_attempted + 1
            try:
                if len(row) > 3:
                    rows_skipped = rows_skipped + 1
                    skipped_rows.append(f"Row {row_number}: extra column detected — skipped")
                    continue

                amount = float(row["amount"])

                clean_data.append({"name": row["name"], "category": row["category"], "amount": amount})
                rows_parsed = rows_parsed + 1

            except ValueError:
                rows_skipped = rows_skipped + 1
                skipped_rows.append(f"Row {row_number}: ValueError — could not convert '{row['amount']}' to float")
            except KeyError:
                rows_skipped = rows_skipped + 1
                skipped_rows.append(f"Row {row_number}: KeyError — missing column")
except FileNotFoundError:
    print("Error: file not found. Please check the file path and try again.")
    exit()

print(f"""=== CSV Report ===
Rows attempted: {rows_attempted}
Rows parsed: {rows_parsed}
Rows skipped: {rows_skipped}\n""")
print("Skipped rows:")
for message in skipped_rows:
    print("  " + message)
print("\nClean data:")
for row in clean_data:
    print(row["name"], row["category"], row["amount"])