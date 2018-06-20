# Write a python function to find the max of 3 numbers

def max_of_three(x, y, z):
    max = x
    if max < y:
        max = y
    if max < z:
        max = z
    return max


print(max_of_three(x=4, y=3, z=8))


# Write a function to sum all the numbers in a list

def add_num(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(add_num(numbers=[2, 4, 5, 6, 7, 9]))


# Write a python function to multiply all the numbers in list.
def multiply(numbers):
    result = 1
    for number in numbers:
        result = result * number
    return (result)


print(multiply((8, 2, 3, -1, 7)))


# Write a python function to calculate the factorial of a number(a non-negative integer). The function accepts the number as an integer
def factorial(number):
    if number == 0:
        number = 1
    else:
        number = number * factorial(number - 1)
    return number


print(factorial((4)))
