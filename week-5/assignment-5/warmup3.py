lst = ["bob", "susan", "harry", "sally"]
nme = input("Enter a name:").lower()
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return f"Found {nme.capitalize()} at index {i}"
    return f"{nme.capitalize()} was not found in the list"
result = linear_search(lst,nme)
print(result)