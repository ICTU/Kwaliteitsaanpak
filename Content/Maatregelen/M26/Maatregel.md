## $M26$

#include "Content/Maatregelen/M26/Definitie.md"

Software wordt minimaal bij iedere grote release of ten minste twee keer per jaar onderworpen aan een beveiligingstest door beveiligingsexperts die ICTU daarvoor inhuurt. Op basis van documentatie en architectuurstudie, crystalbox security audits (broncodescan) en penetratieaudits beoordelen deze experts of de software voldoet aan de projectspecifieke niet-functionele eisen met betrekking tot beveiliging, of bekende kwetsbaarheden (zoals bijvoorbeeld in de OWASP Top-10 genoemd) vermeden zijn en of voldoende invulling gegeven is aan de normen die vanuit BIO en SSD gelden. Penetratietesten op de software vinden plaats in de testomgeving van het project. Als ICTU verantwoordelijk is voor het operationeel beheer laat ICTU de penetratietesten op de software (ook) uitvoeren in een productie-like omgeving.

ICTU zorgt ervoor dat de benodigde expertise op afroep beschikbaar gesteld kan worden aan projecten.

De opdrachtgevende organisatie kan een derde partij opdracht geven beveiligingstesten uit te voeren in een daarvoor door de opdrachtgevende organisatie beschikbaar gestelde omgeving. Dit kan zowel incidenteel als structureel worden ingericht. Als de opdrachtgevende organisatie dit structureel inricht en als deze beveiligingstesten voldoen aan de eisen die het project zou stellen, dan kunnen de opdrachtgevende organisatie en het project besluiten dat het project zelf geen beveiligingstesten laat uitvoeren. Afspraken hierover worden bij voorkeur al in de voorfase gemaakt, inclusief een controle dat de opdrachtgevende organisatie de benodigde contractuele mogelijkheden heeft beveiligingstesten uit te besteden. Het project ontvangt in dat geval de beveiligingstestrapportages van de opdrachtgevende organisatie.

De beveiligingstesten vinden altijd plaats in aanvulling op de door tools uitgevoerde continue beveiligingsanalyse van de gerealiseerde software. Bevindingen uit beveiligingstesten en de continue analyse die niet direct worden opgelost, worden in Jira als issue vastgelegd op de product backlog.

De kwaliteitsmanager van het project bewaakt de opvolging van de kritische beveiligingsissues. De kwaliteitsmanager bewaakt tevens of de beveiligingstesten voldoende frequent plaatsvinden, bij voorkeur door Quality-time te laten waarschuwen als het tijd is voor de volgende beveiligingstest.

### Rationale

Het inschakelen van actuele, specifieke expertise vergroot de kans dat eventuele kwetsbaarheden in de gerealiseerde software tijdig herkend worden.
