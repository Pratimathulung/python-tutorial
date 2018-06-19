largest_so_far = -1
print('Before', largest_so_far)
for num in (9, 41, 12, 3, 74, 15):
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print('After', largest_so_far)

count = 0
sum = 0

for num in [2, 4, 5, 8, 9, 25, 35]:
    count = count + 1
    sum = sum + num
    print(count, sum, )

num=[2,4,5,8,9,25,35]
smallest_so_far = num[0]
for index in range(1, len(num)):
    if num[index] < smallest_so_far:
        smallest_so_far = num[index]
print(smallest_so_far)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')