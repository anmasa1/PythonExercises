#Tehtävä L15T05
# Save lottery numbers to a file

from random import randint

try:
    lotto1 = []
    lottofile = "lotto.txt"
    lotto = open(lottofile, "w")

    while len(lotto1) < 7:
        new_number = randint(1, 40)
        if new_number not in lotto1:
            lotto1.append(new_number)
            lotto.write(str(new_number)+",")
 

    print(lotto1)
    lotto.close()
except:
    print("Failed to read file: + ")