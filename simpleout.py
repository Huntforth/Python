first = "Christian"
last = "Peterson"
studentID = "4018009"

print("My name is " + first + " " + last)
print("My student ID is " + studentID)

for char in first:
    print(char)

print("My name all capitalized is " + first.upper() + " " + last.upper())

a = ["sleep,", "travel,", "work."]

print("This summer I plan to ", end = "")

for string in a:
    print(string, end=" ")
