with open("week-7/data/notes.txt", "r") as file:
    x = 0
    for line in file:
        x += 1
        print(f"Line {x}: {line.strip()}")