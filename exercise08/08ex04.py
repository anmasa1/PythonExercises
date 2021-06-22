#Tehtävä L08T04

points = int(input("Give points"))

if points >= 0 and points < 2:
    print("Grade is 0")
elif points >= 2 and points <= 3:
    print("Grade is 1")
elif points >= 4 and points <= 5:
    print("Grade is 2")
elif points >= 6 and points <= 7:
    print("Grade is 3")
elif points >= 8 and points <= 9:
    print("Grade is 4")
elif points >= 10 and points <= 12:
    print("Grade is 5")
