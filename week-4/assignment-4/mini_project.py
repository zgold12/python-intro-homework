students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
top = 0
for i in students:
    scr = i["score"]
    if scr > top:
        top = scr
        pers = i["name"]
print(f"Top scorer: {pers} ({top})")
tot = 0
for g in students: 
    tot += g["score"]
print(f"Class average: {tot/len(students):.2f}")
cls = set()
for h in students:
    cls.add(h["subject"])
print(f"Subjects offered: {cls}")
tstud = []
for j in students:
    if j["score"] > 75:
        tstud.append(j["name"])
print(f"High scorers: {tstud}")