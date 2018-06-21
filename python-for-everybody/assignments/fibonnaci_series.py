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
def fib(number):
    a, b = 0, 1
    for i in range(number-1):
        a, b = b, a + b
    return a


number = int(input('Enter number:'))
for i in range(1,number):
    print(fib(i))
