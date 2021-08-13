#Tehtävä L11T02

#Create class Human, class has to objects

class Human:
    name = ""
    age = 0

#Function show_info returns name and age
    def show_info(self):
        info_name = self.name 
        info_age = self.age
        return info_name, info_age


man = Human()
man.name = "Kalle"
man.age = 20

woman = Human()
woman.name = "Kaisa"
woman.age = 21

#call function show_info
print(man.show_info())
print(woman.show_info())
