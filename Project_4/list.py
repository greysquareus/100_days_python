fruits = ["apple", 123, 1.23, True, {"key": "value"}, {1, 2, 3}, (1, 2, 3)]

print(fruits)
# ['apple', 123, 1.23, True, {'key': 'value'}, {1, 2, 3}, (1, 2, 3)]

print(fruits[4])
# {'key': 'value'}

print(fruits[0])
# apple

fruits[1] = 111
print(fruits[1])
# 111 instead of 123

fruits.append("Gennaland")
print(fruits[-1])
# Gennaland