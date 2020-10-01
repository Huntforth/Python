firstName = "Christian"
lastName = "Peterson"
studentID = "4018009"

print("My name is " + firstName + " " + lastName)
print("My student ID is " + studentID)

for char in firstName:
    print(char)

print("My name all capitalized is " + firstName.upper() + " " + lastName.upper())

a = ["sleep,", "travel,", "work."]

print("This summer I plan to ", end = "")

for string in a:
    print(string, end=" ")
