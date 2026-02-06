name = input("Enter your Name: ")
score = int(input("Enter your grade: "))

if score >= 70:
    print("Name: ", name),
    print("Grade: A"),
elif score >= 60:
    print("Name: ", name),
    print("Grade: B"),

elif score >= 50:
    print("Name: ", name),
    print("Grade: C"),

else:
    print("Name: ", name),
    print("Failed"),

if score > 100 or score < 0:
    print("Sorry You've Enterred an Impossible Number, TRY AGAIN")