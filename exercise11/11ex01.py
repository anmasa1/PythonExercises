#Tehtävä L11T01
#Change time given in seconds to hh:mm:ss

seconds = int(input("Give time in seconds: "))

hours = seconds // 3600
extraseconds = seconds % 3600
minutes = extraseconds // 60
seconds2 = extraseconds % 60
    
print("Time is", hours,":",minutes,":",seconds2)



 