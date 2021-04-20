two_digit_number = (input("Digite um número de dois dígitos "))
print(type(two_digit_number))

soma = int(two_digit_number[0]) + int(two_digit_number[1])
print(type(soma))
print(soma)

num_char =  len(input("What is your name?"))
new_num_char = str(num_char)

print("Your name has " + new_num_char + " caracters.")

print(type(num_char))

a = float(123)
print(type(a))

print(str(70) + str(100))

print(2 ** 3)

#PEMDASL -> () ** * / + - left

print(3 * (3 + 3) / 3 - 3)

height = float(input("enter your height in meters:"))
weight = float(input("enter your weight in kg"))

bmi = round(weight / (height ** 2))
print(bmi)

print(round(8/3, 2))

score = 0

# User scores a point
score += 1
print(score)
height = 1.8
isWinning = True

print("your score is " + str(score))

# f-String
print(f"your score {score}, your height is {height}, your are winning is {isWinning}")












