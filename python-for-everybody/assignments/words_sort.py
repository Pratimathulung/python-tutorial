# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.

def sort_word(words):
    sorted_words = sorted(words)
    return ','.join(sorted_words)


words = input("Enter your words here:").split(',')
print(sort_word(words))


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
#  all duplicate words and sorting them alphanumerically.

def remove_duplicate(words):
    result = set(words)
    return ' '.join(sorted(result))


words = input('Enter your line here:').split(' ')
print(remove_duplicate(words))
