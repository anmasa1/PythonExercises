#Tehtävä L09T02

# Count sum of the given numbers, an empty space terminates the loop.

i = 0
sum = 0
while True:
    number = input("Enter a number:")
    if number == "": 
        print("An empty space terminated the loop.")
        print("You gave", i ,"numbers. The sum is", sum,".")
        break
    i += 1
    sum = int(number)+sum
    
