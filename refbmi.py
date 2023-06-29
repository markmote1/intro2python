user_weight = input("Enter weight in kg")
weight = float(user_weight)
user_height = input("Enter height in meters")
height = float(user_height)
calc_bmi = weight/(height*height)
if calc_bmi < 18:
    print("Underweight")
elif 18.1 <= calc_bmi <= 29:
    print("Normal weight")
elif 29.1 <= calc_bmi <= 34:
    print("Overweight")
else:
    print("Obese")
