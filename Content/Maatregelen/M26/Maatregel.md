## M26: Het project laat de beveiliging van het ontwikkelde product periodiek beoordelen

#include "Content/Maatregelen/M26/Definitie.md"

Software wordt minimaal bij iedere grote release of ten minste twee keer per jaar onderworpen aan een beveiligingstest door beveiligingsexperts die ICTU daarvoor inhuurt. Op basis van documentatie en architectuurstudie, crystalbox security audits (broncodescan) en penetratieaudits beoordelen deze experts of de software voldoet aan de projectspecifieke niet-functionele eisen met betrekking tot beveiliging, of bekende kwetsbaarheden (zoals bijvoorbeeld in de OWASP Top 10 genoemd) vermeden zijn en in hoeverre voldoende invulling gegeven is aan de normen vanuit die vanuit BIO en SSD gelden.

ICTU zorgt ervoor dat de benodigde expertise op afroep beschikbaar gesteld kan worden aan projecten.

Indien door de opdrachtgever gewenst, kunnen securitytesten door een onafhankelijke derde partij worden uitgevoerd in een daarvoor door de opdrachtgever beschikbaar gestelde omgeving. Dit kan zowel incidenteel als structureel worden ingericht. Afspraken hierover worden bij voorkeur al in de voorbereidingsfase gemaakt.

De beveiligingstesten vinden plaats in aanvulling op de door tools uitgevoerde continue beveiligingsanalyse van de gerealiseerde software. Bevindingen uit zowel een beveiligingstest als de continue analyse worden in Jira als issue - gemarkeerd als beveiligingsbugreport - vastgelegd op de backlog van het project.

### Rationale

Door het inschakelen van actuele, specifieke expertise wordt de kans vergroot dat eventuele kwetsbaarheden in de gerealiseerde software tijdig herkend worden.

### Referenties

Zie ook:

* {{M05}}
* {{M16}}
