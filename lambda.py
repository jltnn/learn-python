double = lambda x: x * 2
add = lambda x, y: x + y

print(add(2, 3))
print(double(2))

max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y

full_name = lambda first, last: first + " " + last

print(max_value(4, 5))
print(min_value(9, 5))

print(full_name("Julie", "Nguyen"))
