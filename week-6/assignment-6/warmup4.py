def is_valid_score(score):
    return score >= 0 and score <= 100
scr = int(input("Enter score here:"))
if is_valid_score(scr) == True:
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")