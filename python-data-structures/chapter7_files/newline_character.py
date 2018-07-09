stuff = 'Hello \nworld'
print(stuff)
print(len(stuff))

x = 'a \nc'
print(len(x))

# Opening a new file
file = open('test.txt')
print(file.read())
file.close()

# file = open('test-write.txt', 'w+')
# file.write('This text should be written')
# file.close()

file = open('ford_escort.csv')
# print(file.readlines())

print('Reading each line...')
lines = file.readlines()


for line in lines[1:]:
    print(line)


# Counting characters length
file = open('ford_escort.csv')
inp = file.read()
print(len(inp))
print(inp[:30])




# Counting lines in a file
file = open('ford_escort.csv')
count = 0
for line in file:
    count += 1
print('line count:', count)


file_name = input('Enter your file name here:')
file = open(file_name)
count = 0
for line in file:
    if line.startswith('1997'):
        count = count + 1
print(count)

