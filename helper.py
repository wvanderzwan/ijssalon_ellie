
def decoreer(tekst=""):
    tekst = "header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag,persoon):
    bedrag_pp = (bedrag/persoon)
    return (f"Het bedrag per persoon is {bedrag_pp} euro. ")


def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit


def som(naam_dictionary):
    som = sum(naam_dictionary.values())
    return som