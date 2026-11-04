num = 0
yes = False
while yes == False:
    try:
        num = int(input("Enter a positive integer:"))
        if num > 0:
            yes = True
            print(f"Got it: {num}")
        else: 
            print("That's not a positive integer. Try again.")
    except:
        print("That's not a positive integer. Try again.")