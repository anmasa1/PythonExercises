#Tehtävä L09T03
# Print square of the given number in a loop

a = int(input("Enter a number between 1-10:"))

for i in range(1,a+1):
    square = i*i
    print("Number" ,i,"square is", square,i)

