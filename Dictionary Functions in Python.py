d={"vanita":"python","pahal":"maths","pratham":"php"}

print(d)
print(d.keys())
print(d.values())

for i in d:
    print(i," = " ,d[i])

d["henik"]="JAVA"
print(d)
d["vanita"]="DBMS"
print(d)

n=len(d)
print("length=",n)

print("pahal" in d)
print("xyz" not in d)

print(d["vanita"])
print(d.get("vanita"))

d.pop("pratham")
print(d)
del d["pahal"]
print(d)
d.clear()
print(d)






