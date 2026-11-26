#1
numbers= (10,20,30,50)
print(numbers)
#2
numbers= (10,20,30,50)
print("third element:",numbers[2])
#3
students =("lisha",21,"bca")
name,age,course=students
print(name)
print(age)
print(course)
#4
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}

print(fruits)
#5
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}
fruits.add("appi")
print(fruits)
#6
fruits ={"Apple","Mango","Banana","Orange","Grapes"}
fruits.remove("Apple")
print(fruits)
#7
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
#8
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Intersection:", a.intersection(b))
#9
a = {1, 2}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))
#10
numbers = [10, 20, 30, 20, 40, 10, 50]

unique = set(numbers)

print(unique)

#11
students={
    "rahul":88,
    "lisha":91,
    "riya":30
    }
print(students)
#12
students = {
    "Rahul": 85,
    "lisha": 90
}

students["riya"] = 78

print(students)
#13
students = {
    "rahul":88,
    "lisha":91,
    "riya":90
}
del students["rahul"]
print(students)
#14
a = {"Rahul": 85, "Priya": 90}
b = {"Amit": 78, "Neha": 88}

a.update(b)

print(a)
#15
students = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78
}

if "Rahul" in students:
    print("Key exists")
else:
    print("Key does not exist")
#16
text = "apple banana apple mango banana apple"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
#17
marks = {
    "rahul":88,
    "lisha":91,
    "priya":89
}  
hightest=max(marks,key=marks.get)
print("Highest marks :",hightest)
#18
data={
    "A":1,
    "B":2,
    "C":3
}  
reverse={}
for key,value in data.items():
    reverse[value] = key
    print(data)
#19
students={
    "lisha":91,
    "riya":88
}
students["lisha"]=95
print(students)
#20
data = [
    ("Name", "lisha"),
    ("Age", 21),
    ("Course", "BCA")
]

result = dict(data)

print(result)

