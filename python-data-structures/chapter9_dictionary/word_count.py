# counts = dict()
# line = input('Enter line:')
# words = line.split()
# print('Words:', words)
# print('Counting lines....')
# for word in words:
#     if word not in counts:
#         counts[word] = 1
#     else:
#         counts[word] = counts.get(word)+1
# print('Counts:', counts)


def count_words(line):
    counts = dict()
    for word in line.split():
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts.get(word) + 1
    return counts


print(count_words('the clown ran after the car and the car ran after the tent and the tent fell down on the clown'))






# def count_word(line):
#     result = {}
#     count = 0
#     for word in line.split():