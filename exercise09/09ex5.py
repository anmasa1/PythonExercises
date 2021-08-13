#Tehtävä L09T05
# Print lottery numebers

from random import randint

lotto = []
while len(lotto) < 7:
    new_number = randint(1, 40)
    if new_number not in lotto:
        lotto.append(new_number)

print(lotto)