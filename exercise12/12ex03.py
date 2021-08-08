#Autotallissasi on kolme autoa. Tee luokka Car. Tee luokalla on kolme ominaisuutta brand, model ja price. 
#Luo Car-luokasta vähintään kolme erilaista auto-oliota. Aseta autojen ominaisuudet seuraavasti:

#brand="Skoda" model="Octavia" price=3000
#brand="Audi" model="A4" price=4000
#brand="Volvo" model="V70" price=5000

#Tulosta kaikkien autotallin kolmen auton ominaisuudet konsolille.
#Laske myös autojen yhteishinta, ja näytä se konsolilla.
import random

class Car:
    brand = ""
    model = ""
    price = 0
    
    def __init__(self, brand="", model="", price=0):
        self.brand = brand
        self.model = model
        self.price = price
        
    def car_price(self):
        price1 = self.price
        return price1


 # override conversion from Vehicle to string with __str__       
    def __str__(self):
        return self.brand+ " " + self.model + ", " + str(self.price) + " €"


car1 = (Car("Skoda","Oktavia",3000)) 
car2 = (Car("Audi","A4",4000))
car3 = (Car("volvo","V70",5000))
print(car1)
print(car2)
print(car3)

print("Total price of all cars is: ",car1.car_price()+car2.car_price()+car3.car_price(), "€")

#Tehtävä L12T04


brans_list = ["Audi","BMW","Ford","Opel","Skoda","Volvo","VW"]
#print(brans_list)
#print(random.choice(brans_list))
#print(random.randint(1000, 10000))

all_cars = []
car4 = (Car(random.choice(brans_list),"",(random.randint(1000, 10000))))
car5 = (Car(random.choice(brans_list),"",(random.randint(1000, 10000))))
car6 = (Car(random.choice(brans_list),"",(random.randint(1000, 10000))))
car7 = (Car(random.choice(brans_list),"",(random.randint(1000, 10000))))
car8 = (Car(random.choice(brans_list),"",(random.randint(1000, 10000))))

all_cars.append(str(car4))
all_cars.append(str(car5))
all_cars.append(str(car6))
all_cars.append(str(car7))
all_cars.append(str(car8))




print(all_cars)
print("Total price of all added cars is: ",car4.car_price()+car5.car_price()+car6.car_price() +car7.car_price()+ car8.car_price(), "€")