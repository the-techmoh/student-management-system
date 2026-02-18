def greet():
    print("Hello, welcome to Software Engineering!")

greet()
greet()

def greet_user(name):
    print("Hello", name, "welcome!")

greet_user("Mohammed")
greet_user("Aisha")


def calculate_age(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age

user_age = calculate_age (int(input("Enter your Birth Year : ")))
print("Your age is:", user_age)

#Combine Functions + Logic

def check_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

result = check_grade(6)
print("Grade:", result)

#addtion



def check_grade(score):
    if score >= 70:
        return "Pass"
    elif score >= 60:
        return "Pass"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

result = check_grade(65)
print("Grade:", result)


def add_numbers(a,b):
    return a + b
result = add_numbers(5, 10)
print(result)

