## $M07$

#include "Content/Maatregelen/M07/Definitie.md"

De geautomatiseerde continuous delivery pipeline voert ten minste de volgende activiteiten uit:

1. Bouw van de software,
2. Unit tests,
3. Regressietests,
4. Beveiligingstests,
5. Performancetests,
6. Toegankelijkheidstests,
7. Broncodekwaliteitscontroles,
8. Installatie van de software in test, acceptatie en/of productieomgevingen,
9. Oplevering van het totale product, dus inclusief alle deliverables, in de vorm zoals bruikbaar voor en afgesproken met de opdrachtgevende organisatie.

Performance- en beveiligingstests op de software zijn ook onderdeel van de continuous delivery pipeline, maar vanwege doorlooptijden en licenties is dat niet altijd haalbaar; in dat geval vinden de performance- en beveiligingstests zo veel mogelijk, en bij voorkeur dagelijks, plaats. Performance- en beveiligingstests op de software vinden plaats in de testomgeving van het project. Als ICTU verantwoordelijk is voor het operationeel beheer laat ICTU de performance- en beveiligingstesten op de software (ook) uitvoeren in een productie-like omgeving.

Niet alle testen en controles kunnen altijd geautomatiseerd worden uitgevoerd. Denk aan kwaliteitscontroles op architectuurbeslissingen of het testen van toegankelijkheidseisen. Waar mogelijk wordt wel een zo groot mogelijk deel van de testen en controles geautomatiseerd en als onderdeel van de pipeline uitgevoerd.

### Rationale

Software incrementeel opleveren vereist dat de software frequent gebouwd, getest en opgeleverd kan worden. Om dit efficiënt en foutvrij te doen, dient het proces van bouwen, testen en opleveren geautomatiseerd te zijn; een continuous delivery pipeline faciliteert dit.
