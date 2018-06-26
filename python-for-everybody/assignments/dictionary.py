# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:

def find_squares(number):
    result = {}
    for num in range(1, number + 1):
        result[num] = num * num
    return result


number = int(input('Enter your number:'))
print(find_squares(number))
