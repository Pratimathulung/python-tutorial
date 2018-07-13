# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the
#  following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the
# person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.


def find_address(file_name):
    file = open(file_name)
    result = []
    for line in file:
        if not line.startswith('From') or line.startswith('From:'):
            continue
        else:
            words = line.split()
            result.append(words[1])
    return result


file_name = input('Enter file here:')
emails = find_address(file_name)
print('\n'.join(emails))
print('There were', len(emails), 'lines in the file with From as the first word')