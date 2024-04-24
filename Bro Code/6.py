#user input
name = input("What is your name: ")
age = int(input("How old are you: "))
height = float(input("How tall are you?: "))

# age += 1

print("Hello {0}".format(name))
print("You are {0} years old".format(str(age)))
print("You are {0} cm tall".format(str(height)))