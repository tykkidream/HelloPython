print("\n# 01")

file_name = "pi_digits.txt"

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


print("\n# 02")

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


print("\n# 03")

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


print("\n# 04")

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


print("\n# 05")

file_name = "programming.txt"

with open(file_name, "w") as file_object:
    file_object.write("I love programming.")
    file_object.write("I love programming.\n")
    file_object.write("I love programming.\n")


print("\n# 06")

file_name = "programming.txt"

with open(file_name, "a") as file_object:
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


print("\n# 07")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("\n# 08")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


print("\n# 09")

file_name = "alice.txt"

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('Sorry, the file ' + file_name + " does not exist.")


print("\n# 10")

contents = "Alic in wonderland"
words = contents.split()
num_words = len(words)
print(num_words)


print("\n# 11")

def count_words(fileName):
    """计算一个文件大致有多少个单词"""
    try:
        with open(fileName) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("-")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + fileName + " has about " + str(num_words) + " words.")


count_words("pi_digits.txt")
count_words("alice.txt")
count_words("programming.txt")

