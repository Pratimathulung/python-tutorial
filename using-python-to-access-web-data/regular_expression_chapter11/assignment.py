import re

file = open('regex_sum_105112.txt')
sum = 0
for line in file:
    integers = re.findall('[0-9]+', line)
    for value in integers:
        sum += int(value)
print(sum)
