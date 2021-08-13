#Tehtävä L11T04
# Ask points from five judges. Removes the highest and lowest points. 
# Prints the sum of the rest.

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
