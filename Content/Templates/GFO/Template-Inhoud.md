# Functionele specificaties

De functionele specificaties zijn in de vorm van epics en user stories beschreven. Een user story is een korte beschrijving ("story") van wat een gebruiker ("user") wil. Een epic is een sprint-overstijgend, samenhangend geheel van user stories, dat als geheel waarde oplevert.

## Actoren

Een actor is een 'gebruiker' van het systeem; dit kunnen menselijke gebruikers zijn, maar ook andere systemen. Hierbij bestaat een onderscheid tussen interne en externe actoren.

| Actor   | Verantwoordelijkheid   | Intern of extern? |
|:--------|:-----------------------|:------------------|
| {actor} | {verantwoordelijkheid} | {intern/extern}   |

## Overzicht van epics

Deze paragraaf geeft een overzicht van alle epics die voorzien zijn in het systeem. De epics zijn geclassificeerd als wel of niet onderdeel van het minimum viable product (MVP).

| Epic ID   | Naam   | MVP?     |
|:----------|:-------|:---------|
| {epic ID} | {naam} | {ja/nee} |

## Gegevens binnen epics en user stories

Epics zijn volgens een vast formaat beschreven. De onderstaande tabel toont de gegevens die over een epic worden opgenomen.

| Epic            | *epic naam*               |
|:----------------|:--------------------------|
| Doel            | *doel van de epic*        |
| *user story ID* | *titel van de user story* |
| *user story ID* | *titel van de user story* |

De user stories beschrijven alle beoogde functionaliteit van het systeem. De lijst met user stories bevat vooralsnog alleen een identificatienummer en een titel.

User stories worden opgesteld volgens een vast formaat. De onderstaande tabel toont de gegevens die over een user story worden opgenomen.

| User story ID         | *Een unieke identificatie van de user story* |
|:----------------------|:----|
| User story titel      | *Korte aanduiding van de user story* |
| Beschrijving          | *Beschrijving van het doel in vast formaat: als __ROL__ wil ik __ACTIE__ zodat __REDEN__. De reden is de rationale die duidelijk maakt wat de businesswaarde is* |
| Screenshot prototype  | *Opnemen of verwijzen naar een screenshot of schets of een beschikbaar prototype* |
| Acceptatiecriteria    | *Acceptatiecriteria voor de betreffende user story, die niet al onderdeel zijn van de NFE* |
| Afhankelijkheden¹     | *Hier worden afhankelijkheden bedoeld die niet evident zijn, zoals bijvoorbeeld een koppeling 'e-herkenning'* |
| Performancerisico’s¹  | *Wanneer sprake is van omstandigheden die de performance nadelig kunnen beïnvloeden, zoals grote aantallen gebruikers of transacties* |
| Beveiligingsrisico’s¹ | *Wanneer sprake is van specifieke potentiële beveiligingsproblemen* |

¹) Indien van toepassing

# Epics

Dit hoofstuk beschrijft alle epics en de bijbehorende user stories. De epics en user stories zijn geclassificeerd volgens MosCoW-prioritering, deze is als volgt:

* **Must have (M)**: deze epics en user stories moeten in het eindresultaat terugkomen, zonder deze epics en user stories is het product niet bruikbaar;
* **Should have (S)**: deze epics en user stories zijn zeer gewenst, maar zonder is het product wel bruikbaar;
* **Could have (C)**: deze epics en user stories zullen alleen aan bod komen als er tijd genoeg is;
* **Would have (W)**: deze epics en user stories zullen waarschijnlijk in dit project niet aan bod komen maar kunnen in de toekomst, bij een vervolgproject, interessant zijn. Ze worden daarom ook wel eens aangeduid als "won't have".

Alle "must haves" bij elkaar worden gezien als de scope van het minimum viable product.

## {Epic 1}

| Epic            | {epic naam}               | Prioriteit |
|:----------------|:--------------------------|:-----------|
| Doel            | {doel van de epic}        | {M/C/S/W}  |
| {user story ID} | {titel van de user story} | {M/C/S/W}  |
| {user story ID} | {titel van de user story} | {M/C/S/W}  |

## {Epic 2}

| Epic            | {epic naam}               | Prioriteit |
|:----------------|:--------------------------|:-----------|
| Doel            | {doel van de epic}        | {M/C/S/W}  |
| {user story ID} | {titel van de user story} | {M/C/S/W}  |
| {user story ID} | {titel van de user story} | {M/C/S/W}  |
