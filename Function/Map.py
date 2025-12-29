nums = [1, 2, 3, 4, 5]
result = map(int, nums)
print(list(result))

# Converting map object to a list
def cube(val):
    return val * val *val

result = list(map(cube, nums))
print(result)

# map() function with lambda
result = list(map(lambda x: x ** 3, nums))
print(result)