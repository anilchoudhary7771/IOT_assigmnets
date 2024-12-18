#Write a program to accept three integer numbers and find its average.
def avg_func():
    num1 = int(input("Enter integer num1: "))
    num2 = int(input("Enter integer num2: "))
    num3 = int(input("Enter integer num3: "))
    print(f"Average: {(num1+num2+num3)/3}")

avg_func()