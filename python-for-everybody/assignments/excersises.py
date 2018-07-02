# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
#  number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_even(min, max):
    result = []
    for number in range(min, max + 1):
        if number % 2 == 0:
            result.append(str(number))
    return ','.join(result)


min = int(input('Enter min:'))
max = int(input('Enter max:'))
print(find_even(min, max))
