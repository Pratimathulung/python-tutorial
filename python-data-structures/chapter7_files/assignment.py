file = open('BE_result.csv', 'r')
result = []
for line in file:
    if "Ilam" in line:
        result.append(line.split(','))
print(result)









