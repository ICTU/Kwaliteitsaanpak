# Opdrachtformulering voor de uit te voeren tests

## Doel van het testen

Het doel van de uit te voeren tests is dat {het product} wordt ontwikkeld en in gebruik genomen zonder onacceptabele risico's voor de gebruikers en voor de betrokken organisaties en hun medewerkers. Hiertoe worden tests gepland, uitgevoerd, gedocumenteerd en geaccepteerd. De testaanpak moet duidelijk maken wat de verschillende verantwoordelijkheden zijn van de verschillende partijen en disciplines die betrokken zijn bij het integrale testtraject.

De resultaten van de tests zijn de basis voor het vrijgaveadvies, op basis waarvan een besluit over ingebruikname van de betreffende release kan worden genomen.

## Context

{Beschrijf kort de context waarin de applicatie zal opereren, voor zover deze van belang is voor de uit te voeren tests. Denk aan de speciale eisen die worden gesteld aan de verschillende onderdelen van het informatiesysteem: het “samenhangend geheel van gegevensverzamelingen en de daarbij behorende personen, procedures, processen en programmatuur alsmede de voor het informatiesysteem getroffen voorzieningen voor opslag, verwerking en communicatie” (zie bijlage A).}

{Maak gebruik van beschrijvingen in bestaande documenten (zie paragraaf 2.5).}

## Scope van de tests

### Binnen scope

De volgende onderdelen van {het product} zijn binnen de scope van de tests: {Deel de onderdelen eventueel in per deelsysteem}

* software
* gegevensverzamelingen
* dataconversies
* interfaces (API’s) met: {de systemen waarmee informatie wordt uitgewisseld}
* infrastructurele voorzieningen
* ondersteunde processen
* {vul aan indien nodig}

{het product} wordt op de volgende kwaliteitskenmerken getest: {Maak gebruik van de kwaliteitskarakteristieken van de norm ISO/IEC-25010:2011 (zie [https://nl.wikipedia.org/wiki/ISO_25010](https://nl.wikipedia.org/wiki/ISO_25010)). Of vat de acceptatiecriteria samen die eventueel al zijn beschreven in het document Niet-functionele eisen.}

* functionele geschiktheid
* prestatie-efficiëntie (performance)
* uitwisselbaarheid (compatibility)
* bruikbaarheid (usability, inclusief toegankelijkheid)
* betrouwbaarheid
* beveiligbaarheid
* onderhoudbaarheid
* overdraagbaarheid
* {vul aan indien nodig}

Voor de combinaties van de onderdelen en de kwaliteitskenmerken worden in de productrisicoanalyse de risico’s bepaald (zie paragraaf 4.1).

### Buiten scope

Buiten de scope van de tests zijn:
* wijzigingen die geen onderdeel zijn van het project, zoals die ten aanzien van de infrastructuur, de systeemsoftware, de systemen waarmee informatie wordt uitgewisseld
* mogelijk toekomstige projecten die op het huidige project van invloed zijn
* {vul aan indien nodig}

{Noem eventueel ook deelsystemen als daarover onduidelijkheid kan bestaan.}

## Acceptanten

In onderstaande tabel is aangegeven wie de verantwoordelijken zijn voor de acceptatie van {het product}. Zij zijn de acceptanten, die akkoord moeten gaan met de resultaten van de tests voor de verschillende kwaliteitskenmerken en onderdelen van het product.

| Naam   | Organisatie                   | Functie         | Accepteert deze kwaliteitskenmerken | Accepteert deze onderdelen |
|:-------|:------------------------------|:----------------|:------------------------------------|:---------------------------|
| {naam} | {opdrachtgevende organisatie} | {projectleider} | {kenmerk}                           | {onderdeel}                |
| {naam} | {opdrachtgevende organisatie} | {product owner} | {kenmerk}                           | {onderdeel}                |
| {naam} | {organisatie}                 | {functie}       | {kenmerk}                           | {onderdeel}                |
| {naam} | {organisatie}                 | {functie}       | {kenmerk}                           | {onderdeel}                |
| {naam} | {organisatie}                 | {functie}       | {kenmerk}                           | {onderdeel}                |

# Productrisicoanalyse en teststrategie

De beschikbare tijd om te testen is beperkt; niet alles kan even zwaar worden getest. Dus moesten er keuzes worden gemaakt. Daarbij is ernaar gestreefd om de testcapaciteit zo effectief en efficiënt mogelijk over het totale testtraject te verdelen. Dit is vastgelegd in de teststrategie.

De teststrategie is gebaseerd op een risicoanalyse: {het product} moet zodanig voldoen in de praktijk dat er geen onacceptabele risico's voor de organisatie uit voortvloeien. Daar waar de oplevering van het systeem veel risico's met zich meebrengt, is uitgebreid testen op zijn plaats; het omgekeerde is aan de andere kant van het spectrum ook waar: 'no risk, no test'.

De eerste stap bij het vaststellen van de teststrategie was daarom het uitvoeren van een productrisicoanalyse. Hierin is het te testen product geanalyseerd, met als doel dat de testmanager en de verschillende andere belanghebbenden tot een gezamenlijk beeld kwamen van wat de meer of minder risicovolle kwaliteitskenmerken en delen van het te testen product zijn, zodat de grondigheid van testen hieraan gerelateerd kan worden. De uitvoering en resultaten van de productrisicoanalyse zijn in paragraaf 4.1 beschreven.

De teststrategie bouwt voort op de resultaten van de risicoanalyse: hier worden keuzes gemaakt over welke onderdelen van {het product} getest gaan worden, op welke manieren en op welke momenten. Paragraaf 4.2 beschrijft de teststrategie.

## Resultaat productrisicoanalyse

De acceptanten {optioneel: en andere bij het project betrokkenen} hebben gezamenlijk de productrisico’s vastgesteld. Deze zijn bepalend voor de zwaarte van de uit te voeren tests. Deze productrisicoanalyse (PRA) bestond uit twee stappen:

1.	Inventariseren van de van belang zijnde risico’s.
2.	Classificeren van de risico’s. De risicoklasse is op de volgende manier afgeleid van de faalkans (hoe groot is de kans dat het fout gaat?) en de schade (voor de organisatie als het inderdaad fout gaat): {beschrijving}

{Tijdens/na} de PRA zijn de omschrijvingen van de risico’s vertaald in kwaliteitskenmerken. Op basis van een kenmerk kunnen in de teststrategie de toe te passen testsoorten worden bepaald. De volledige productrisicoanalyse is beschreven in {documentreferentie}.

Onderstaande tabel bevat voor de verschillende onderdelen en kwaliteitskenmerken van {het product} de in de PRA vastgestelde risico’s en risicoklassen (A = hoog, B = middelhoog, C = laag).

| Volgnummer | Onderdeel product | Kwaliteitskenmerk van het product | Omschrijving risico | Risicoklasse |
|:-----------|:------------------|:----------------------------------|:--------------------|:-------------|
| R01        | {onderdeel}       | {kwaliteitskenmerk}               | {omschrijving}      | {A, B of C}  |
| R02        | {onderdeel}       | {kwaliteitskenmerk}               | {omschrijving}      | {A, B of C}  |
| R03        | {onderdeel}       | {kwaliteitskenmerk}               | {omschrijving}      | {A, B of C}  |

## Teststrategie

In de teststrategie is per onderdeel van {het product} bepaald welke testsoorten met welke zwaarte worden toegepast. Hierbij is de risicoklasse bepalend voor de zwaarte van de test. De teststrategie is er bovendien op gericht om de risico’s met de hoogste risicoklasse zo vroeg mogelijk in het testtraject af te dekken.

### Testsoorten en testvormen

Onderstaande tabel bevat de te plannen testsoorten met hun definities. Ook zijn de onderkende testvormen genoemd; deze worden in het volgende hoofdstuk toegelicht.

Een testsoort is een concreet uit te voeren test waarmee een of meer testdoelen worden gerealiseerd. Binnen een testsoort kunnen verschillende testvormen voorkomen; een testvorm is bedoeld voor het testen op een specifiek kenmerk van {het product}.

| Testsoort                           | Definitie                                                                                                                                                                                                                  | Testvormen                                                                          |
|:------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| Unittest (UT)                       | Een door de ontwikkelaar tijdens de realisatie uitgevoerde test, die moet aantonen dat het ontwikkelde onderdeel aan de functionele en niet-functionele specificaties en het technisch ontwerp voldoet.                    | Functionele test                                                                    |
| Unit-integratietest (UIT)           | Een door de ontwikkelaar tijdens de realisatie uitgevoerde test, die moet aantonen dat meerdere onderdelen samen aan de functionele en niet-functionele specificaties en het technisch ontwerp voldoen.                    | Functionele test                                                                    |
| Systeemtest (ST)                    | Een door het ontwikkelteam in een (goed beheersbare) laboratoriumomgeving uitgevoerde test, die moet aantonen dat het ontwikkelde systeem of delen daarvan aan de functionele- en niet-functionele specificaties voldoen.  | Functionele test, securitytest,  volledigheidstest, regressietest                   |
| Functionele acceptatietest (FAT)    | Een door een vertegenwoordiger van de opdrachtgever in een acceptatieomgeving uitgevoerde test, die moet aantonen dat het ontwikkelde systeem aan de functionele acceptatiecriteria voldoet.                               | Functionele test, volledigheidstest                                                 |
| Gebruikers-acceptatietest (GAT)     | Een door de beoogde gebruikers in een acceptatieomgeving uitgevoerde test, die moet aantonen dat zij met de geleverde applicatie hun werk correct en volledig kunnen doen.                                                 | Functionele test                                                                    |
| Penetratietest (PEN)                | Een door testers in een acceptatieomgeving uitgevoerde test, die moet aantonen dat het ontwikkelde systeem aan de beveiligingscriteria voldoet.                                                                            | Black box penetratietest, grey box penetratietest, white box penetratietest         |
| Performancetest (PERF)              | Een door testers in een productie-like omgeving uitgevoerde test die worden uitgevoerd om te bepalen hoe een systeem presteert in termen van reactievermogen en stabiliteit onder een bepaalde werklast.                   | Performance loadtest, performance stresstest, performance duurtest                  |
| Gebruikerstevreden-heidstest (GEBR) | Een gebruikerstevredenheidstest is een test om de functionaliteit van het systeem te testen door echte gebruikers taken te laten uitvoeren en te observeren hóe ze dat doen.                                               | Usabilitytest,enquête                                                               |
| Toegankelijkheidstest (TOEG)        | Een test waarbij de functionaliteit en toegankelijkheid van het systeem getest wordt, aan de hand van de webrichtlijnen WCAG 2.1                                                                                           |                                                                                     |
| Productie-acceptatietest (PAT)      | Een in een productie-like omgeving uitgevoerde test, die moet aantonen dat het ontwikkelde systeem aan de voor de (toekomstige) beheerorganisatie relevante acceptatiecriteria voldoet.                                    | Functionele test, installatie- en rollbacktest, hersteltest, backup- en restoretest |
| Conformancetest (CONF)              | Een test waarmee de beheerder van een stelsel kan toetsen of de oplossing van een aansluitende partij (authenticatiedienst, machtigingsdienst of dienstverlener) technisch en functioneel werkt volgens de gestelde eisen) | Afhankelijk van het stelsel                                                         |

Naast deze testsoorten voorziet het project de volgende toetsen (toetsingen/reviews van documenten uit de voorfase en realisatiefase):
* {review architectuur}
* {review ontwikkelomgeving}
* {vul aan indien relevant}

### Strategie voor de verschillende testsoorten

Afhankelijk van de risicoklasse (RK) is de beoogde teststrategie bepaald, dat wil zeggen: welke testsoorten met welke zwaarte per onderdeel van {het product} voor ieder kenmerk moeten worden uitgevoerd. Dit is samengevat in onderstaande tabellen.

De mogelijke testzwaarten zijn:
* Beperkte dynamische test: ●
* Gemiddelde dynamische test: ●●
* Zware dynamische test: ●●●

In een dynamische test wordt de software daadwerkelijk uitgevoerd. Daartegenover staan statische tests, waaronder het toetsen van documenten.

Waar de kolom Onderdeel niet is ingevuld geldt er één teststrategie voor alle onderdelen van {het product}. In deze kolom kan ook worden aangegeven dat de strategie de keten betreft.

De risiconummers verwijzen naar de in de PRA vastgestelde risico’s.

{Zorg dat de kolommen in de tabellen overeenkomen met de toe te passen testsoorten genoemd in de vorige paragraaf.}

##### Functionele geschiktheid

| Kenmerk                      | Onderdeel | RK | Risico-nummers | UT  | UIT | ST | FAT | {...} |
|:-----------------------------|:----------|:---|:---------------|:----|:----|:---|:----|:------|
| Functionele compleetheid     |           | M  |                | ●●  |     |    |     |       |
| Functionele correctheid      | {deel 1}  | M  |                | ●●● | ●●● |    | ●●  |       |
| Functionele correctheid      | {deel 2}  | M  |                | ●●  | ●●● |    | ●●  |       |
| Functionele toepasselijkheid |           | M  |                |     |     | ●● |     |       |

##### Prestatie-efficiëntie

| Kenmerk        | Onderdeel | RK | Risico-nummers | UT  | UIT | ST | FAT | {...} |
|:---------------|:----------|:---|:---------------|:----|:----|:---|:----|:------|
| Snelheid       |           | M  |                | ●●  |     |    |     |       |
| Middelenbeslag | {deel 1}  | H  |                | ●●● | ●●● |    | ●●  |       |
| Middelenbeslag | {deel 2}  | M  |                | ●●  | ●●● |    | ●●  |       |
| Capaciteit     |           | M  |                | ●●  |     |    |     |       |

##### Uitwisselbaarheid

| Kenmerk           | Onderdeel | RK | Risico-nummers | UT | UIT | ST | FAT | {...} |
|:------------------|:----------|:---|:---------------|:---|:----|:---|:----|:------|
| Beïnvloedbaarheid | {deel 1}  | M  |                | ●● | ●●  |    |     |       |
| Beïnvloedbaarheid | {deel 2}  | M  |                | ●● | ●●  |    |     |       |
| Koppelbaarheid    |           | M  |                | ●● | ●●  |    |     |       |

##### Bruikbaarheid

| Kenmerk                           | Onderdeel | RK | Risico-nummers | UT | UIT | ST | FAT | {...} |
|:----------------------------------|:----------|:---|:---------------|:---|:----|:---|:----|:------|
| Herkenbaarheid van geschiktheid   |           | M  |                | ●● | ●●  |    |     |       |
| Leerbaarheid                      | {deel 1}  | M  |                | ●● | ●●  |    |     |       |
| Leerbaarheid                      | {deel 2}  | M  |                | ●● | ●●  |    |     |       |
| Bedienbaarheid                    |           | M  |                | ●● | ●●  |    |     |       |
| Voorkomen gebruiksfouten          | {deel 1}  | H  |                | ●● | ●●● |    |     |       |
| Voorkomen gebruiksfouten          | {deel 2}  | L  |                | ●● | ●●  |    |     |       |
| Volmaaktheid gebruikersinteractie |           | M  |                | ●● | ●●  |    |     |       |
| Toegankelijkheid                  |           | M  |                | ●● | ●●  |    |     |       |

##### Betrouwbaarheid

| Kenmerk           | Onderdeel | RK | Risico-nummers | UT  | UIT | ST | FAT | {...} |
|:------------------|:----------|:---|:---------------|:----|:----|:---|:----|:------|
| Volwassenheid     |           | M  |                | ●●● | ●●  |    |     | ●●    |
| Beschikbaarheid   |           | M  |                | ●●● | ●●  |    |     | ●●    |
| Foutbestendigheid |           |    |                |     |     |    |     |       |
| Herstelbaarheid   |           | M  |                | ●●● | ●●  |    |     | ●●    |

##### Beveiligbaarheid

| Kenmerk           | Onderdeel | RK | Risico-nummers | UT  | UIT | ST  | FAT | {...} |
|:------------------|:----------|:---|:---------------|:----|:----|:----|:----|:------|
| Vertrouwelijkheid |           | L  |                | ●●● | ●   | ●   |     |       |
| Integriteit       | {deel 1}  | H  |                | ●●  |     | ●●● |     |       |
| Integriteit       | {deel 2}  | L  |                | ●   |     | ●   |     |       |
| Onweerlegbaarheid |           | L  |                | ●●● | ●   | ●   |     |       |
| Verantwoording    |           | L  |                | ●   | ●   | ●   | ●   |       |
| Authenticiteit    |           | L  |                | ●●● | ●   | ●   |     |       |

##### Onderhoudbaarheid

| Kenmerk           | Onderdeel | RK | Risico-nummers | UT  | UIT | ST  | FAT | {...} |
|:------------------|:----------|:---|:---------------|:----|:----|:----|:----|:------|
| Modulariteit      |           |    |                |     |     |     |     |       |
| Herbruikbaarheid  |           | L  |                | ●●● | ●   | ●   |     |       |
| Analyseerbaarheid | {deel 1}  | H  |                | ●●  |     | ●●● |     |       |
| Analyseerbaarheid | {deel 2}  | L  |                | ●   |     | ●   |     |       |
| Wijzigbaarheid    |           |    |                |     |     |     |     |       |
| Testbaarheid      |           |    |                |     |     |     |     |       |

##### Overdraagbaarheid

| Kenmerk            | Onderdeel | RK | Risico-nummers | UT  | UIT | ST | FAT | {...} |
|:-------------------|:----------|:---|:---------------|:----|:----|:---|:----|:------|
| Aanpasbaarheid     |           |    |                |     |     |    |     |       |
| Installeerbaarheid |           | M  |                | ●●● | ●●  |    |     | ●●    |
| Vervangbaarheid    |           | M  |                | ●●● | ●●  |    |     | ●●    |

# Testaanpak

In dit hoofdstuk is de teststrategie vertaald naar een concrete testaanpak (het hoe). Voor iedere testsoort is hiervoor een deelparagraaf opgenomen.

{Zorg er hierbij voor dat de beschreven testaanpak de teststrategie uit het vorige hoofdstuk reflecteert. Elk element uit de teststrategie moet hier dan ook terugkomen. Als er, volgend op het MTP, voor een testsoort ook nog een detailtestplan (DTP) wordt opgesteld, dan is de betreffende paragraaf minder diepgaand dan wanneer dit niet het geval is (refereer dan wel aan het DTP). Twee belangrijke factoren die bepalen of er wel/niet DTP's worden opgesteld zijn
de omvang van het project en de mate waarin er bij het opstellen van het MTP nog onzekerheden/onduidelijkheden zijn.}

## Aansluiting op de agile werkwijze

In onderstaand plaatje is weergegeven welke testproducten worden gerealiseerd op welke momenten in het agile proces van ontwikkeling, ingebruikname en inbeheername:

![Relaties tussen agile proces en testproducten](relaties-testproducten-agile.png "Relaties tussen testproducten en agile")

De op de tests toe te passen acceptatiecriteria worden als volgt bepaald:

| Testsoort                           | Wanneer en hoe bepalen van acceptatiecriteria                                                                                                                                                                                               |
|:------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unittest (UT)                       | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Unit-integratietest (UIT)           | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Systeemtest (ST)                    | De testspecificaties voor de systeemtest worden tijdens de sprints gemaakt, parallel aan de realisatie.                                                                                                                                     |
| Functionele acceptatietest (FAT)    | Functionele acceptatiecriteria voor een sprint worden vóór een sprint opgesteld (backlog refinement). {Alternatief: De testspecificaties voor de functionele acceptatietest worden tijdens de sprints gemaakt, parallel aan de realisatie.} |
| Gebruikers-acceptatietest (GAT)     | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Penetratietest (PEN)                | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Performancetest (PERF)              | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Gebruikerstevreden-heidstest (GEBR) | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Toegankelijkheidstest (TOEG)        | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Productie-acceptatietest (PAT)      | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |
| Conformancetest (CONF)              | {Beschrijf wanneer en hoe de acceptatiecriteria worden bepaald}                                                                                                                                                                             |

## Aanpak van de toetsen

{Indien toetsen onderdeel zijn van de teststrategie, beschrijf dan hier de aanpak van deze toetsen of: “Toetsen zijn geen onderdeel van de teststrategie”.}.

## Aanpak van de testsoorten

{In deze template is de Systeemtest als voorbeeld genomen. Deze paragraaf wordt herhaald voor iedere toe te passen testsoort.}

### Aanpak systeemtest

{Als er voor een testsoort een detailtestplan wordt opgesteld, geef dan hier alleen een korte beschrijving van de testsoort en verwijs naar het detailtestplan.}

##### Beschrijving systeemtest algemeen

| Onderwerp                    | Beschrijving                                                                                                                                                              |
|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aandachtspunten              | {Denk aan: bijzondere risico’s, en voor welke kenmerken; of de test voor specifieke onderdelen van het systeem moet worden uitgevoerd}                                    |
| Acceptatiecriteria           | {De criteria waaraan de testresultaten moeten voldoen voor de acceptatie van een increment of een release}                                                                |
| Uitvoering door              | Scrumteam                                                                                                                                                                 |
| Frequentie                   | {Bij welke (oplever)momenten in het voortbrengingsproces de test wordt uitgevoerd}                                                                                        |
| Specificaties opgesteld door |                                                                                                                                                                           |
| Testbasis                    | {GFO, use cases en user stories, informatiebeveiligingsplan}                                                                                                              |
| Entry-criteria               | {Wanneer met de testsoort kan worden begonnen. Denk aan: welke andere tests afgerond moeten zijn; noodzakelijke voorbereidingen}                                          |
| Exit-criteria                | {Wanneer de testsoort naar tevredenheid is afgerond. Heeft een relatie met de Definition of Done. Denk aan: vereiste testdekking; maximum aantal blokkerende bevindingen} |
| Infrastructuur               |                                                                                                                                                                           |
| Testomgeving                 |                                                                                                                                                                           |

{Controleer of de hieronder beschreven testvormen voldoende invulling geven aan de teststrategie voor deze testsoort: per kwaliteitskenmerk, eventueel specifiek voor bepaalde onderdelen, met de gewenste zwaarte.}

##### Testvorm functionele test

| Onderwerp    | Beschrijving                                                                                                                           |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| Omschrijving | Controleren of de functionaliteit correct is gerealiseerd conform de beschrijving in de functionele documentatie en procesbeschrijving |
| Onderdelen   | Autorisaties t.a.v. wachtwoord, beheer en logging                                                                                      |
| Diepgang     | Alle goed- en foutpaden                                                                                                                |

##### Testvorm securitytest

| Onderwerp    | Beschrijving                                                                                                               |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------|
| Omschrijving | Controleren of de security ‘functionals’ (wachtwoordinvoer, autorisatiebeheer, logging, toegang etc.) correct functioneren |
| Onderdelen   |                                                                                                                            |
| Diepgang     |                                                                                                                            |

##### Testvorm volledigheidstest

| Onderwerp    | Beschrijving                                                                                                                    |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------|
| Omschrijving | Steekproefsgewijs controleren of de mechanismes die de volledigheid moeten borgen (bijvoorbeeld tellingen) correct functioneren |
| Onderdelen   |                                                                                                                                 |
| Diepgang     |                                                                                                                                 |

##### Testvorm regressietest

| Onderwerp    | Beschrijving                                                                                              |
|:-------------|:----------------------------------------------------------------------------------------------------------|
| Omschrijving | Geautomatiseerd controleren dat de functionaliteit uit voorgaande sprints nog steeds correct functioneert |
| Onderdelen   |                                                                                                           |
| Diepgang     |                                                                                                           |

### Aanpak {testsoort}

{Gebruik de vorige paragraaf als template en vul deze in voor de andere testsoorten.}

## Op te leveren producten

De volgende producten worden door het testteam opgeleverd:

| Testsoort   | Product       | Doel   | Doelgroep   | Opstellers   | Reviewers   |
|:------------|:--------------|:-------|:------------|:-------------|:------------|
| {testsoort} | {het product} | {doel} | {doelgroep} | {opstellers} | {reviewers} |

## Go / No go voor vervolg

{Beschrijf hier het Go/No go beslissingsproces. Het vervolg kan de realisatie van een volgend increment zijn of de vrijgave van een release voor ingebruikname van het systeem. In dat laatste geval wordt na afronding van het gehele testtraject een vrijgaveadvies opgesteld. Het vrijgaveadvies bevat alle nog openstaande testbevindingen en geconstateerde beveiligingsbevindingen. Er wordt vermeld in hoeverre aan de gestelde acceptatiecriteria is voldaan. Op basis van de resultaten van de verschillende testsoorten zijn de risico’s voor gebruikers en beheerorganisaties vastgesteld bij eventuele ingebruikname van het informatiesysteem.}

# Organisatie

## Organisatiestructuur

{Neem hier het organogram van de testorganisatie op en de relatie tot de projectorganisatie.}

## Rollen, taken en verantwoordelijkheden

In onderstaande tabel zijn per rol de taken en verantwoordelijkheden beschreven.

| Rol   | Naam   | Testsoort   | Uren per week   | Periode   | Taken en verantwooordelijkheden  |
|:------|:-------|:------------|:----------------|:----------|:---------------------------------|
| {rol} | {naam} | {testsoort} | {uren per week} | {periode} | {taken en verantwoordelijkheden} |

{Maak onderscheid tussen overallniveau en per testsoort. Voeg extra personen toe en geef per rol de specifieke taken en verantwoordelijkheden aan. Alle betrokkenen die genoemd zijn in de testaanpak dienen hier terug te komen.}

{Optioneel: Per rol niet alleen de taken en verantwoordelijkheden benoemen, maar ook de bevoegdheden. Zonder bevoegdheden geen verantwoordelijkheden.}

## Opleidings- en coachingsbehoefte

{Vermeld hier de opleidings- en coachingsbehoefte van de testmedewerkers ten behoeve van de juiste materie- en/of testkennis.}

## Overlegstructuur

In de volgende overleggen worden afspraken gemaakt over het plannen en uitvoeren van tests:

| Overleg                   | Doel                                                     | Frequentie   | Deelnemers                  |
|:--------------------------|:---------------------------------------------------------|:-------------|:----------------------------|
| Projectoverleg            | Voortgang project bespreken, risicolog behandelen        | wekelijks    | Projectleiders, testmanager |
| Werkoverleg per testsoort | Stand van zaken per testsoort bespreken                  | wekelijks    | Testmanager, testers        |
| Bevindingenoverleg        | Bespreking inhoud, risico en planning rondom bevindingen | {frequentie} | {deelnemers}                |
| {overleg}                 | {doel}                                                   | {frequentie} | {deelnemers}                |

# Testinfrastructuur

Het uitgangspunt voor de testinfrastructuur is dat verschillende testsoorten in verschillende testomgevingen kunnen worden gedaan. Deze scheiding is nodig om te kunnen voldoen aan de verschillende eisen van de testsoorten; een performancetest stelt bijvoorbeeld andere eisen aan een omgeving dan een usabilitytest.

{Zie eventuele detailtestplannen.}

## Testomgevingen

Onderstaande tabel bevat een opsomming van de testomgevingen per testsoort. Zie de volgende paragraaf voor het beheer van de testomgevingen.

| Test-soort | Testomgeving        | Infrastructuur   | Testgegevens   | Periode   | Kosten   |
|:-----------|:--------------------|:-----------------|:---------------|:----------|:---------|
| UT         | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| UIT        | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| ST         | Ontwikkel-omgeving  | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| FAT        | Testomgeving        | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| GAT        | Acceptatie-omgeving | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| PEN        | Productie-omgeving  | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| PERF       | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| GEBR       | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| TOEG       | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| PAT        | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |
| CONF       | {testomgeving}      | {infrastructuur} | {testgegevens} | {periode} | {kosten} |

# Testtools

Onderstaande tabel bevat een opsomming van de testtools per testsoort of testvorm.

{Deze tabel kan ook worden gecombineerd met die in de vorige paragraaf.}

| Testsoort | Testvorm   | Testtool   | Toelichting   | Periode   | Kosten   |
|:----------|:-----------|:-----------|:--------------|:----------|:---------|
| UT        | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| UIT       | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| ST        | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| FAT       | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| GAT       | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| PEN       | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| PERF      | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| GEBR      | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| TOEG      | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| PAT       | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |
| CONF      | {testvorm} | {testtool} | {toelichting} | {periode} | {kosten} |

# Beheer

In dit hoofdstuk wordt beschreven hoe de activiteiten uit het testplan worden uitgevoerd, bewaakt en eventueel bijgestuurd.

## Testproductbeheer

{Beschrijf hier hoe de op te leveren producten worden beheerd en bewaakt. Beschrijf hiervoor procedures, sjablonen, tools en de omgeving waar de producten worden vastgelegd.}

## Bevindingenprocedures

Het bevindingenbeheer is ingericht conform de {in de methode X beschreven bevindingenprocedure, of, de bij de klantorganisatie vigerende bevindingenprocedure}. Voor het registreren en onderhouden van bevindingen wordt gebruik gemaakt van {tool}.

De verantwoordelijkheid voor de naleving van het bevindingenbeheer ligt bij de {testmanager}.

Onderstaande tabel bevat de bevindingenprocedures per testsoort en/of testvorm.

| Testsoort | Testvorm   | Bevindingenprocedure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:----------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UT        | {testvorm} | {bevindingenprocedure}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| UIT       | {testvorm} | {bevingingenprocedure}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ST        | {testvorm} | De bevindingen die niet binnen de sprint worden opgelost zullen geregistreerd worden in het bevindingenregistratiesysteem. Deze bevindingen komen op de backlog en zullen op basis van prioriteit door de product owner in één van de volgende sprints worden gepland.                                                                                                                                                                                                                                                  |
| FAT       | {testvorm} | De bevindingen worden vastgelegd in het bevindingenregistratiesysteem en in bevindingenoverleg besproken. Deze bevindingen komen op de backlog en worden op basis van prioriteit door de product owner in dezelfde sprint of in één van de volgende sprints gepland. Een uitzondering hierop vormen blokkerende testbevindingen. Voor deze bevindingen moet zo snel mogelijk binnen de lopende sprint een oplossing worden gerealiseerd. Dit zal in overleg met het ontwikkelteam door de product owner worden bepaald. |
| GAT       | {testvorm} | Zie FAT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PEN       | {testvorm} | Zie FAT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PERF      | {testvorm} | {bevingingenprocedure}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| GEBR      | {testvorm} | {bevingingenprocedure}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| TOEG      | {testvorm} | {bevingingenprocedure}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PAT       | {testvorm} | Zie FAT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CONF      | {testvorm} | {bevingingenprocedure}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

# Testprocesrisico's en maatregelen

In dit hoofdstuk zijn de belangrijkste potentiële projectrisico's voor het testproces van {project} beschreven. Door te anticiperen op wat mogelijk kan gebeuren kunnen nu reeds maatregelen worden getroffen. De risico’s kunnen optreden in het testproces zelf of projectrisico’s zijn met gevolgen voor het testproces.

Het in kaart brengen en bewaken van deze risico’s is ook na het opstellen van dit MTP een continu proces: bij uitwerking van de testaanpak en bij aanvang van de testuitvoering van elke testsoort zal de risicotaxatie worden geactualiseerd.

De volgende risico’s voor het testproces zijn onderkend. Zie ook het risicolog {documentreferentie}.

| Risicovolg-nummer   | Testsoort   | Gebeurtenis   | Gevolg   | Impact   | Kans   | Score   |
|:--------------------|:------------|:--------------|:---------|:---------|:-------|:--------|
| {risicovolg-nummer} | {testsoort} | {gebeurtenis} | {gevolg} | {impact} | {kans} | {score} |

De volgende maatregelen zijn getroffen.

| Risicovolgnummer   | Maatregelvolgnummer   | Maatregel   | Eigenaar   |
|:-------------------|:----------------------|:------------|:-----------|
| {risicovolgnummer} | {maatregelvolgnummer} | {maatregel} | {eigenaar} |

De testmanager is op deze punten extra alert en bewaakt de te nemen maatregelen.

De maatregelen die niet binnen de testorganisatie kunnen worden genomen worden in het projectoverleg besproken en toegewezen. Ze worden vastgelegd in de actielijst en bewaakt tijdens het projectoverleg.

# Globale planning

{Neem in de globale planning de volgende onderdelen op:}

* {de onderscheiden testsoorten en testvormen}
* {op te leveren producten;}
* {te behalen mijlpalen;}
* {uit te voeren activiteiten (op faseniveau per testsoort) met start- en einddatum;}
* {relaties met en afhankelijkheden van andere activiteiten (binnen of buiten het testproces en tussen de diverse testsoorten);}
* {te besteden tijd per testsoort;}
* {benodigde en beschikbare resources (organisatie en infrastructuur);}
* {benodigde en beschikbare doorlooptijd.}
