# the lambda function uses nested if-else logic to classify numbers as Positive, Negative or Zero.
# n = lambda x: "positive" if x > 0 else "Negative" if x < 0 else "zero"

# print(n(5))
# print(n(-5))
# print(n(0))

# This lambda checks divisibility by 2 and returns "Even" or "Odd" accordingly.
check = lambda x: "even" if x % 2 == 0 else "odd"
print(check(4))
print(check(3))