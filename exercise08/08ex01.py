#Tehtävä L08T01
#Ask users age and prints users agegroup.

age = int(input("How old are you: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("Senior")