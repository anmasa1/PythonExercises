#Tehtävä L09T01

# Count weeks rainfall


rain = 0
rainfall = 0
i = 0

while i < 7:
   rain = int(input("Give days rainfall: "))
   i += 1  
   rainfall += rain
print("Weeks rainfall is",rainfall," mm.")