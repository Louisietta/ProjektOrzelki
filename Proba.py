przepisy = {
    "Spaghetti bolońskie": {"makaron", "mięso mielone", "sos pomidorowy", "cebula", "czosnek"},
    "Naleśniki": {"mąka", "mleko", "jajka", "masło"},
    "Pizza": {"mąka", "sos pomidorowy", "ser", "szynka"},
    "Gołąbki": {"mięso mielone", "sos pomidorowy", "ryż", "kapusta"},
    "Zupa pomidorowa": {"bulion", "pomidory", "śmietana", "ryż"},
    "Omlet": {"jajka", "szynka", "masło", "mleko"},
    "Sałatka Cezar": {"sałata", "parmezan", "kurczak", "czosnek"},
    "Jajecznica": {"jajka", "sól", "pieprz", "masło"}
}

def znajdz_przepis(dostepne_składniki):
    mozliwe_przepisy = []
    for nazwa_przepisu, skladniki in przepisy.items():
        if dostepne_składniki.issuperset(skladniki):
            mozliwe_przepisy.append(nazwa_przepisu)
    return mozliwe_przepisy

dostepne_skladniki = set(input("Wpisz składniki po przecinku: ").lower().split(", m"))

mozliwe_przepisy = znajdz_przepis(dostepne_skladniki)
if mozliwe_przepisy:
    print("Możesz zrobić następujące przepisy:", ", ".join(mozliwe_przepisy))
else:
    print("Nie znaleziono przepisów")