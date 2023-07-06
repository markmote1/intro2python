from database import Student

students = Student.select()

for student in students:
    print(student.name, student.phone, student.age, student.gender, student.studentcode)
