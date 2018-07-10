def count_lines(file_name,starting_with):
    file = open(file_name)
    count = 0
    for line in file:
        print(line)
        if line.startswith(starting_with):
            count += 1
    return count


file_name = input('Enter your file here:')
print(count_lines(file_name,'1997'))
print(count_lines(file_name,'1996'))
