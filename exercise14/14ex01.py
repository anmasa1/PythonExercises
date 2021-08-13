#Tehtävä L14T01
# try change name that is out of index
try:
    names = [ "Aatu", "Eetu", "Anu", "Mia"]
    names[5] = input("Change last nimi: ")
    print("Changed name is ", names[5])
except IndexError:
    print("Wrong index used in accessing list")
print(names)
