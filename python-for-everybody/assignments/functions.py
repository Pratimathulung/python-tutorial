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


# Write a python function to calculate the factorial of a number(a non-negative integer). The function accepts the
#  number as an integer
def factorial(number):
    if number == 0:
        number = 1
    else:
        number = number * factorial(number - 1)
    return number


print(factorial((4)))
print(factorial((5)))


# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# in a given range

def find_number(min, max):
    result = []
    for number in range(min, max):
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result


min = int(input("Enter min:"))
max = int(input("Enter max:"))
print(find_number(min, max))


# Write a function to check whether a number is in a given range
def test_range(number):
    if number in range(5, 8):
        print("%d is in given range" % number)
    else:
        print("The number is not in given range")


test_range(7)


# Write a program to reverse string
def reverse_string(str):
    string_reverse = (str[::-1])
    return string_reverse


print(reverse_string('Pratima'))


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_upper_lower(string):
    upper_case = 0
    lower_case = 0
    for letter in string:
        if letter.isupper():
            upper_case += 1
        if letter.islower():
            lower_case += 1
        else:
            pass
    print("String:%s" % string)
    print("Upper Case:%d" % upper_case)
    print("Lower Case:%d" % lower_case)


count_upper_lower("My name is Pratima Rai")


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def create_unique_list(numbers):
    list = []
    for n in numbers:
        if n not in list:
           list.append(n)
    return list


print(create_unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

