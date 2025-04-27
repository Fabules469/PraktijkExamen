""" Het programma berekent de pensioenleeftijd en het pensioenbedrag van een werknemer."""

lijst_werkstatuut = ["medewerker", "zelfstandige", "ambtenaar"]

def bereken_pensioenleeftijd(leeftijd, werkstatuut):
    """Berekend de pensioenuitkering op basis van de leeftijd en het werkstatuut."""
    if werkstatuut == "medewerker":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 350
            uitv_1 = f"Je krijgt € {week_uitkering} per week."
        elif leeftijd > 70:
            week_uitkering = 350 + 20 #extra toeslag medewerker voor ouderen
            uitv_1 = f"Je krijgt € {week_uitkering} per week."
    if werkstatuut == "zelfstandige":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 300
            uitv_1 = f"Je krijgt € {week_uitkering} per week."
        elif leeftijd > 70:
            week_uitkering = 300 + 15 #extra toeslag zelfstandige voor ouderen
            uitv_1 = f"Je krijgt € {week_uitkering} per week."
    if werkstatuut == "ambtenaar":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 370
            uitv_1 = f"Je krijgt € {week_uitkering} per week."
        elif leeftijd > 70:
            week_uitkering = 370 + 25 #extra toeslag ambtenaar voor ouderen
            uitv_1 = f"Je krijgt € {week_uitkering} per week."
    if werkstatuut in lijst_werkstatuut:
        if leeftijd >= 18 and leeftijd < 65:
            leeftijd_verschil = 65 - leeftijd
            uitv_1 = f"Van werken word je gelukkig, je mag nog {leeftijd_verschil} jaar genieten van je baan."
    
    return uitv_1   
        
""" verzoek tot invoer."""   
print("Wat is je leeftijd?")
leeftijd = int(input("Voer het aantal jaren in: "))
print("Wat is je werkstatuut?")
werkstatuut = input("Voer in: medewerker, zelstandige of ambtenaar: ").lower()

uitvoer = bereken_pensioenleeftijd(leeftijd, werkstatuut)
print(uitvoer[0:])

