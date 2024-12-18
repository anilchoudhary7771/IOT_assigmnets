#Using for loop, write and run a Python program to find factorial from 0 to 10.

range = [0,1,2,3,4,5,6,7,8,9,10]
def factorial():
    num = 0
    i = 1
    for num in range:
        i = 1
        fac = 1
        while i <= num:
            fac = fac * i
            i = i + 1
        print(f"Factoial of {num}: {fac}")

factorial()