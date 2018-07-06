#1) Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
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


#2) Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
def count_number(line):
    upper_case = 0
    lower_case = 0
    for letter in line:
        if letter.isupper():
            upper_case += 1
        if letter.islower():
            lower_case += 1
    print('Upper case: %d' % upper_case)
    print('Lower case: %d' % lower_case)


line = input()
count_number(line)

#3) Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

