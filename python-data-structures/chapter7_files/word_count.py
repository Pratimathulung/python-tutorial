import re


def count_word(file_name):
    file = open(file_name)
    result = {}

    words = re.split(r' |\n', file.read())
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result.get(word) + 1
    file.close()
    return result


file_name = input('Enter your file here:')
print(count_word(file_name))
