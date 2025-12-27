# the lambda function uses nested if-else logic to classify numbers as Positive, Negative or Zero.
# n = lambda x: "positive" if x > 0 else "Negative" if x < 0 else "zero"

# print(n(5))
# print(n(-5))
# print(n(0))

# This lambda checks divisibility by 2 and returns "Even" or "Odd" accordingly.
# check = lambda x: "even" if x % 2 == 0 else "odd"
# print(check(4))
# print(check(3))

# The lambda calculates both sum and product of two numbers and returns them as a tuple.
# calculate = lambda x,y:(x + y,x * y)
# res = calculate(3, 4)
# print(res)

# Here, the lambda is used as a filtering condition to keep only even numbers from the list.
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
odd = filter(lambda x: x % 2 != 0, numbers)
print(list(odd))

