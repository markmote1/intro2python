def calculate_bmi():
    weight = float(input("Enter weight in Kgs"))
    height = float(input("Enter height metres"))
    bmi = weight / (height * height)
    print(f"Your BMI is {bmi}")


calculate_bmi()
