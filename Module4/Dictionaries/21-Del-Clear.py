pol_swahili_dictionary = {
    "jumba": "castle",
    "maji": "water",
    "mchanga": "soil"
    }

def Printkeys(pol_swahili_dictionary):
    i = 1
    for item in pol_swahili_dictionary:
        print(i, ": ", item)
        i += 1

del pol_swahili_dictionary["maji"]    # remove an item
print("After using the del keyword :")    # outputs: 2
Printkeys(pol_swahili_dictionary) 
    
pol_swahili_dictionary.clear()   # removes all the items
print("After using the clear() method")    # outputs: 0
Printkeys(pol_swahili_dictionary)

print("The length of the dictionary is :", len(pol_swahili_dictionary))
print(pol_swahili_dictionary)
Printkeys(pol_swahili_dictionary)
 
del pol_swahili_dictionary   # removes the dictionary
try:
    Printkeys(pol_swahili_dictionary) 
except:
    print("pol_swahili_dictionary Not found") 
