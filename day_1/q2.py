"""
Write a program to accept a 4 digit number and
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
ut should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 9
c. 1639
"""

num = int(input("Enter the four digit number: "))
count = 0
val = num
while val != 0:
    count = count + 1
    val = val // 10

ret = 0
val = num
if count != 4:
    print("Invalid number..!!")
else:
    print(f"{val // 1000} {(val // 100) % 10} {(val // 10) %10} {val % 10}")
    print(f"{(val // 1000)*1000} + {((val // 100) % 10)*100} + {((val // 10) %10)*10} + {val % 10}")
    while val != 0:
        ret = ret * 10 + val % 10
        val = val // 10
    print(f"Reverse number: {ret}")