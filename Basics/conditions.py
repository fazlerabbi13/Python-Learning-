# age = int(input("Enter age: "))
# if age <= 20:
#     print("eligible for playing")
# else:
#     print("not eligible")


# elif Statement
# age = int(input("Enter age: "))

# if age <= 15:
#     print("Child")
# elif age <= 18:
#     print("Teenager")
# elif age <= 30:
#     print("Young Adult")
# else:
#     print("Adult")


# Nested if..else Conditional Statement

# age = int(input("Enter age: "))
# age = 15
# is_eligible = True

# if age >= 20:
#     if is_eligible:
#         print("eligible for vote")
#     else:
#         print("not eligible")
# else:
#     print("Child")

# age = int(input("Enter age: "))
# result = "Adult" if age >= 18 else "child"
# print(result)

# Match-Case Statement

number = int(input("Enter number: "))
match number:
    case 1:
        print("one")
    case 2 | 3 | 5:
        print("Two or Three or five")
    case _:
        print("other number")
  