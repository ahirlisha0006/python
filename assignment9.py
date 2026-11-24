#1
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")
#2
try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Please enter a valid integer")
#3
try:
    file = open("demo.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")
#4
try:
    a=int(input("enter first  number:"))
    b=int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)
except ValueError:
 print("please enter an number only ")
except ZeroDivisionError:
  print("Cannot divide by zero")
#5
file = None

try:
    file = open("demo.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    if file is not None:
        file.close()

    print("File operation completed")
#6
class  InvalidAgeError (Exception):
 pass 
try:
    age=int(input("enter your age: "))
    if age < 18:
        raise InvalidAgeError("your age must be above 18")
    print("you are eligible ")
except InvalidAgeError as e:
    print(e)

except ValueError:
    print("Please enter a valid age")
#7
my_list =[10,20,30,45,70]
try:
    print(my_list[67])
except IndexError:
    print("this is not in the range")
#8
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Division:", result)

except ValueError:
    print("Invalid input! Enter integers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Some other error occurred:", e)    

#10
class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")

    print("Valid email address")

except InvalidEmailError as e:
    print(e)


    
        