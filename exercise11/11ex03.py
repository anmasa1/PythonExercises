#Tehtävä L11T03
# Ask names and prints the names and the number of names. An empty space terminates the loop.

i = 0
sum = 0
name2 = ""
while True:
    name = input("Enter a name:")
    if name == "": 
        print("An empty space terminated the loop.")
        print("You gave", i ,"names.")
        break
    i += 1
    name2 = name + ", " +name2
   
print(name2)