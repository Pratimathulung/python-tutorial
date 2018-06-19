# def add_odd(numbers):
#     sum = 0
#     for number in numbers:
#         if number % 2 == 1:
#             sum += number
#     return sum
#
#
# print(add_odd(numbers=[1, 3, 5, 6, 8, 11]))

# numbers = [1, 3, 5, 6, 8, 11]
# even_sum = 0
# odd_sum = 0
# for number in numbers:
#     if number % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number
# print(even_sum)
# print(odd_sum)
# difference = odd_sum - even_sum
# print(difference)

# def get_even_odd_sum(numbers):
#     sum_even = 0
#     sum_odd = 0
#     for number in numbers:
#         if number % 2 == 0:
#             sum_even += number
#         else:
#             sum_odd += number
#     return (sum_even, sum_odd)
#
# print(get_even_odd_sum(numbers=[1, 3, 5, 6, 8, 11]))

# Write a programming to find the difference of sum of even and sum of odd numbers.


def get_even_odd_sum_diff(numbers):
    sum_odd = 0
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    return sum_even - sum_odd


print(get_even_odd_sum_diff([1, 3, 5, 6, 8, 11]))
