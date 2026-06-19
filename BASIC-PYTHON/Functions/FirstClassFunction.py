'''
First Class function :- In python, function are treated as first-class objects. This
means they can be used just like numbers,string,or any other variable. You can

-> Assign functions to variables.
-> Pass them as arguments to other functions.
-> Return them from functions.
-> Store them in data structures such as lists or dictionaries.

This ability allows you to write reusable, modular and powerful code.

Characteristics of First-Class Functions
Functions in Python have the following important characteristics. Let's see them one by one with
example:
'''

# 1. Assigning Functions to Variables
# We can assign a function to a variable and use the variable to call the function.

def msg(name):
    return f"Hello, {name}!"
# Assigning the function to a variable
f = msg
#Calling the function using the variable
print(f("Emma"))

#2. Passing Functions as Arguments
# -> Function can be passed as arguments to other functions, enabling higher-order functions.

def msg1(name):
    return f"Hello, {name}!"

def fun1(fun2,name):
    return fun2(name)

# Passing the msg function as an argument
print(fun1(msg1, "Ranjan"))

#3. Returning Functions from Other Functions
#-> A Function can return another function, allowing for the creation of function factories.
def fun1(msg):
    def fun2():
        return f"message: {msg}"
    return fun2
#Getting the inner function
func = fun1("Hello, World")
print(func())

#4. Storing Function in Data Structure
#Function can be stored in data structures like lists or dictionaries.

def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

#storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

#Calling functions from the dictionary
print(d["add"](5,3))
print(d["subtract"](5,3))




