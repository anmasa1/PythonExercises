#Tehtävä L13T01 Tehtävä B
i = 0; 
number = 0
cards = []


while i < 13:

   land = "hertta" 
   number += 1
   luku = str(number)
   card = "hertta "+ luku   
   cards.append(card)
   i += 1   

i = 0; 
number = 0

while i < 13:

   land = "ruutu" 
   number += 1
   luku = str(number)
   card = "ruutu "+ luku   
   cards.append(card)
   i += 1   

i = 0; 
number = 0

while i < 13:

   land = "pata" 
   number += 1
   luku = str(number)
   card = "pata "+ luku   
   cards.append(card)
   i += 1   

i = 0; 
number = 0

while i < 13:

   land = "risti" 
   number += 1
   luku = str(number)
   card = "risti "+ luku   
   cards.append(card)
   i += 1   

print(cards)

#Tehtävä L13T02 Tehtävä B

import random


random.shuffle(cards)
print(cards)