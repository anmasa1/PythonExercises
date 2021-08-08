#Mäkihypyssä käytetään viittä arvostelutuomaria. Kirjoita ohjelma, 
#joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten, 
#että summasta on vähennetty pois pienin ja suurin tyylipiste.

i = 0; 
list = []

while i < 5:

   point = int(input("Give points: "))
   list.append(point)
  
   i += 1   
list2 = sorted(list)
list3 = list2[1:4]
#print(list3)
print("Total points are",sum(list3))
