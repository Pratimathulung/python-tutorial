# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.

def sort_word(words):
    sorted_words = sorted(words)
    return ','.join(sorted_words)


words = input("Enter your words here:").split(',')
print(sort_word(words))
