#Tehtävä L08T02
#Print largest number.

number1 = int(input("Give first number"))
number2 = int(input("Give second number"))
number3 = int(input("Give third number"))

if number1 >= number2 and number1 >= number3:
    print(number1)
elif number2 >= number1 and number2 >= number3:
    print(number2)
else:
     print(number3)