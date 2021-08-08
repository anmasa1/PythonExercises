def calc_consumption(consumption, price, distance):
    fuel = (consumption/100) * distance
    fuelprice = fuel * price
    return fuel, fuelprice

