# Wap to print the fibonnaci series calling function that gives you list of fibonaci numbers with
# max number as input


# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b

# def fib(number):
#     fib_series = []
#     a, b = 0, 1
#     while b < number:
#         fib_series.append(b)
#         a, b = b, a + b
#
#     return fib_series
#
#
# print(fib(5))
# print(fib(30))
# print(fib(50))
# print(fib(60))

# Wap to print the fibonacci numbers in given range

def fib_series(min, max):
    result = []
    f1, f2 = 0, 1
    while f2 < max:
        if f2 >= min:
            result.append(f2)
        f1, f2 = f2, f1 + f2
    return result


min = int(input('Enter min:'))
max = int(input('Enter max:'))
print(fib_series(min,max))
