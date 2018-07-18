fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = []
for key, value in counts.items():
    new_tuple = (value, key)
    lst.append(new_tuple)
lst = sorted(lst, reverse=True)
print(lst)

for value, key in lst[:10]:
    print(key,value)