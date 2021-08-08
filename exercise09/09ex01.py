#Tehtävä L09T01


#Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän. Sademäärä annetaan kokonaislukuna, 
#jollei kyseisenä päivänä ole satanut käyttäjä antaa luvuksi 0. Laske ja näytä viikon kokonaissademäärä.




rain = 0

i = 0; # kierrosmuuttuja
while i < 7:

   rain = int(input("Give days rainfall: ")) + rain
   i += 1   # tarkoittaa samaa kuin i = i+1;
print("Weeks rainfall is",rain," mm.")