# Reading file

file = open('test.txt')
message = file.read()
print(message)
file.close()

# appending to a pre-existing txt file

file = open('test.txt', 'a')
file.write('\nhello world!!')
file.write('\nAdding QA here:\nWhy robots do not love \nBecause they do not have heart :)')
file.close()




