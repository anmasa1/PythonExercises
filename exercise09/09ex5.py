from random import randint

rivi = []
while len(rivi) < 7:
    uusi = randint(1, 40)
    if uusi not in rivi:
        rivi.append(uusi)

print(rivi)