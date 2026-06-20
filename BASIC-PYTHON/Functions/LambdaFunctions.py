'''
Lambda Functions :- Lambda functions are small anonymous functions, meaning they do not have a defined name. these are small,
short-lived functions used to pass simple logic to another function.

-> Contain only one expression.
-> Result of that expression is returned automatically (no return keyword needed)

'''

a = 'Hello to myself'
upper = lambda x: x.upper()
print(upper(a))

square = lambda num: num**2
print(square(4))

#Use Cases
#1. Condition Checking : lambda function can use conditional expressions(if-else)
    # to return different results based on a condition.

check = lambda x : "Postive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(-2))
print(check(3))
print(check(0))


#2. List Comprehension : Lambda can be combined with list comprehensions to apply the same operation to multiple values
#                        in a compact way.

func = [lambda arg=x: arg * 10 for x in range(1,5)]
for i in func:
    print(i())

#3. Returning Multiple Results: Although a lambda can contain only one expression, it can still return
                                # multiple results by combining them into a tuple.

calc = lambda x,y: (x + y, x * y)
res = calc(3,4)
print(res)
# lambda function performs both addition and multiplication and returns a tuple with both result.

#4.filter() : This function uses a lambda expression to select elements from a list that satisfy a given condition, such as keeping only even numbers.

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0,c)
print(list(even))

d = [13, 29, 67,39, 48]
multipleOf13 = filter(lambda x: x%13 == 0, d)
print(list(multipleOf13))

#5. map() :- This function applies a lambda expression to each elements and return a map object. it can be converted to a list using list().

a = [1, 2, 3, 4]
double = map(lambda x: x*2,a)
print(list(double))

e = [4,3,5,2]
triple = map(lambda x: x*3,e)
print(list(triple))

#6. reduce() : lambda function repeatedly applies a lambda expression to elements of a list to combine them into a single result.

from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)





