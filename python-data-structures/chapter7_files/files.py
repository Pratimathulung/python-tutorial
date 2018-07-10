def count_lines(file_name):
    file = open(file_name)
    count = 0
    for line in file:
        if line.startswith('1997'):
            count += 1
    return count


file_name = input('Enter your file here:')
print(count_lines(file_name))
