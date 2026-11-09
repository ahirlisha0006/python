#1
for i in range(1,11):
    print(i)

#2#2
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

 #3
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

#4
n = int(input("Enter how many numbers: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#5
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


#6
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number =", reverse)

#7
num = int(input("Enter a number: "))

count = 0

while num > 0:
    count = count + 1
    num = num // 10

print("Total digits =", count)

#8
total = 0

for i in range(2, 101, 2):
    total = total + i

print("Sum of even numbers =", total)
#9
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

#10
num = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)



    