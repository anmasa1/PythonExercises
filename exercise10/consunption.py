# call function calc_consumtion

from utils import calc_consumption

fuelcon = int(input("What is the fuel consumption for 100 km? "))
fuel_price = int(input("How much does the fuel costs per litre? "))
trip = int(input("What is the travel distance? "))

travel_info1, travel_info2 = calc_consumption(fuelcon, fuel_price, trip)
print("Fuel consumpition is", travel_info1,"(l) and price of the fuel ",travel_info2, "(€)" )
