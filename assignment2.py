#1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

remainder = a % b

print("Remainder =", remainder)

#2
num=int(input("enter an number:"))
if num % 2 ==0:
 print ("number is even ")
else:
 print ("number is odd")

 #3
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if a > b:
    print("Larger number =", a)
else:
    print("Larger number =", b)


  #4
num = int(input("Enter a number: "))
square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

#5
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")


#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a > 0 and b > 0

print(result)

#7
num = float(input("Enter a decimal number: "))

result = int(num)

print("Integer value =", result)

#8
num = input("Enter a number: ")

num = int(num)

result = num * 10

print("Result =", result)

#9
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print("Both numbers are positive")

elif a > 0 or b > 0:
    print("At least one number is positive")

else:
    print("Both numbers are negative or zero")


#10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
quotient = a // b
remainder = a % b

print("Quotient =", quotient)
print("Remainder =", remainder)
