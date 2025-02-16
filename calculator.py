

# def add(x,y):
#     return x+y

# def multiply(x,y):
#     return x*y

# def subtract(x,y):
#     return x-y

# def divide(x,y):
#     if y==0:
#         return "Error, division by zero is not allowed" 
#     else:
#         return x/y

# print ("Calculator")
# print ("1. Addition")
# print ("2. Subtraction")
# print ("3. Multiplication")
# print ("4. Division")

# while True:
#     choice = input("Enter your choice (1,2,3,4):")
#     if choice in ("1", "2", "3", "4"):
#         num1 = int(input("Enter the first number "))
#         num2 = int(input("Enter the second number "))
#         if choice =="1":
#             print(num1, "+", num2, "=", add(num1,num2))
#         elif choice =="2":
#             print (num1, "*", num2, "=", multiply(num1,num2))
#         elif choice =="3":
#             print (num1, "-", num2, "=", subtract(num1,num2))
#         elif choice =="4":
#             print (num1, "/", num2, "=", divide(num1,num2)) 
          
#     else:
#         print("Syntax Error!")

    

print("Simple Calculator")

num1 = int(input("Enter your first number "))
operator = input("Enter your operator ")
num2 = int(input("Enter your second number "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print (num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Error, Division by zero is not allowed")
    else:
        print (num1 / num2)
else:
    print("Syntax Error!")
