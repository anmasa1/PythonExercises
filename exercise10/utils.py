#Tehtävä L10T01 

#function show_info
def show_info():
    print("I'm Utils.Info")

#show_info()

#Tehtävä L10T02
# returns subraction of number1 and number2

def subtract(number1, number2):
    return number1 - number2

number = subtract(10, 5)
print("subtraction returned ", number)

#Tehtävä L10T03
# returns averege of the tree numbers

def average(num1,num2,num3):
    return (num1 + num2 +num3)/3
    

result = average(8,2,5)
print("average returned ", result)

#Tehtävä L10T04

#returns fuel consumption and price of the used fuel

def calc_consumption(consumption, price, distance):
    fuel = (consumption/100) * distance
    fuelprice = fuel * price
    return fuel, fuelprice
    


