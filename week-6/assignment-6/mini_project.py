data = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
def find_min(numbers):
    min = 0
    for num in numbers:
                if min == 0:
                    min = num
                elif min > num:
                    min = num
    return print(f"The minimum is {min}")
def find_max(numbers):
    max = 0
    for num in numbers:
        if num > max:
            max = num
    return print(f"The maximum is {max}")
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return print(i)
    return print("-1")
def bubble_sort(numbers):
    numbers = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return print(numbers)
def show_menu():
    menu = input("""
        ===== Number Cruncher =====
        1. Find minimum
        2. Find maximum
        3. Search for a number
        4. Sort the list
        5. Quit
        Choose an option (1-5):
    """)
    return menu
def main():
    while True:
        num = int(show_menu())
        if num == 1:
            find_min(data)
        elif num == 2:
            find_max(data)
        elif num == 3:
            search(data, int(input("Enter a number:")))
        elif num == 4:
            bubble_sort(data)
        elif num == 5:
            break
        else:
            print("That is not a valid entry. Please only type a number 1-5.")
main()