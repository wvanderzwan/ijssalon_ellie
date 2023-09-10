from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs * (1 - korting)} euro.")

aanbieding_1("aarbei", 4, 0.1)


"""
def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])
"""


def inkomsten_totaal(inkomsten, btw):
    print(f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {sum(inkomsten) * btw} euro btw betaald dient te worden.")

inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)


def hoog_en_laag(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

hoog_en_laag([220, 430, 125, 160, 205, 90, 345])


"""
def gemiddelde(mijn_lijst):
    import numpy
    return numpy.mean(mijn_lijst)

gemiddelde([220, 430, 125, 160, 205, 90, 345])
"""


def gemiddelde(mijn_lijst):
    import numpy
    print(f"De gemiddelde inkomsten deze week zijn {numpy.mean(mijn_lijst)} euro.")

gemiddelde([220, 430, 125, 160, 205, 90, 345])


"""
Numpy moet geïnstalleerd worden via de command in de terminal: pip install nympy
"""


def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

meervoudig([10,5,3,2,1,2,9])


def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return korte_lijst