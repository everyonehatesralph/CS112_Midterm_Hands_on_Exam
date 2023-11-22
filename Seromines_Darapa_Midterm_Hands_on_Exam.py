from random import randint

add_num1 = randint(0, 99)
add_num2 = randint(0, 99)

answer_addition = eval(input("What is " + str(add_num1) + "+" + str(add_num2) + " = "))
add = add_num1 + add_num2

if answer_addition == add:
    print("The answer is correct")
else:
    print("The answer is wrong")



sub_num1 = randint(0, 99)
sub_num2 = randint(0, 99)

answer_subtraction = eval(input("What is " + str(sub_num1) + "-" + str(sub_num2) + " = "))
sub = sub_num1 - sub_num2
if answer_subtraction == sub:
    print("The answer is correct")
else:
    print("The answer is wrong")



mul_num1 = randint(0, 99)
mul_num2 = randint(0, 99)

answer_multiplication = eval(input("What is " + str(mul_num1) + "*" + str(mul_num2) + " = "))
mul = mul_num1 * mul_num2
if answer_multiplication == mul:
    print("The answer is correct")
else:
    print("The answer is wrong")


div_num1 = randint(0, 99)
div_num2 = randint(0, 99)

answer_division = eval(input("What is " + str(div_num1) + "/" + str(div_num2 ) + " = "))
div = div_num1 / div_num2
div = round(div, 2)
if answer_division == div:
    print("The answer is correct")
elif div_num2 == 0:
    print("The divisor should not be equal to 0")
else:
    print("The answer is wrong")
