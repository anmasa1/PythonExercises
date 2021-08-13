#Tehtävä L09T04

# Print the first letter of the first name as many times as the lenght of the name is. 
# Reverse the lastname

firstname = input("Give your firstname: ")
lastname = input("Give your lastname: ")
namelenght = str(len(firstname))
#print(namelenght)
lenght = int(namelenght)
letter = firstname[0]

i=0

for i in range(lenght):
        print (letter, end=" ")

# reverse lastname
reversed = lastname[::-1]
print(reversed)
        
        