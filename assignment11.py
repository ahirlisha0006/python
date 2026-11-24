#1
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
#2
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")
#3
light = input("Enter traffic light color: ")

if light.lower() == "red":
    print("Stop")
elif light.lower() == "yellow":
    print("Wait")
elif light.lower() == "green":
    print("Go")
else:
    print("Invalid color")
#4
balance = 50000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance and amount > 0:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance or invalid amount")
#5
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
#6
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is within the range")
else:
    print("Number is outside the range")
#7
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
#8
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity bill: Rs.", bill)
#9
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
#10
6a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")    