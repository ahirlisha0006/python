#1
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration:", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed after braking:", self.speed)

c = Car("Toyota", "Innova", 40)

print("Brand:", c.brand)
print("Model:", c.model)
print("Speed:", c.speed)

c.accelerate()
c.brake()
#2
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Balance:", self.balance)

b = BankAccount(5000)

b.deposit(1000)
b.withdraw(2000)
b.display()
#3
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print("Average marks:", avg)

s = Student(80, 70, 90)
s.average()
#4
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.breadth))

r = Rectangle(10, 5)

r.area()
r.perimeter()
#5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

e = Employee("lisha", 25000)
e.display()
#6
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b = Book("Python Basics", "lisha", 450)
b.display()
#7
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * 3.14 * self.radius)

c = Circle(5)

c.area()
c.circumference()
#8
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percentage):
        discount_amount = self.price * percentage / 100
        final_price = self.price - discount_amount

        print("Brand:", self.brand)
        print("Original Price:", self.price)
        print("Final Price:", final_price)

l = Laptop("HP", 50000)
l.discount(10)
#9
class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked successfully")
        else:
            print("No seats available")

    def display(self):
        print("Available seats:", self.seats)

f = Flight(3)

f.display()
f.book_seat()
f.book_seat()
f.display()
#10
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added successfully")

    def list_products(self):
        print("Products in shop:")
        for product in self.products:
            print(product)

s = Shop()

s.add_product("Laptop")
s.add_product("Mobile")
s.add_product("Headphones")

s.list_products()