"""This is to check the prime number"""
def is_prime(n):
    if n <=1:
        return False
    for i in range (2, (n**0.5) + 1): #Here we add 1, becase range doesn;t include the last number 
        if n % 2==0:
            return False 
    return True 

num = int(input("Enter a number :"))
if is_prime(num):
    print(f"{num} is a prime number ")
else:
    print(f"{num} is not a prime number")





#  A simple CLI calculator 
def add(a,b):
    return a + b
def subtruct(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("\n ---Simple CLI calculator")
    print("1.Add")
    print("2.subtruct")
    print("3.multiply")
    print("4.devide")
    print("5.Exit")

    while True:

        choice = input("\n Choose operation (1-5): ")
        if choice == "5":
            print("Exiting calculator ...")
            break
        if choice not in ["1","2","3","4"]:
            print("Invalid choice")
            continue

        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))
            
        if choice == "1":
            print("Result: ", add(num1,num2) )
        elif choice == "2":
            print("Result: ", subtruct(num1,num2) )
        elif choice == "3":
            print("Result: ", multiply(num1,num2) )
        elif choice == "4":
            print("Result: ", divide(num1,num2) )

calculator()