#Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen. 
#Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.

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