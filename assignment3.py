#1
text=input("enter an string:")
print("length of string:",len(text))

#2
text = input("Enter a sentence: ")

print("Lowercase:", text.lower())

#3
text=input("enter an string:")

result=text.replace(" ","_")
print(result)

#4
text=input("enter an string:")
print("first character:",text[0])
print("last character:",text[-1])

#5
text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)

#6
text=input("enter an string:")
letter=input("enter an letter:")

count=text.count(letter)
print("letter appear:" ,count,"time")

#7
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Word is present")
else:
    print("Word is not present")

#8
name = input("Enter your name:")
age = int(input("Enter your age:"))

print(f"My name is {name} and I am {age} years old.")    

#9
text = input("Enter a string: ")

result = text.strip()

print("After removing spaces:", result)
#10
words = ["Python", "is", "easy"]

result = "$".join(words)

print(result)

#11
movies = ["3 Idiots", "Dangal", "PK", "Chhichhore", "Jawan"]

print("My favorite movies:", movies)

#12
movies = ["3 Idiots", "Dangal", "PK", "Jawan"]

movies.append("Pathaan")

print("Updated movie list:", movies)

#13
movies = ["3 Idiots", "Dangal", "PK", "Jawan"]

movies.pop(0)

print("Updated list:", movies)

#14
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Sorted list:", numbers)

#15
numbers = [50, 10, 40, 20, 30]

numbers.__reversed__()

print("reversed list:", numbers)

#16
numbers = [10, 50, 30, 80, 20]

largest = max(numbers)

print("Largest number:", largest)

#17
list1=[60,50,20,50]
list2=[12,11,20,60]
results=list1+list2
print("merged list:",result)

#18
numbers = [10, 20, 30, 40, 50]

print("Last element:", numbers[-1])

#19
numbers = [[10, 20], [30, 40], [50, 60]]

print("Element:", numbers[1][0])

#20
numbers = [10, 20, 10, 30, 10, 40]

count = numbers.count(10)

print("10 appears:", count, "times")

