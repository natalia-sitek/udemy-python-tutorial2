def function():
    print("Hello World")


function()


def myfunc(name):
    print('Hello ' + name)


myfunc("Jose")


def is_greater(x, y):
    return x > y


print(is_greater(2, 3))


def myfunction(a):
    if a == True:
        return "Hello"
    elif a == False:
        return "Goodbye"


print(myfunction(True))


def changing(x, y, z):
    if z == True:
        return x
    else:
        return y


def myfunct(a, b):
    return a + b


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Define the function called myfunc that takes in arbitrary number of arguments and returns their sum
def myfunc(*args):
    return sum(args)


# Define the function called argument that takes in arbitrary number of arguments and returns a list of arguments which are even
def argument(*args):
    return ([x for x in args if x % 2 == 0])


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return (result)


print(lesser_of_two_evens(10, 2))
