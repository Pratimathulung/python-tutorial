books = {'history': 2, 'economics': 5, 'psychology': 3}
print(sorted([(value,key) for key,value in books.items()]))