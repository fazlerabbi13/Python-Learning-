# user  = int(input("Enter number: "))
# result = "Even" if user % 2 == 0 else "Odd"
# print(result)


# Ternary Operator in Nested If else
# user = int(input("Enter number: "))
# result = "Possitive" if user > 0 else "Negative" if user < 0 else "Zero"
# print(result)

# Ternary Operator using Tuple
user = int(input("Enter number: "))
result = ("Odd","Even")[user % 2 == 0]
print(result)