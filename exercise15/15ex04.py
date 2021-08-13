#Tehtävä L15T04
#Ask user int and float numbers, save int numbers to int.txt filee
# and float numbers to float.txt file, end program if number is not int or float.

from os import close


try:
    filename1 = "int.txt"
    ints = open(filename1, "w")
    filename2 = "float.txt"
    floats = open(filename2, "w")
    number = input()

    while True:
    
        number = input("Give a number, int or float ")
       
        if number.isnumeric() == True:
            num1 = int(number)
            #print("int",num1)
            ints.write(str(num1) + "\n")

        elif "-" in number and "." not in number:
            num2 = int(number)
            #print("int",num1)
            ints.write(str(num2) + "\n")
            
        elif "." in number:
            num3 = float(number)
            #print("float",num2)
            floats.write(str(num3) + "\n")
    
        else:
            num4 = float(number)

    ints(close)
    floats(close)
except ValueError:
    print("You typed wrong type")