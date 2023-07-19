#1.2
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

#1.3
aanbieding = prijzen["vanille"] * 0.8

#1.4
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
#print(reclame_tekst)
#print()

#1.5
""" 
Op het moment dat ik de "reclame_tekst" print krijg ik de waarde € 3.2 wat past bij de key "vanille" met value "4"
De € 2.4000000000004 in de opgave heeft als input value "3" van de key "aardbei"
Hieronder de versie betreft "aardbei".
"""

aanbieding1a = prijzen["aardbei"] * 0.8
reclame_tekst1a = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding1a}"
#print(reclame_tekst1a)
#print()

reclame_tekst2 = reclame_tekst1a[:63]
#print(reclame_tekst2)
#print()

#1.6
reclame_tekst3 = reclame_tekst2.upper()
#print(reclame_tekst3)
#print()

#1.7
reclame_tekst4 = reclame_tekst3.split()
#print(reclame_tekst4)
#print()

#1.8
# el = reclame_tekst4
#for i in el:
#    print(i)
#print()

#1.9
#el = reclame_tekst4
#for i in el:
#    print(i.lower())
#print()

#1.10

for el in reclame_tekst4:
    if (len(el))>4:
        print(el.upper())
    else:
        print(el.lower())
