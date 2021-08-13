#Tehtävä L13T01 Tehtävä B
# Print a deck of cards

i = 0; 
number = 0
cards = []


while i < 13:

   land = "harts" 
   number += 1
   luku = str(number)
   card = "harts "+ luku   
   cards.append(card)
   i += 1   

i = 0; 
number = 0

while i < 13:

   land = "diamonds" 
   number += 1
   luku = str(number)
   card = "diamonds "+ luku   
   cards.append(card)
   i += 1   

i = 0; 
number = 0

while i < 13:

   land = "spade" 
   number += 1
   luku = str(number)
   card = "spade "+ luku   
   cards.append(card)
   i += 1   

i = 0; 
number = 0

while i < 13:

   land = "clubs" 
   number += 1
   luku = str(number)
   card = "clubs "+ luku   
   cards.append(card)
   i += 1   

print(cards)

#Tehtävä L13T02 Tehtävä B

#shuffle deck of cards

import random


random.shuffle(cards)
print(cards)