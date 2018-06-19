# wap to input the list of numbers and find the maximum value using function.

# write a function to input list of numbers and return maximum
# [3,21,1,5,50]
def find_max(numbers):
    max = numbers[0]
    for index in range(1, len(numbers)):
        if max < numbers[index]:
            max = numbers[index]
    return max


nums = [3, 21, 1, 5, 50]
print(find_max(nums))
