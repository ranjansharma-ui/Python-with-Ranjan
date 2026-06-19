def fun():
    print("Welcome to world!")

fun()

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(4))
print(evenOdd(5))

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)
myFun(10,90)

def student(fname, lname):
    print(fname,lname)

student(fname='Greek', lname='Greek')
student(fname='Ranjan', lname='Sharma')


def nameAge(name, age):
    print("Hi,I am", name)
    print("My age is", age)

print("case-1:")
nameAge("Ranjan",20)
print("case-2:")
nameAge(20,"Ranjan")

#Arbitrary Arguments: allow functions to accept multiple value. This is done using two special symbol.
# *args collects extra positional arguments as a tuple.
# **kwargs collects extra keyword arguments as a dictionary

def myFun(*args, **kwargs):
    print("Non-keyword Arguments (*args):")

    for arg in args:
        print(arg)

    print("keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome',first='Greek', mid='for',last='Greek')

#Function within Functions
'''
A function defined inside another function is called an inner function(or nested function)
it is used to organize related logic and access variable from the outer function.
'''

def f1():
    s = 'I love papa'
    def f2():
        print(s)
    f2()
f1()


# Return Statement

def sq_value(num):
    return num**2
print(sq_value(5))
print(sq_value(-4))

'''
Pass by Reference and Pass by Value
Variables refer to objects. Function behavior depends on whether the object is mutable or immutable.

-> Mutable object like lists can be modified inside functions.
-> Immutable objects like integers and strings remain unchanged.
 
'''

def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)

def myfun2(x):
    x = 20

a = 10
myfun2(a)
print(a)

