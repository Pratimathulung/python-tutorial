# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
#  second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


def find_hrs(file_name):
    file = open(file_name)
    result = []
    for line in file:

        if not line.startswith('From') or line.startswith('From:'):
            continue
        else:
            words = line.split()
            word = words[5].split(':')
            result.append(word[0])
    return result


file_name = input('Enter file here:')
hrs = find_hrs(file_name)


def count_hrs(hrs):
    counts = dict()
    for hr in hrs:
        if hr not in counts:
            counts[hr] = 1
        else:
            counts[hr] = counts.get(hr, 0) + 1
    return counts


counted_hrs = count_hrs(hrs)


def sorting_hrs():
    lst = []
    for key, value in sorted(counted_hrs.items()):
        lst.append((key, value))
    return lst


result = sorting_hrs()
for key, value in result:
    print(key, value)
