# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence

from math import *


# c = 50
# h = 30
# # Q = sqrt((2 * c * int(input())) /h)
# # print(round(Q))
#
# input_line = input('Input number in comma seperated sequence: ')
# nums = input_line.split(',')
# print(nums)
# res = [str(round(sqrt((2 * c * int(num)) /h))) for num in nums]
# print(res)
# print(','.join(res))

def calculate_value(line):
    c = 50
    h = 30
    result = []
    for number in line.split(','):
        result.append(str(round(sqrt((2 * c * int(number)) / h))))
    return ','.join(result)


line = input('Input number in comma seperated sequence: ')
print(calculate_value(line))
