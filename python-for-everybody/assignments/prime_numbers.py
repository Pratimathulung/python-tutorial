# Wap to find prime numbers

def is_prime(number):
    if number == 2:
        return True
    if number < 2:
        return False
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True


# number=(int(input('Enter your number:')))
# print (is_prime(number))


def find_primes(min, max):
    primes = []
    for num in range(min, max):
        if is_prime(num):
            primes.append(num)
    return primes


min = int(input('Enter min:'))
max = int(input('Enter max:'))

print(find_primes(min, max))
