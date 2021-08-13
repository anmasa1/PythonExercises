#Tehtävä L15T02
#read names.txt and add names to namelist

try:
    filename = "names.txt"
    names = open(filename, "r")
    line = names.readline()
    namelist = []
    while line != "":
        line = line.rstrip()
        #print(line)
        namelist.append(line)
        line = names.readline()
    names.close()
except:
    print("Failed to read file: " + filename)



n = 0
name = namelist[n]
lkm = 0

#returns name and the times name appears in the list
def many_names(name1, name_times, y):
    i = 0
    m = 0
    times = 0
    while i < len(namelist):
            name = namelist[n]
            
            if name == namelist[m]:
                times += 1
                
            i += 1
            m += 1
    return name, times

tulos1, tulos2 = many_names(name, lkm, n)

try:

    n = 0
    namelist2 = []
    k = 0
    lenght = len(namelist)
    while k < (lenght):
        name = namelist[n]
        tulos1, tulos2 = many_names(name, lkm, n)
        result1 = str(tulos1) +" "+ str(tulos2)
        if result1 not in namelist2:
            namelist2.append(result1)
     
        lkm = 0
        m = 0
        k += 1
        n += 1 
    
    print(filename, "has",lenght, "names")
    print("Names appear in the file following way:")
    for name3 in namelist2:
        print(name3, "times")
    

# Tehtävä L15T03
# sort the namelist
    
    sorted_list = sorted(namelist)
    print("Names in alhapetical order:")
    for name4 in sorted_list:
        print(name4)
    
except:
    print("error")

   