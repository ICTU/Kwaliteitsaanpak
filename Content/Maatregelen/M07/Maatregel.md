## M07: Het project gebruikt een continuous delivery pipeline met vaste onderdelen

#include "Content/Maatregelen/M07/Definitie.md"

Niet alle testen en controles kunnen altijd geautomatiseerd worden uitgevoerd. Denk aan kwaliteitscontroles op architectuurbeslissingen of het testen van toegankelijkheidseisen. Waar mogelijk wordt wel een groot mogelijk deel van de testen en controles geautomatiseerd en als onderdeel van de pipeline uitgevoerd.

ICTU voorziet door middel van de afdeling ISR in mensen en hulpmiddelen, zodat projecten deze pipeline kunnen toepassen. Projecten zijn verantwoordelijk voor de correcte werking van de pipeline.

ICTU gebruikt Jenkins of TFS (Team Foundation Server) als tool voor de implementatie van de continuous delivery pipeline. De ICTU Release Manager ondersteunt de laatste stap (oplevering van het totale product).

### Rationale

Software incrementeel opleveren vereist dat de software frequent gebouwd, getest en opgeleverd kan worden. Om dit efficiënt en foutvrij te doen, dient het proces van bouwen, testen en opleveren geautomatiseerd te zijn; een continuous delivery pipeline faciliteert dit.

### Referenties

Zie ook:

* {{M05}}
