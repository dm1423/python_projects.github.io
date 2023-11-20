# Exercise
# if temperature is greater than 30
#   it's a hot day
# otherwise if it's less than 10
#   it's a cold day
# otherwise
#   it's neither hot nor cold

temperature = 30

if temperature >= 30:
    print("It's a hot day.")
else:
    print("It's not a hot day")

# creating a user input using comparison operators

temperature = input("Input temperature here: ")

if float(temperature) >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Exercise
#if name is less than 3 characters long
#   name must be at least 3 characters
#otherwise if it's more than 50 characters long
#   name can be a maximum of 50 characters
#otherwise
#   name looks good!

name = input("Name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can only be a maximum of 50 characters")
else:
    print("Name looks good!")

