print(not True and False) # not True is False; False and False is False
print(True or False and False) # and operates first; True or any value will always be True
print(not (5 > 3)) # 5 is greater than 3 so that's True but the not makes it False
print(10 == 10 and 4 != 4) # the first part is True but the second part is false. Since and is there, the whole thing is false
print(not False or not True) # the line is True or False, which is True because of the or