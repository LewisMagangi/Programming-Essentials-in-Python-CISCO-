def liters_100km_to_miles_gallon(liters):
    gallons = 0
    miles = 100 / 1.609344              #kilometres to miles
    gallons = liters / 3.785411784      #liters to gallons
    return (miles / gallons) 

def miles_gallon_to_liters_100km(miles):
    gallons = 1
    kilometres = miles * 1.609344       #miles to kilometres
    liters = gallons * 3.785411784      #litres to gallons
    return ((100 * (liters / kilometres))) 

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))