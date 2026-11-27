
import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()


# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
)
""")


# Insert student records
cursor.execute("DELETE FROM students")

students = [
    (1, "Harshada", "CSE", 2, 85),
    (2, "Riya", "IT", 3, 70),
    (3, "Mahi", "CSE", 2, 92),
    (4, "Liya", "ECE", 1, 65),
    (5, "Shiv", "CSE", 3, 78),
    (6, "Sanjay", "IT", 2, 95)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
    students
)


# 1. Display all student records
print("\n1. All Student Records")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())


# 2. Display only name and department
print("\n2. Name and Department")
cursor.execute("SELECT name, department FROM students")
print(cursor.fetchall())


# 3. Find students with marks greater than 75
print("\n3. Students with marks greater than 75")
cursor.execute("SELECT * FROM students WHERE marks > 75")
print(cursor.fetchall())


# 4. Display students from CSE department
print("\n4. CSE Department Students")
cursor.execute("SELECT * FROM students WHERE department = 'CSE'")
print(cursor.fetchall())


# 5. Sort students by marks (descending)
print("\n5. Students Sorted by Marks")
cursor.execute("SELECT * FROM students ORDER BY marks DESC")
print(cursor.fetchall())


# 6. Display top 3 scorers
print("\n6. Top 3 Scorers")
cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
print(cursor.fetchall())



conn.commit()
conn.close()
