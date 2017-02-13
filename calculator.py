##adamgrierson
##13/10/16
##calculator

menu = "what would you like to calculate:\n\
    1. Multiply\n\
    2. subtract\n\
    3. add\n\
    4. divide\n"

answer = int(input (menu))

def multiply (x,y):
    return x * y
def subtract (x,y):
    return x - y
def add (x,y):
    return x + y
def divide (x,y):
    return x / y

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if answer == 1:
    print (num1, "*", num2,"=", multiply(num1,num2))

elif answer == 2:
    print (num1, "-", num2,"=", subtract(num1,num2))

elif answer == 3:
    print (num1, "+", num2,"=", add(num1,num2))

elif answer == 4:
    print (num1, "/", num2,"=", divide(num1,num2))

else:
    print("invalid input")
