from database import Student

try:
    name = input("Enter Name\n")
    phone = input("Enter Phone\n")
    age = input("Enter Age\n")
    gender = input("Enter Gender\n")
    code = input("Enter student's code\n")

    Student.create(name=name, phone=phone, age=age, gender=gender, studentcode=code)
    print("Student registered successfully")

except:
    print("Failed to register student")
