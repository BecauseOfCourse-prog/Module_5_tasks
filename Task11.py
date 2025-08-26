from functools import reduce

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubed = list(map(cube, numbers))
print(cubed)


def is_multiplicity(x):
    return x % 5 == 0

mult_numbers = list(filter(is_multiplicity, numbers))
print(mult_numbers)


def is_not_even(x):
    return x % 2 != 0

def multiply(x, y):
    return x * y

res = reduce(multiply, list(filter(is_not_even, numbers)))
print(res)