# "This is not good because this is bad"

def count_word(line):  # line= "This is not good because this is bad"
    words = line.split(" ")  # words=["This","is","not","good","because","this","is","bad"]
    result = {}
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result.get(word) + 1
    return result


print(count_word("this is not good because this is bad"))
