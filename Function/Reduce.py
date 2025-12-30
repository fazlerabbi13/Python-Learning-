#  adding two numbers at a time.
# from functools import reduce
# def add(x, y):
#     return x + y

# nums = [1, 2, 3, 4, 5]
# result = reduce(add, nums)
# print(result)

#  calculate factorial of a number by multiplying all elements of a list.
from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, nums)
print(result)