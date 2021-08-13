#Tehtävä L14T04 
#Ask user in which indext to place a name. Inform user if it is out of range.

try:
    names = [ "Aatu", "Eetu", "Anu", "Mia", "Mika"]
    
    while True:
        i = int(input("Give index (number 0 - 4) for a new name: "))
        
        if i < 0 or i > 4:
            print("You gave wrong index.")
            continue
        new_name = names[i]
        names[i] = input("Give the new name: ")
        break
    print(names)
        
except IndexError:
    print("Wrong index used in accessing list")
