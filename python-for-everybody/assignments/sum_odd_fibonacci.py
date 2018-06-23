# Wap to print sum of odd fibonacci numbers in given range

def odd_fib_series(min, max):
    result = []
    f1, f2 = 0, 1
    while f2 < max:
        if f2 >= min and f2 % 2 != 0:
            result.append(f2)
        f1, f2 = f2, f1 + f2
    return result


min = int(input("Enter min:"))
max = int(input("Enter max:"))
print(odd_fib_series(min, max))


def odd_fib_sum(min, max):
    fib_series = odd_fib_series(min, max)
    sum = 0
    for number in fib_series:
        sum += number
    return sum


print(odd_fib_sum(min, max))

# More efficient way to find sum of odd fibonacci numbers
def find_odd_fib_sum(min, max):
    sum = 0
    f1, f2 = 0, 1
    while f2 < max:
        if f2 >= min and f2 % 2 != 0:
            sum += f2
        f1, f2 = f2, f1 + f2
    return sum


print(find_odd_fib_sum(min, max))
