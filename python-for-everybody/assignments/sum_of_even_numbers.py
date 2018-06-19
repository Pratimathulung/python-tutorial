numbers = [2, 5, 7, 6, 8]
sum = 0
for number in numbers:
    if number % 2 == 0:
        sum += number
print(sum)


def add_even(numbers):
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
    return sum


num = [2, 5, 7, 6, 8]
print(add_even(numbers))





