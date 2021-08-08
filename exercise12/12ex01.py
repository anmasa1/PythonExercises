#Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. 
#Luo Human-luokasta kaksi olioita, joitten arvot asetat. Tulosta olioiden tiedot konsolille

class Human:
    name = ""
    age = 0

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

print(man.show_info())
print(woman.show_info())
