#Tehtävä L14T02
# read C: and try add file to C

import os

c_dir = os.listdir("/")
  
print("Files and directories in '", c_dir, "' :") 
  
# print the list
print(c_dir)

#can't add file to C, in Linux might succeed as root user

try:
   filename = "ayho.txt"
   file = open("C:\\" + filename, "w")
   file.write("Creating a file with Python!")
   file.close()
except:
    print("Failed to create file to drive root")
