#Tee luokka Cat. Tee luokalla on kaksi ominaisuutta name ja color, sekä yksi metodi miau.
#Luo Cat-luokasta vähintään kaksi erilaista kissa-oliota. 
#Näytä kissa-olioiden ominaisuudet konsolille, laita kissat myös naukumaan.

class Cat:
    name = ""
    color = ""

    def miau(self):
        print("Miau!")

katti1 = Cat()
katti1.name = "Viiru"
katti1.color = "red"

katti2 = Cat()
katti2.name = "Mikko"
katti2.color = "black"


print(katti1.name, "is",katti1.color,"and says: ")
katti1.miau()

print(katti2.name, "is",katti2.color,"and says: ")
katti2.miau()