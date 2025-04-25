""" Het programma berekent de pensioenleeftijd en het pensioenbedrag van een werknemer."""

week_uitkering = 0
def bereken_pensioenleeftijd(leeftijd, werkstatuut):
    """Berekend de pensioenuitkering op basis van de leeftijd en het werkstatuut."""
    extra_per_week_1 = 20
    extra_per_week_2 = 15
    extra_per_week_3 = 25
    global week_uitkering
    if werkstatuut == "medewerker":
        if leeftijd >= 65 and leeftijd <= 70:
            week_uitkering = 350
            return week_uitkering
        elif leeftijd > 70:
            week_uitkering =  350 + extra_per_week_1
            return week_uitkering
         
    

print("Wat is je leeftijd?")
leeftijd = int(input("Voer het aantal jaren in: "))
print("Wat is je werkstatuut?")
werkstatuut = input("Voer in: medewerker, zelstandige of ambtenaar: ").lower()

resultaat = bereken_pensioenleeftijd(leeftijd, werkstatuut)

""" Toon resultaat van de berekening. """
print(f"Je krijgt € {week_uitkering} per week.")


