# Tehtävä L14T04

#Create funktion isthiszero.
#I get ValueError when input is not int


def isthiszero(num):
    
    if num == 0:
        return True
    if num != 0:
        return False

try:
    number = int(input("Give a number: "))
    number2 = isthiszero(number)
    print(number2)
except ValueError:
    print("You didn't give a number")