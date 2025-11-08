# def evenOdd(n):
#     if(n % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"
    
# print(evenOdd(5))
# print(evenOdd(10))

# default Argument

# def func(x,y=20):
#     print("x = ",x)
#     print("y = ",y)
# func(10)

# Keyword Arguments

# def employee(first, second):
#     print(first, second)

# employee(first="mohammad",second="ali")
# def nameAndAge(name, age):
#     print("hi, i am ",name)
#     print("my age is ", age)

# print("case - 1:")
# nameAndAge("Fazle Rabbi", 20)
# print("\ncase - 2:")
# nameAndAge(20,"Fazle Rabbi")

# Arbitrary Arguments

# Function within Functions

def func1():
    s = 'Hello World'
    def func2():
        print(s)
        
    func2()
func1()