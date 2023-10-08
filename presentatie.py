mijn_dict = {"vis" : 10, "vlees" : 25, "overig" : 15}
totaal = 50

def presenteer(naam_dictionary,totaal):
    for k, v in naam_dictionary.items():
        print(k,":",v, "euro")

    totaal = totaal
    
    print(26 * "=")
    print(f"totaal : {totaal} euro")