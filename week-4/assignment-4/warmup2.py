stud = {"name":"bob", "grade": 67, "subjects": ["math","science","english"]}
for i,v in stud.items():
    print(i,v)
stud["graduated"] = "false"
print(stud.items())
