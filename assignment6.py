#1
def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if check_prime(n):
    print("Prime number")
else:
    print("Not a prime number")

#2
def reverse_string(text):
    return text[::-1]

word = input("Enter a string: ")

print("Reversed string:", reverse_string(word))
#3
def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result

n = int(input("Enter a number: "))

print("Factorial:", factorial(n))
#4
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))
#5
def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")

if check_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
#6
def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count

text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))
#7
def merge_lists(list1, list2):
    return list1 + list2

a = [1, 2, 3]
b = [4, 5, 6]

print("Merged list:", merge_lists(a, b))
#8
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD:", find_gcd(x, y))
#9
def rectangle_area(length, breadth):
    return length * breadth

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print("Area of rectangle:", rectangle_area(l, b))
#10
def check_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == num

n = int(input("Enter a number: "))

if check_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")    
    