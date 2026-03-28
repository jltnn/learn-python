def my_func(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_func(1,2,3))
print(my_func(5))

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers [0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(my_function(3,7,2,9,1))

def gojo(upper,lower):
    x = upper + lower
    print(x)
gojo("upper Gojo","Lower Gojo")
    
    