#Tehtävä L10T01 

def show_info():
    print("I'm Utils.Info")

show_info()

#Tehtävä L10T02

def subtract(number1, number2):
    return number1 - number2

number = subtract(10, 5)
print("subtract returned ", number)

#Tehtävä L10T03

def average(num1,num2,num3):
    return (num1 + num2 +num3)/3
    

result = average(8,2,5)
print("average returned ", result)

#Tehtävä L10T04

def calc_consumption(consumption, price, distance):
    fuel = (consumption/100) * distance
    fuelprice = fuel * price
    return fuel, fuelprice
    


