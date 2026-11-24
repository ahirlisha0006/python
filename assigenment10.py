#1
file = open("demo.txt","r")
content =file.read()
print(content)
file.close()
#2
file =open("demo.txt","r")
lines= file.readlines()
print("number of lines:",len(lines))
file.close
#3
file = open("demo.txt", "r")

text = file.read()

words = text.split()

count = {}

for word in words:
    word = word.lower()
    count[word] = count.get(word, 0) + 1

print(count)

file.close()
#4
file = open("sentences.txt", "w")

for i in range(5):
    sentence = input("Enter a sentence: ")
    file.write(sentence + "\n")

file.close()

print("Sentences saved successfully")
#5
file =open("demo.txt","a")
words =["banana\n","applie\n"]
file.writelines(words)
file.close()
print("data added")
#6
word = input("Enter word to search: ")

file = open("demo.txt", "r")

for line in file:
    if word.lower() in line.lower():
        print(line, end="")

file.close()
#7
file = open("demo.txt", "r")

text = file.read()

file.close()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

text = text.replace(old_word, new_word)

file = open("demo.txt", "w")

file.write(text)

file.close()

print("Word replaced successfully")
#8

file1 = open("demo.txt", "r")
data1 = file1.read()
file1.close()


file2 = open("sentence.txt", "r")
data2 = file2.read()
file2.close()


file3 = open("merged.txt", "w")
file3.write(data1 + "\n" + data2)
file3.close()

print("Files merged successfully")
#9
import csv

file = open("students.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(" | ".join(row))

file.close()
#10
file1 = open("demo.txt", "r")

data = file1.read()

file1.close()

file2 = open("backup.txt", "w")

file2.write(data)

file2.close()

print("Backup created successfully")