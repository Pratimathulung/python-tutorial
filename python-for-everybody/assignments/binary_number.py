# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

def test_number(numbers):
    result = []
    for number in numbers:
        binary_number = int(number, 2)
        if binary_number % 5 == 0:
            result.append(number)
    return ','.join(result)


numbers = input().split(',')
print(test_number(numbers))


def test_number(numbers):
    result = []
    for number in numbers:
        binary_number = int(number, 2)
        if binary_number % 3 == 0:
            result.append(number)
    return ','.join(result)


numbers = input().split(',')
print(test_number(numbers))
