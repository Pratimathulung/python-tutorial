# def find_average():
#     total = 0
#     count = 0
#     average = 0
#     while True:
#         input_str = input('Enter your number here:')
#         if input_str == 'done':
#             break
#         total = float(input_str) + total
#         count = count + 1
#         average = total / count
#     return average

# number = float(input('Enter your number here:'))
# print('Average:', find_average())


def input_values():
    input_list = []
    while True:
        input_str = input('Enter your number here:')
        if input_str == 'done':
            break
        input_list.append(float(input_str))
    return input_list


def find_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)


print(find_average(input_values()))



# total = 0
# count = 0
# while True:
#     inp = input('Enter number :')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total/count
# print('Average:',average)

