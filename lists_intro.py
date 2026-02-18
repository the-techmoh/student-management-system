students = ["Mohammed", "Aisha", "Sadiq", "Fatima"]

print(students)

print(students[0])  #Mohammed
print(students[2])  # Sadiq

students.append("Zainab")
print(students)

for student in students:
    print("Students:", student)

print("Total Students:", len(students))



scores = []

scores.append(70)
scores.append(85)
scores.append(60)

total = 0
for score in scores:
    total += score

average = total / len(scores)
print("Average score:", average)


names = []
names.append(input("Enter name: "))
names.append(input("Enter name: "))
names.append(input("Enter name: "))
for name in names:
    print("Names: ", name)

count = 1
for name in names:
    print(count, ".", name)
    count += 1

name = []
total = int(input("How many names? :"))

for i in range (total):
    names.append(input("Enter name: "))

    for name in names:
        print(name)
