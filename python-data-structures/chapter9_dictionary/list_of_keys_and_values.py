fruits = {'apple': 5, 'banana': 2, 'mango': 3}
print(list(fruits))  # ['apple', 'banana', 'mango']
print(fruits.keys())  # ['apple', 'banana', 'mango']
print(fruits.values())  # [5,2,3]
print(fruits.items())  # [('apple', 5), ('banana', 2), ('mango', 3)]

for fruit, num in fruits.items():
    print(fruit, num)
