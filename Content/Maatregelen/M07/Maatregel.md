## M07: Het project gebruikt een continuous delivery pipeline om het product te bouwen, testen en op te leveren

#include "Content/Maatregelen/M07/Definitie.md"

De geautomatiseerde continuous delivery pipeline voert ten minste de volgende activiteiten uit:

1. Bouw van de software,
2. Unit tests,
3. Regressietests,
4. Beveiligingstests,
5. Performancetests,
6. Toegankelijkheidstests,
7. Broncodekwaliteitscontroles,
8. Installatie van de software,
9. Oplevering van het totale product, dus inclusief alle deliverables, in de vorm zoals bruikbaar voor en afgesproken met de opdrachtgever.

Performance- en beveiligingstests zijn ook onderdeel van de continuous delivery pipeline, maar vanwege doorlooptijden en licenties is dat niet altijd haalbaar; in dat geval vinden de performance- en beveiligingstests zo veel mogelijk, en bij voorkeur dagelijks, plaats.

Niet alle testen en controles kunnen altijd geautomatiseerd worden uitgevoerd. Denk aan kwaliteitscontroles op architectuurbeslissingen of het testen van toegankelijkheidseisen. Waar mogelijk wordt wel een zo groot mogelijk deel van de testen en controles geautomatiseerd en als onderdeel van de pipeline uitgevoerd.

ICTU voorziet door middel van de afdeling ISR in mensen en hulpmiddelen, zodat projecten deze pipeline kunnen toepassen. Projecten zijn verantwoordelijk voor de correcte werking van de pipeline.

ICTU gebruikt Jenkins of Azure DevOps (voorheen Team Foundation Server) als tool voor de implementatie van de continuous delivery pipeline. ISR biedt de projecten een voorziening om releases van het totale product van het total product veilig op te leveren aan opdrachtgevers en beheerpartijen.

### Rationale

Software incrementeel opleveren vereist dat de software frequent gebouwd, getest en opgeleverd kan worden. Om dit efficiënt en foutvrij te doen, dient het proces van bouwen, testen en opleveren geautomatiseerd te zijn; een continuous delivery pipeline faciliteert dit.

### Referenties

Zie ook:

* {{M05}}
