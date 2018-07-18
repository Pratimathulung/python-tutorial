
# sorting through keys
books = {'history': 2, 'economics': 5, 'psychology': 3}
print(books.items())
# print(sorted(books.items()))
for key, value in sorted(books.items()):
    print(key, value)


# sorting through values
books = {'history': 2, 'economics': 5, 'psychology': 3}
lst = list()
for key, value in books.items():
    lst.append((value, key))
print(lst)
print(sorted(lst, reverse=True))