def set_name():
    name = "Zach"
set_name()
#print(name)  # NameError: name 'name' is not defined

def set_name():
    name = "Zach"
    return name
result = set_name()
print(result)