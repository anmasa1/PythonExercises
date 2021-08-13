try:
    filename = "lastnames.txt"
    lastnames = open(filename, "w")
    print("Anna tallennettavat nimet.")
    print("Lopeta tyhjalla rivilla.")
    line = input()
    while line != "":
        lastnames.write(line + "\n")
        line = input()
        
    lastnames.close()
    print("Names have been written to file", filename)
except OSError:
    print("Virhe tiedoston", filename, "kirjoittamisessa. Ohjelma paattyy.")

try:
    lastnames2 = open("lastnames.txt", "r")
    line2 = lastnames2.readline()
    while line2 != "":
        print(line2)
        line2 = lastnames2.readline()
    lastnames2.close()
except:
    print("Failed to read file: " + filename)

    


