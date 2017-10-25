print("\n# 01")

message = input("Tell me something, and I will repeat it back to you: ")

print(message)


print("\n# 02")

name = input("Please enter your name: ")
print("Hello, " + name + "!")


print("\n# 03")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("Hello, " + name + "!")


print("\n# 04")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("成年")


print("\n# 05")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou're be able to ride when you're a little older.")


print("\n# 06")

number = input("Enter a number,and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
