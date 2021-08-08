firstname = input("Give your firstname: ")
lastname = input("Give your lastname: ")
namelenght = str(len(firstname))
print(namelenght)
pituus = int(namelenght)
letter = firstname[0]


i=0
for i in range(pituus):
        print (letter, end=" ")


txt = lastname[::-1]
print(txt)
        
        