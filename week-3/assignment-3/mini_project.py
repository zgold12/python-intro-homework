day = input("What day is it?").lower()
time = input("What time of day is it?").lower()

if day == "thursday":
    if time == "morning": print("Hit the gym.")
    if time == "afternoon": print("Go to work.")
    if time == "evening": print("Go to happy hour.")
elif day == "friday":
    if time == "morning": print("Go for a run.")
    if time == "afternoon": print("Open a beer.")
    if time == "evening": print("Go to a party.")
elif day == "saturday":
    if time == "morning": print("Go back to sleep.")
    if time == "afternoon": print("Walk the dog.")
    if time == "evening": print("Go clubbing.")
else: print("Sorry, I only have suggestions for Thursday-Saturday in the morning, afternoon or evening.")