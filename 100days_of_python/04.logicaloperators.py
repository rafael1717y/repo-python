height = float(input("enter your height in meters:"))
weight = float(input("enter your weight in kg"))

bmi = round(weight / (height ** 2))
print(bmi)


if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are overweight')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')






"""
number = int(input("Which number do you want test? "))
if number % 2 == 0:
    print(f'{number} é par')
else:
    print(f'{number} é impar')
"""
