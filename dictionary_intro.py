student = {
    "name": "Mohammed",
    "age": 20,
    "course": "Software Engineering"
}

print(student)

print(student["name"])
print(student["course"])

student["age"] = 21
student["matric"] = "MOU/SE/2001"

print(student)


for key, value in student.items():
    print(key, ":", value)


scores = {}

scores["Mohammed"] = 75
scores["Aisha"] = 82
scores["Sadiq"] = 64

for name, score in scores.items():
    print(name, "scored", score)
