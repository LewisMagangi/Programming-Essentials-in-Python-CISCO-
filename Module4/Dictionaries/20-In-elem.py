pol_swahili_dictionary = {
    "jumba": "castle",
    "maji": "water",
    "mchanga": "soil"
    }

if "maji" in pol_swahili_dictionary:
    print("maji iko kwenye kamusi letu")
else:
    print("neno maji haiko kamusini")

print("Maneno kamusini ndio haya :")

global i
i = 1
    
for item in pol_swahili_dictionary:
    print(i, ": ", item)
    i += 1
