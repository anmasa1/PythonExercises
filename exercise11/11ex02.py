#Tee ohjelma, joka kysyy käyttäjältä ensin muutetaanko fahrenheitit celsiuksiksi vai celsius-asteet fahrenheitiksi. 
#Tämän jälkeen kysytään käyttäjältä asteet ja muutetetaan ne toisiin asteisiin ja näytetään tulos käyttäjälle.

#°C = (°F − 32) / 1,8
def f_to_c(value1):
    return ((value1-32) / 1.8)

#°F = (°C) · 1,8 + 32
def c_to_f(value3):
    return (value3 * 1.8) + 32

    


choice = input("Type 1 if you want to change Fahrenhait to Celsius or 2 if Celsius to Fahrenhait ")

if choice == "1":
    value2 = int(input("give °F degree:"))
    fahrenhait = f_to_c(value2)
    print(fahrenhait)

elif choice == "2":
    value4 = int(input("give °C degree:"))
    celsius = c_to_f(value4)
    print(celsius)

else:
    print("You didn't type 1 or 2")
