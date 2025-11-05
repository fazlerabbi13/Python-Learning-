# user  = int(input("Enter number: "))
# result = "Even" if user % 2 == 0 else "Odd"
# print(result)


# Ternary Operator in Nested If else
# user = int(input("Enter number: "))
# result = "Possitive" if user > 0 else "Negative" if user < 0 else "Zero"
# print(result)

# Ternary Operator using Tuple
# user = int(input("Enter number: "))
# result = ("Odd","Even")[user % 2 == 0]
# print(result)

# Ternary Operator using Dictionary
# userIn1 =int(input("Enter Number 1: ")) 
# userIn2 =int(input("Enter Number 2: "))
# max = {True: userIn1, False: userIn2}[userIn1 > userIn2]
# print(max)

# Ternary Operator using Python Lambda
userIn1 =int(input("Enter Number 1: ")) 
userIn2 =int(input("Enter Number 2: "))
max = (lambda userIn1,userIn2: userIn1 if userIn1 > userIn2 else userIn2)(userIn1,userIn2)
print(max)