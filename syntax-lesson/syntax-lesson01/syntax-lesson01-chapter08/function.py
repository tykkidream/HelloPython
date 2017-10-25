print("\n# 01")


def greet_user():
    """显示简单的问候语"""
    print("Hello")


greet_user()

print("\n# 02")


def greet_user(username):
    """显示简单的问候语"""
    print("Hello " + username.title() + "!")


# 　greet_user()　会出错
greet_user("jesse")

print("\n# 03")


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet(pet_name="willie", animal_type="dog")

print("\n# 04")


def describe_pet(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("willie")
describe_pet(pet_name="willie")
describe_pet("willie", animal_type="dog")
describe_pet("willie", "hamster")

print("\n# 05")


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()


print(get_formatted_name("jimi", "hendrix"))


print("\n# 06")

def get_formatted_name(first_name, last_name, middle_name=""):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


print(get_formatted_name("jimi", "hendrix"))
print(get_formatted_name("jimi", "hendrix", "lee"))


print("\n# 07")

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    return person


print(build_person("jimi", "hendrix"))


print("\n# 08")

def build_person(first_name, last_name, age=""):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


print(build_person("jimi", "hendrix",28))


print("\n# 09")

while True:
    print("\nPlease tell me you name:")
    f_name = input("\tFirst name: ")
    if f_name == "q":
        break

    l_name = input("\tLast name:  ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


print("\n# 10")

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

greet_users(["hannah", "ty", "margot"])


print("\n# 11")

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


print("\n# 12")

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


print("\n# 13")

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


print("\n# 14")

def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


print("\n# 15")

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, "pepperoni")
make_pizza(22, "mushrooms", "green peppers", "extra cheese")


print("\n# 16")

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
        print("\t" + key + " - " + value)
    return profile

print(build_profile("albert", "einstein", location = "princeton", field = "physics"))
print(build_profile(first = "albert",  location = "princeton", field = "physics", last = "einstein"))

