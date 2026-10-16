day = input("What day is it?").lower()
time = input("What time of day is it?").lower()

if day == "thursday":
    if time == "morning": print("Hit the gym.")
    elif time == "afternoon": print("Go to work.")
    elif time == "evening": print("Go to happy hour.")
    else: print("Sorry, I only have suggestions for morning, afternoon or evening.")
elif day == "friday":
    if time == "morning": print("Go for a run.")
    elif time == "afternoon": print("Open a beer.")
    elif time == "evening": print("Go to a party.")
    else: print("Sorry, I only have suggestions for morning, afternoon or evening.")
elif day == "saturday":
    if time == "morning": print("Go back to sleep.")
    elif time == "afternoon": print("Walk the dog.")
    elif time == "evening": print("Go clubbing.")
    else: print("Sorry, I only have suggestions for morning, afternoon or evening.")
else: print("Sorry, I only have suggestions for Thursday-Saturday.")