
#1
class animal:
    def sound(self):
        print("animals are relly gud!!!")
class dog(animal):
    def bark(self):
        print("dogs barks")
class cat(animal):
    def meow(self):
        print("cats do not bark")
d=dog() 
d.sound()
d.bark()  

c=cat()
c.sound()
c.meow()

#2
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

e = ElectricCar()
e.start()
e.drive()
e.charge()
#3
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Animal()
a.sound()

d = Dog()
d.sound()
#4
class Father:
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")

c = Child()
c.show_father()
c.show_mother()
c.show_child()
#5
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Rectangle:
    def area(self):
        return 10 * 5

def calculate_area(shape):
    print("Area:", shape.area())

c = Circle()
r = Rectangle()

calculate_area(c)
calculate_area(r)
#6
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def show(self):
        print("Savings Account Balance:", self.balance)

class CurrentAccount(BankAccount):
    def show(self):
        print("Current Account Balance:", self.balance)

s = SavingsAccount(5000)
c = CurrentAccount(10000)

s.show()
c.show()
#7
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

s = Student("liya")

print("Name:", s.get_name())

s.set_name("lisha")

print("Updated Name:", s.get_name())
#8
class Person:
    def show(self):
        print("This is a person")

class Teacher(Person):
    def teach(self):
        print("Teacher teaches students")

class Student(Person):
    def study(self):
        print("Student studies")

t = Teacher()
t.show()
t.teach()

s = Student()
s.show()
s.study()
#9
class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")

m = MusicPlayer()
m.play()

s = Spotify()
s.play()
#10
class Parent:
    def __init__(self):
        print("This is Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is Child class")

c = Child()



