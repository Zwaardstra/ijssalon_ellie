from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    actieprijs = prijs * (1- korting)
    actie_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {actieprijs} euro."
    return actie_tekst

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for inkomst in inkomsten:
        totaal += inkomst
    btw_bedrag = totaal * btw
    totaal_tekst = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden"
    return totaal_tekst

def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    MinMax = [laag, hoog]
    return MinMax

def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst)/len(mijn_lijst)
    gem_tekst = f"De gemiddelde inkomsten deze week zijn {gem} euro"
    return gem_tekst

def meervoudig(invoer_lijst):
    waardes = laag_en_hoog(invoer_lijst)
    return waardes

def combinatie(invoer_lijst_2):
    laag, hoog = laag_en_hoog(invoer_lijst_2)
    combiwaarde = mijn_functie_2(hoog,laag)
    return combiwaarde
    





