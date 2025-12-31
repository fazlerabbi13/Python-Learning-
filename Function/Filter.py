# filter() to extract all even numbers from a list.
def even(n):
    return n % 2 == 0
nums = [1, 2, 3, 4, 5]
f = filter(even, nums)
print(list(f))

# Using filter() with a Lambda Function

l = filter(lambda x: x % 2 == 0, nums)
print(list(l)) 
