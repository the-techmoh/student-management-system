count = 1
while count <=10:
    print("Count:", count)
    count +=1

score = int(input("Enter Score (0-100):"))

while score <0 or score >100:
    print("Invalid Score. Try Again")
    score = int(input("Enter Score (0-100)"))

print("Valid Score Entered:", score)


#password challenge

password = ""

while password != "admin123":
    password = input("Enter Password:")
print("Access Granted")