## $M01$

#include "Content/Maatregelen/M01/Definitie.md"

ICTU hanteert de volgende documenten, templates en documentstandaarden voor softwareontwikkelprojecten:

**Functionele eisen**
De beschrijving van functionele eisen bestaat uit een geprioriteerde backlog met epics en/of user stories, eventueel aangevuld met use cases. De beschrijving bevat tevens eisen voor ondersteuning van beheerfuncties, die door de beoogd beheerder gesteld worden, en voor logging, inclusief de globale inhoud van te loggen business events (gebeurtenissen op procesniveau) en de daarvoor geldende bewaartermijnen.

Bronnen als procesbeschrijvingen, een programma van eisen en projectstartarchitectuur zijn het startpunt voor de functionele eisen. Tijdens het project worden use cases in samenwerking met de product owner vertaald naar user stories.

**Niet-functionele eisen**
Niet-functionele eisen specificeren criteria om het functioneren van de software te beoordelen, maar beschrijven niet het specifieke gedrag zelf. Voor de beschrijving en onderverdeling van niet-functionele eisen gebruikt ICTU:

* ISO/IEC-25010,
* Wet beveiliging netwerk- en informatiesystemen (Wbni),
* Baseline Informatiebeveiliging Overheid (BIO),
* methode Grip op SDD (Secure Software Development) van het Centrum Informatiebeveiliging en Privacybescherming (CIP),
* Algemene verordening gegevensbescherming (AVG),
* ISO 9241-210:2019 Ergonomics of human-system interaction - Part 210: Human-centred design for interactive systems,
* hoofdstuk 9 van de Europese Standaard EN 301 549 - dit is gelijk aan de Web Content Accessibility Guidelines versie 2.1, niveau A en AA.

De beschrijving van niet-functionele eisen moet expliciet aandacht besteden aan de door de beoogd beheerder gewenste ondersteuning van beheerfuncties. Bepaalde niet-functionele eisen kunnen aanleiding zijn tot het treffen van beveiligingsmaatregelen. Door deze eisen expliciet in de voorfase te benoemen, wordt voorkomen dat de bijbehorende beveiligingsmaatregelen achteraf moeten worden toegevoegd.

Overheidsorganisaties moeten een [toegankelijkheidsverklaring](https://www.digitoegankelijk.nl/verklaring) op hun websites plaatsen. Indien gewenst ondersteunt ICTU bij het opstellen van de toegankelijkheidsverklaring.

Bronnen als procesbeschrijvingen, privacy impact analysis (PIA), beheeracceptatiecriteria, beveiligingsbeleid, programma van eisen en projectstartarchitectuur zijn het startpunt voor de niet-functionele eisen.

**Product backlog**
De product backlog is een overzicht van alle nog te realiseren functionele en niet-functionele eigenschappen van de software. De product owner is de eigenaar van de product backlog. De zaken op de lijst zijn normaal gesproken in de vorm van een epic of user story. Hierin staat:

* *Wat* er gemaakt moet worden,
* *Waarom*,
* en voor *wie*.

De product owner is verantwoordelijk voor de inhoud en bepaalt de prioritering van de eisen. Er staan ook ruwe schattingen bij van de waarde voor de organisatie en van de ontwikkelkosten.

Zie [http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog](http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog).

**Ontwerp en architectuur**
De ontwerp- en architectuurdocumentatie beschrijft de opzet van de te bouwen software in de context waarbinnen het moet opereren en de ontwerpkeuzes en -principes die zijn gevolgd. Die documentatie laat tevens zien hoe de software aan de gestelde functionele en niet-functionele eisen voldoet.

Ontwerp- en architectuurinformatie kan haar plaats vinden in verschillende documenten en producten, zoals een projectstartarchitectuur (PSA), een softwarearchitectuurdocument (SAD), een infrastructuurarchitectuur (IA), een globaal functioneel ontwerp (GFO) en een prototype en/of interactieontwerp.

Een projectstartarchitectuur is bedoeld om te borgen dat nieuwe ontwikkelingen en veranderingen in samenhang worden gerealiseerd en passen binnen de toekomstig gewenste informatievoorziening. Een PSA bevat in ieder geval de volgende onderwerpen:

* Een beschrijving van de doelen en ambities waaraan het project bijdraagt en invulling geeft. Dus niet de projectdoelen en -ambitie.
* Een afbakening van het project en de context van de voorziening/oplossing die het project gaat realiseren gezien als een 'black box'. Denk o.a. ook aan relaties met andere projecten en generieke en specifieke diensten (services).
* De belangrijkste functies van de door het project te realiseren voorziening, informatiestromen en koppelvlakken.
* Een beschrijving van de belangrijkste belanghebbenden en/of betrokken ketenpartijen.
* Een concretisering van kaders en randvoorwaarden die van toepassing zijn.
* Beleidsuitgangspunten (drijfveren en doelen), zowel voor het specifieke project als algemeen voor de organisatie en visie (oplossingsrichting).
* Standaarden en normen (open standaarden van het Forum Standaardisatie en domeinspecifieke standaarden).

Zie [http://www.noraonline.nl/wiki/PSA_(Project_Startarchitectuur)](http://www.noraonline.nl/wiki/PSA_(Project_Startarchitectuur)).

Het softwarearchitectuurdocument verschaft een compleet overzicht van en rationale voor de architectuur van de te ontwikkelen software, waarbij diverse relevante views diverse aspecten van de software belichten. Zie bijvoorbeeld [http://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf); andere manieren van architectuurbeschrijving zijn ook toegestaan.

De infrastructuurarchitectuur beschrijft de topologie van de implementatie-omgeving waaronder protocollen, beveiligingsniveaus en services. Deze architectuur biedt een logische afbeelding van eisen naar implementatie-omgeving en geeft onderbouwing voor gemaakte keuzes.

Een prototype is een eerste, ruwe versie van de applicatie. Het prototype illustreert waar men uiteindelijk met de toepassing naar toe wil. Het maakt ideeën tastbaar en creëert een eerste indruk van structuur, ontwerp en functionaliteit.

**Test**
De testplannen bestaan uit een mastertestplan (MTP), gemaakt op basis van een productrisicoanalyse (PRA), en detailtestplannen. Het doel van een mastertestplan is om betrokkenen bij het testproces te informeren over de strategie, aanpak, activiteiten, inclusief de onderlinge relaties en afhankelijkheden, en de op te leveren producten met betrekking tot het testtraject. Het mastertestplan beschrijft deze strategie, aanpak, activiteiten en eindproducten, die in de detailtestplannen verder worden gedetailleerd.

ICTU maakt een detailtestplan voor de testsoorten die tijdens de realisatiefase door ICTU worden uitgevoerd. Voor testen die onder verantwoordelijkheid van ICTU door een derde partij worden uitgevoerd, denk aan penetratietesten en evaluaties van gebruikskwaliteit, worden aparte detailtestplannen gemaakt.

Logische testgevallen worden vastgelegd in Jira en gekoppeld met use cases en user stories. Fysieke testgevallen worden vastgelegd in het formaat van de gebruikte tooling en gekoppeld met de logische testgevallen. Op basis hiervan worden testrapportages gegenereerd die laten zien dat alle use cases en user stories zijn getest en dat die tests zijn geslaagd.

**Informatiebeveiliging**
Het informatiebeveiligingsplan vormt een handzaam document dat uitlegt binnen welke kaders bescherming geleverd wordt tegen welke dreigingen en hoe die bescherming vorm krijgt. Mogelijke bronnen voor het informatiebeveiligingsplan zijn de Business Impact Analysis (BIA), Privacy Impact Analysis (PIA) en de Threat and Vulnerability Assessment (TVA). De TVA wordt tijdens de voorfase opgesteld op basis van de resultaten van de BIA, de eventuele PIA en inhoud van de ontwerp- en architectuurdocumentatie. Een TVA levert een deel van een traceerbare onderbouwing voor de te treffen beveiligingsmaatregelen.

Het Voorschrift Informatiebeveiliging Rijksdienst (VIR) bevat een methode om te komen tot een systematische aanpak van informatiebeveiliging. Eén van de vereisten van het VIR is dat voor elk informatiesysteem en voor elk verantwoordelijkheidsgebied een afhankelijkheids- en kwetsbaarheidsanalyse (A&K-analyse) wordt uitgevoerd. Bij ICTU wordt daarvoor een TVA gebruikt. De betrouwbaarheidseisen, die aan de bedrijfsprocessen en dientengevolge aan het informatiesysteem of verantwoordelijkheidsgebied worden gesteld, worden tijdens een afhankelijkheidsanalyse geïnventariseerd. Vervolgens worden de bedreigingen geïdentificeerd en geanalyseerd.

**Deployment**
De deploymentdocumentatie bevat informatie over de eisen die een applicatie stelt aan een omgeving en de stappen die nodig zijn om de applicatie in die omgeving veilig te installeren en configureren. De documentatie bevat daartoe onder meer aanwijzingen voor de HTTP-header en -request-configuratie van de webserver en voor het verwijderen van overbodige header-informatie zoals de 'Server'-header. Ook zijn er aanwijzingen voor veilige configuratie(s) van (externe) toegang tot de beheerinterface. De documentatie bevat daarnaast in ieder geval een beschrijving van de protocollen en services die de applicatie aanbiedt, de protocollen, services en accounts die het product gebruikt en de protocollen, services en accounts die de applicatie gebruikt voor beheer.

**Kwaliteitsplan**
Het kwaliteitsplan beschrijft welke kwaliteitsmaatregelen het project treft om de niet-functionele eisen te realiseren.

**Vrijgaveadvies**
Voor elke major release stelt het project een vrijgaveadvies op. Het vrijgaveadvies bevat ten minste alle nog openstaande testbevindingen en geconstateerde beveiligingsbevindingen; zie ook {{M26}} en {{M16}}. Indien er issues zijn, bijvoorbeeld rondom kwaliteit of beveiliging, zijn deze voorzien van een beschreven voorziene impact.

**Overzicht**
De onderstaande tabel bevat de hierboven genoemde producten en geeft aan in welke fase ze van belang zijn en worden opgeleverd, ook als ze zijn opgesteld door externe auteurs.

Als tijdens een project bestaande software dient te worden afgebouwd, onderhouden en/of herbouwd, vindt een onderzoek plaats naar de compleetheid en consistentie van de bestaande softwareproducten aan de hand van de onderstaande tabel (inclusief de deliverables in de kolom 'Realisatiefase') en wordt de kwaliteit van de bestaande softwareproducten getoetst. Dit onderzoek, dat bij ICTU een "due diligence" heet, is onderdeel van de voorfase en wordt uitgevoerd door vertegenwoordigers van ICTU en medewerkers van het desbetreffende project, in samenwerking met vertegenwoordigers van de opdrachtgever.

| Product                                       | Voorfase | Voorfase met onderzoek | Realisatiefase |
|----------------------------------------------------------------------------------------|---|---|---|
| BIA (Business impact analysis)¹                                                        | ✔ | ✔ | ✔ |
| PIA (Privacy impact analysis)²                                                         | ✔ | ✔ | ✔ |
| Beschrijving van functionele eisen                                                     | ✔ | ✔ | ✔ |
| Beschrijving van niet-functionele eisen                                                | ✔ | ✔ | ✔ |
| Ontwerp- en architectuurdocumentatie (software, interactie, infrastructuur)            | ✔ | ✔ | ✔ |
| Testdocumentatie: testplannen                                                          | ✔ | ✔ | ✔ |
| Testdocumentatie: testgevallen, rapportages                                            |   |   | ✔ |
| Informatiebeveiligingsplan                                                             | ✔ | ✔ | ✔ |
| Projectplan                                                                            | ✔ | ✔ |   |
| Kwaliteitsplan                                                                         | ✔ | ✔ | ✔ |
| Deploybare versie van de software                                                      |   |   | ✔ |
| Broncode, inclusief de benodigdheden voor het bouwen van de software                   |   |   | ✔ |
| Regressietests, inclusief de benodigdheden voor het uitvoeren van de regressietesten   |   |   | ✔ |
| Vrijgaveadvies                                                                         |   |   | ✔ |
| Release notes                                                                          |   |   | ✔ |
| Deploymentdocumentatie                                                                 |   |   | ✔ |
| Uitkomsten onderzoek (bevindingen, risico's, mitigerende maatregelen)                  |   | ✔ |   |
| Transitieplan voor af te bouwen, te onderhouden en/of te herbouwen softwareproducten   |   | ✔ |   |
| Plan voor aflossen technische schuld, indien van toepassing                            |   | ✔ |   |

¹) De opdrachtgever stelt bij voorkeur een BIA en PIA voorafgaand aan een voorbereidende fase beschikbaar. Indien dat niet mogelijk is worden deze analyses gedurende de voorbereidende fase onder verantwoordelijkheid van de opdrachtgever uitgevoerd.
²) Indien een PIA niet nodig is, is een verklaring daaromtrent vereist.

### Rationale

Het uniformeren van op te leveren producten biedt voordelen voor planning (het is bekend welke producten gemaakt moeten worden), voor bemensing (het is bekend welke expertise nodig is) en voor het uitwisselen van medewerkers.

De voorgeschreven producten stellen de ontvanger in staat om de opgeleverde software uit te rollen, te beheren en te onderhouden. Daarnaast is duidelijk welke eventueel openstaande punten er nog zijn. De voorgeschreven producten bieden voldoende verantwoording richting de ontvanger voor uitgevoerde werkzaamheden.

De genoemde producten uit de voorbereidingsfase hebben tot doel om enerzijds de omvang, kosten en doorlooptijd van de realisatiefase te kunnen schatten en anderzijds om de kaders voor de realisatiefase te bepalen, zodat de scope, aanpak en oplossingsrichting in grote lijnen bekend zijn.

Een BIA en eventuele PIA zijn richtinggevend voor de in de voorbereidingsfase te selecteren beveiligingsmaatregelen en zijn daarom, bij voorkeur, voorafgaand aan het project al beschikbaar.

In een BIA legt de vragende organisatie vast hoe belangrijk informatiebeveiliging is voor de eigen bedrijfsvoering/processen. Naast de gevoeligheid voor incidenten komt hierin ook de 'risk appetite' van de organisatie tot uiting. Alleen de organisatie zelf kan hierover een uitspraak doen.

In een PIA legt de vragende organisatie vast wat de privacy-gevoeligheid is van de gegevens die in een proces of informatiesysteem worden verzameld en verwerkt. Zicht op privacygevoelige gegevens en het (laten) treffen van adequate en afdoende beschermingsmaatregelen is een wettelijke plicht die een organisatie niet aan een andere partij kan overdragen.

### Referenties

Zie ook:

* {{M14}}
