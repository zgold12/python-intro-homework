cod1 = ["python", "ruby", "sql"]
cod2 = ["json", "xml", "ruby"]
lang1 = set()
lang2 = set()
for i in cod1:
    lang1.add(i)
for g in cod2:
    lang2.add(g)
print(lang1.union(lang2))          
print(lang1.intersection(lang2))   
print(lang1.difference(lang2))