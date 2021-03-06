# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
#  split() method. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting words
# in alphabetical order.

import re

# file_name = input("Enter file name: ")
# file = open(file_name)
# lst = list()
# for line in file:
#     line = line.rstrip().split()
#     for i in line:
#         if not i in lst:
#             lst.append(i)
# lst.sort()
# print(lst)

def remove_repeated_words(file_name):
    file = open(file_name)
    result = list()
    words = re.split(r' |\n', file.read().rstrip())
    for word in words:
        if word in result:
            continue
        else:
            result.append(word)
    result.sort()
    return result


file_name = input('Enter your file here:')
print(remove_repeated_words(file_name))



