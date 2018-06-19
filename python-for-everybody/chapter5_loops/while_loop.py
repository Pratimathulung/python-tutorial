n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')

# breaking down of loop
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done')

# finishing an iteration with continue
while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')
