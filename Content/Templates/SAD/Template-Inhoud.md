# Ontwerpbeslissingen

{Dit hoofdstuk bevat een aantal veelgebruikte ontwerpbeslissingen. Waar nodig moeten ze worden aangevuld of aangepast.}

## Ontwerpprincipes

Hieronder volgt een aantal ontwerpprincipes die binnen software engineering als best practice gelden. Sommige principes, zoals "Abstractie", worden afgedwongen door het gebruik van de gangbare API’s en standaardcomponenten; andere principes spelen een rol bij het ontwerp en de implementatie van de applicatie en worden expliciet getoetst door de SIG/TÜViT-richtlijnen voor onderhoudbaarheid van de software en continu geëvalueerd door het kwaliteitssysteem.

* **Eenvoud**: Software die simpel en begrijpelijk is, is beter onderhoudbaar, overdraagbaar en uitbreidbaar. Dit is een principe waaruit andere voortvloeien.
* **Modulariteit**: Software is op alle detailniveaus opgesplitst in zelfstandige modules (componenten), zodat de modules afzonderlijk aangepast en getest kunnen worden.
* **Abstractie**: Modules (componenten) zijn voorzien van een abstracte interface die beschrijft wat de module doet en hoe ermee gecommuniceerd kan worden, zodat de modules kunnen samenwerken zonder dat er een rechtstreekse afhankelijkheid ontstaat. Met andere woorden: interface en implementatie zijn van elkaar gescheiden en onderdelen zijn alleen afhankelijk van de interfaces.
* **Low coupling, high cohesion**: Modules zijn zo onafhankelijk van elkaar als mogelijk (low coupling); de interne onderdelen van een module hebben juist een grote samenhang (high cohesion). Low coupling zorgt ervoor dat modules individueel gewijzigd kunnen worden zonder negatieve effecten op de rest van de applicatie, vergelijkbaar met Abstractie. High coupling verhoogt de eenvoud en de onderhoudbaarheid van de applicatie.
* **Separation of concerns**: Elke module heeft precies één taak of verantwoordelijkheid ("concern").

De term "module" hierboven is generiek bedoeld en duidt op alle vormen waarin delen van de software kunnen worden gebundeld, zoals componenten, klassen en methoden.

## Gelaagde applicatiearchitectuur

De applicatiearchitectuur van het systeem is gebaseerd op de onderstaande lagen. Elke component maakt onderdeel uit van precies één laag.

1. Presentatielaag: deze laag is verantwoordelijk voor de presentatie van informatie aan de eindgebruiker. {Eventueel opsomming van componenten uit deze laag.}
2. Applicatie-serviceslaag: deze laag bevat de businesslogica. {Eventueel opsomming van componenten uit deze laag.}
3. Technische-serviceslaag: deze laag bevat de ondersteunende technische services. {Eventueel opsomming van componenten uit deze laag.}
4. Datalaag of gegevenslaag: deze laag is verantwoordelijk voor de opslag van gegevens. {Eventueel opsomming van componenten uit deze laag.}

Componenten uit een laag mogen alleen componenten uit dezelfde of een diepere laag (een laag met een hoger nummer in de opsomming) gebruiken. Het is niet noodzakelijk dat dit de direct onderliggende laag is, als er redenen zijn om een laag "over te slaan".

## Gebruik van bewezen componenten en standaarden

{De applicatie} is gebaseerd op industriestandaarden {opsomming van standaarden}. Om deze standaarden te implementeren gebruikt {de applicatie} gangbare componenten en bibliotheken, bij voorkeur die onderdeel uitmaken van beheerde platformen. Gebruik van gangbare, bewezen en actief onderhouden componenten verlaagt de beheerlast op langere termijn; gebruik van beheerde en volwassen componenten verlaagt beveiligingsrisico's.

De toegankelijkheid van de applicatie voldoet aan de WCAG 2.1 (Web Content Accessibility Guidelines).

## Gebruik van gangbare security-ontwerpprincipes

{De Applicatie} maakt gebruik van de volgende gangbare security-ontwerpprincipes:

* **Least common mechanism**: Minimaliseer gedeelde resources tussen verschillende functies of gebruikers.
* **Least privilege**: Ken de minimale rechten toe die nodig zijn voor de adequate uitvoering van elke rol en taak.
* **Complete mediation**: Controleer de rechten voor elke toegang tot een object.

## Gebruiker beslist

In situaties waarin het niet op voorhand duidelijk is wat de correcte reactie van de applicatie is, wordt de keus aan de gebruiker gelaten. Een voorbeeld is het langdurig uitblijven van een reactie bij opvragen van gegevens: bij het bereiken van de ingestelde maximale wachttijd, krijgt de gebruiker de mogelijkheid om de betreffende actie nogmaals uit te voeren.

# Applicatiecontext

{Beschrijf in dit hoofdstuk de technische context waarbinnen de applicatie zal opereren. Indien deze informatie al in de PSA of ander document beschreven staan kan dit hoofdstuk weggelaten worden.}

## Omliggende systemen

### Management & control

### Softwareprovisioning

### Identity- en authorization-provisioning

### Dataprovisioning

### Logging & auditing

### Backup & recovery

## Gebruikerssystemen

## Externe systemen

# Applicatiearchitectuur

## Componenten

{Figuur met alle componenten}

### Webserver

### Directoryserver

### Functieservices

## Logische View - Dynamisch

### Use cases

{Beschrijf hier alleen de voor de architectuur significante use cases. Verwijs voor de uitwerking van deze use cases en de overige use cases naar het GFO. Gebruik hier dezelfde ids en namen voor de use cases als in het GFO.}

# Informatiearchitectuur

## Uitwisseling van gegevens met externe systemen

### Koppelvlak {identiteiten- en autorisatiessysteem}

### Koppelvlak {naam 1}

### Koppelvlak {naam 2}

## Conceptueel gegevensmodel

## Conceptueel gegevensmodel metadata

## Logginginformatie

### Technische (applicatie)log

### Berichtenlog

### Audit log

### Performance log

# Deployment view

# Implementatieview

## Scope

Dit hoofdstuk beschrijft de algemene richtlijnen voor de implementatie van {de applicatie} en de belangrijkste aspecten met betrekking tot de realisatie van de componenten.

## Implementatierichtlijnen

### Programmeertaal en programmeeromgeving

Criteria voor de keuze van een programmeertaal voor de implementatie zijn:

1. De programmeertaal moet toekomstvast en gangbaar zijn.
2. De programmeertaal en run-timeomgeving kennen een redelijke mate van onafhankelijkheid van het onderliggend besturingssysteem.
3. Het totale softwareplatform met gebruikte tooling moet eenvoudig over te zetten zijn naar een andere leverancier.

### Technische applicatielogging

### Gebruik van exceptions

### Gebruik van transacties

### Gebruik van threads en processen

### Toepassing van frameworks en libraries

### Coding rules

## Implementatietechnologie

### Besturingssysteem en middleware

### Applicatiecode

### Testcode

## Voortbrengingsproces

## Kwaliteitsstraat

## Omgevingen

## Componenten – Implementatieview

# Security view

## Inleiding

Dit hoofdstuk vat de technische beveiliging van {de applicatie} samen. De maatregelen zijn gegroepeerd naar systeemfunctie en voorzien van verwijzingen naar maatregelen in de risicoanalyse ({referentie}) en het informatiebeveiligingsplan ({referentie}).

## Gegevensbeveiliging tijdens transport

| Nr | Technische maatregel | Relatie IB-plan |
|:---|:---------------------|:----------------|
| 1  | {maatregel}          | {relatie}       |

## Gegevensbeveiliging opgeslagen gegevens

| Nr | Technische maatregel | Relatie IB-plan |
|:---|:---------------------|:----------------|
| 1  | {maatregel}          | {relatie}       |

## Authenticatie en autorisatie

| Nr | Technische maatregel | Relatie IB-plan |
|:---|:---------------------|:----------------|
| 1  | {maatregel}          | {relatie}       |

## Auditing en accounting

| Nr | Technische maatregel | Relatie IB-plan |
|:---|:---------------------|:----------------|
| 1  | {maatregel}          | {relatie}       |

## Richtlijnen

Bij de ontwikkeling van de programmatuur worden de volgende richtlijnen in acht genomen:

* [OWASP Top-10](https://owasp.org/www-project-top-ten/),
* [NCSC ICT-beveiligingsrichtlijnen voor webapplicaties](https://www.ncsc.nl/documenten/publicaties/2019/mei/01/ict-beveiligingsrichtlijnen-voor-webapplicaties).
* [Baseline Informatiebeveiliging Overheid (BIO)](https://bio-overheid.nl/media/1572/bio-versie-104zv_def.pdf).
* [Software Development (SSD) van het Centrum Informatiebeveiliging en Privacybescherming](https://www.cip-overheid.nl/media/1101/grip-op-ssd-het-proces-v20.pdf)

## Overzicht van gebruikte certificaten

Certificaten (alle PKIoverheid):

1. {lijst van PKIoverheidcertificaten}

Certificaten van anderen:

1. {lijst van andere certificaten}

# Performance view

## Inleiding

Dit hoofdstuk vat de performancekarakteristieken van {de applicatie} samen en beschrijft hoe de benodigde throughput, response tijden en schaalbaarheid bereikt zullen worden.

## Belasting

{Beschrijf of verwijs naar de verwachte belasting van het systeem: aantallen gebruikers, aantallen transacties, hoeveelheden te bewaren data, etc.}

## Snelheid (time behavior)

{Beschrijf hoe de applicatie de gewenste response tijden en throughput gaat realiseren}

## Middelen beslag (resource utilization)

{Beschrijf welke en hoeveel middelen (denk aan storage, bandbreedte, rekencapaciteit) nodig zijn voor de vereiste performance}

## Schaalbaarheid

{Beschrijf hoe de applicatie horizontaal danwel verticaal schaalbaar is}

# {Overige architectureel-significante niet-functionele eigenschappen}

{Voeg indien nodig hoofdstukken toe voor andere architectuureel-significante niet-functionele eigenschappen van de applicatie}
