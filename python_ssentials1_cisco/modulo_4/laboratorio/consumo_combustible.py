#crea un algoritmo que calcule el consumo de galones y convierta cantidad consumida por galon a millas por galon y vice versa


gallon_liters = 3.785411784
milla_meters = 1609.344

def liters_100km_to_miles_gallon(liters):

    liters_gallon = liters/gallon_liters
    miles = 100 * 1000 / milla_meters
    return miles / liters_gallon
def miles_gallon_to_liters_100km(miles):


    meters_miles = milla_meters*miles

    liters_100km = meters_miles/100000
    return gallon_liters/liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))