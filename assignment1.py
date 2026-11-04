#1
print("My name is Annie, I am 21 years old and I live in chikhli.")


#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum =", sum)

#3
c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32

print("Temperature in Fahrenheit =", f)

#4
name="lishhaa"
print(name.upper())

#5
birth_year =int(input("enter your birthday:"))
current_year=2026
age=current_year -birth_year
print("age is :",age)


#6
a=10
b=20
print("before swapping:")
print("a=",a)
print("b=",b)
a,b=b,a

print("after swapping")
print("a=",a)
print("b=",b)

#7
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle =", area)

#8

num=int(input("enter an number:"))

if num > 0:
    print("number is positive ")
elif num < 0:
    print("number is negative ")
else :
    print("number is zero")


    #9

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

average = (a + b) / 2

print("Average =", average)
