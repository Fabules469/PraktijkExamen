import keyword
""" Het programma berekent de pensioenleeftijd en het pensioenbedrag van een werknemer."""
week_uitkering = 0 #globale variabel
def bereken_pensioenleeftijd(leeftijd, werkstatuut):
    """Berekend de pensioenuitkering op basis van de leeftijd en het werkstatuut."""
    extra_per_week_1 = 20 #extra per week medewerker
    extra_per_week_2 = 15 #extra per week zelfstandige
    extra_per_week_3 = 25 #extra per week ambtenaar
    global week_uitkering
    if werkstatuut == "medewerker":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 350
            return week_uitkering
        elif leeftijd > 70:
            week_uitkering =  350 + extra_per_week_1
            return week_uitkering
    elif werkstatuut == "zelfstandige":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 300
            return week_uitkering
        elif leeftijd > 70:
            week_uitkering = 300 + extra_per_week_2
            return week_uitkering
    elif werkstatuut == "ambtenaar":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 370
            return week_uitkering
        elif leeftijd > 70:
            week_uitkering = 370 + extra_per_week_3
            return week_uitkering
        
""" verzoek tot invoer."""   
print("Wat is je leeftijd?")
leeftijd = int(input("Voer het aantal jaren in: "))
print("Wat is je werkstatuut?")
werkstatuut = input("Voer in: medewerker, zelstandige of ambtenaar: ").lower()

uitvoer = bereken_pensioenleeftijd(leeftijd, werkstatuut)
print(f"Je krijgt € {uitvoer} per week.")

