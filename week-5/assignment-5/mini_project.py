numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data
while True:
    menu = int(input("""
        ===== Number Cruncher =====
        1. Find minimum
        2. Find maximum
        3. Search for a number
        4. Sort the list
        5. Quit
        Choose an option (1-5):
    """))
    min = 0
    max = 0
## 1. Find minimum
    if menu == 1:
        for num in numbers:
            if min == 0:
                min = num
            elif min > num:
                min = num
        print(f"The minimum is {min}")
## 2. Find maximum
    elif menu == 2:
        for num in numbers:
            if num > max:
                max = num
        print(f"The maximum is {max}")
## 3. Linear Search
    elif menu == 3:
        usr = int(input("Enter a number:"))
        result = linear_search(numbers,usr)
        if result == -1:
            print("Number not found")
        else:
            print(f"Found {usr} at index {result}")
## 4. Bubble sort
    elif menu == 4:
        print(bubble_sort(numbers))
## 5. Quit
    elif menu == 5:
        break
    else:
        print("That is not a valid entry. Please only type a number 1-5.")