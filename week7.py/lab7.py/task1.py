# A simple function
def greet(name):
    return "Hello " + name


# (a) Assign function to another variable
new_greet = greet
print(new_greet("Nikhil"))


# (b) Pass function as an argument
def call_function(func, name):
    print(func(name))


call_function(greet, "Ravi")


# (c) Return a function from another function
def create_greeting():
    def message(name):
        return "Welcome " + name

    return message


g = create_greeting()
print(g("Asha"))
# output:
# Hello Nikhil
# Hello Ravi
# Welcome Asha