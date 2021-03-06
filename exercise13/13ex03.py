#Tehtävä L13T03 
# Save info of ten cars. Print info.

#save cars to dictionary
car_info = {
    "ABC-123": "Volvo", 
    "CVB-567": "Audi",
    "BNM-456": "Audi",
    "SFF-355": "Opel",
    "RRY-686": "Opel",
    "TET-124": "Skoda", 
    "TTY-564": "Skoda",
    "YUY-898": "Lada",
    "FGH-346": "Mersu",
    "DHJ-456": "Audi",
}
    


#print unsorted car info

print("Not sorted: ")
for brand, licence in car_info.items():
    print(brand,licence)
sorted_brand = sorted(car_info.items(), key = lambda kv: kv[1])
sorted_brand = dict(sorted_brand)

#print car info sorted by brand

print("Sorted by brand: ")
for brand, licence in sorted_brand.items():
    print(brand,licence)
sorted_licence = sorted(car_info.items(), key = lambda kv: kv[0])
sorted_licence = dict(sorted_licence)

#print car info sorted by licence

print("Sorted by licence: ")
for brand, licence in sorted_licence.items():
    print(brand,licence)