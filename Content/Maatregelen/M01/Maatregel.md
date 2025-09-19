## $M01$

#include "Content/Maatregelen/M01/Definitie.md"

Opdrachtgevende organisatie, ICTU, beheerorganisatie en andere meewerkende partijen leveren de onderstaande informatie op. Voor een aantal documenten zijn als onderdeel van de Kwaliteitsaanpak templates beschikbaar. Ook kan gebruik worden gemaakt van bestaande templates uit bijvoorbeeld de NORA. Zie [$M29$](#m29).

De onderstaande tabel bevat de in deze paragraaf beschreven producten. Het vinkje (✔) geeft aan in welke fase ze (initieel) worden opgeleverd. Het tandwiel (⚙) geeft aan in welke fase de producten worden onderhouden en bijgewerkt.

| Product | Voor start | Voorfase | Realisatiefase | Verantwoordelijke organisatie |
|---------|------------|----------|----------------|-------------------------------|
| [submeasure-title]Business impact analyse[/submeasure-title]                             | ✔          | ⚙        | ⚙              | opdrachtgever                 |
| [submeasure-title]Data protection impact assessment[/submeasure-title]                   | ✔          | ⚙        | ⚙              | opdrachtgever                 |
| [submeasure-title]Impact assessment mensenrechten en algoritmes[/submeasure-title]       | ✔          | ⚙        | ⚙              | opdrachtgever                 |
| [submeasure-title]Projectstartarchitectuur en solution architectuur [/submeasure-title]  | ✔          | ⚙        | ⚙              | opdrachtgever                 |
| [submeasure-title]Afspraken met de beheerorganisatie [/submeasure-title]                 | ✔          | ⚙        | ⚙              | opdrachtgever                 |
| [submeasure-title]Plan van aanpak: voorfase [/submeasure-title]                          | ✔          |          |                | ICTU                          |
| [submeasure-title]Beschrijving van functionele eisen [/submeasure-title]                 |            | ✔        | ⚙              | opdrachtgever                 |
| [submeasure-title]Beschrijving van niet-functionele eisen [/submeasure-title]            |            | ✔        | ⚙              | opdrachtgever                 |
| [submeasure-title]Product backlog[/submeasure-title]                                    |            | ✔        | ⚙              | opdrachtgever                 |
| [submeasure-title]Ontwerp- en architectuurdocumentatie[/submeasure-title]                |            | ✔        | ⚙              | ICTU, beheerorganisatie       |
| [submeasure-title]Mastertestplan[/submeasure-title]                                      |            | ✔        | ⚙              | opdrachtgever                 |
| [submeasure-title]Detailtestplannen[/submeasure-title]                                   |            | ✔        | ⚙              | ICTU, beheerorganisatie       |
| [submeasure-title]Informatiebeveiligingsplan[/submeasure-title]                          |            | ✔        | ⚙              | opdrachtgever                 |
| [submeasure-title]Kwaliteitsplan[/submeasure-title]                                      |            | ✔        | ⚙              | ICTU                          |
| [submeasure-title]Plan van aanpak: realisatiefase[/submeasure-title]                     |            | ✔        |                | ICTU                          |
| [submeasure-title]Deploybare versie van de software[/submeasure-title]                   |            |          | ✔              | ICTU                          |
| [submeasure-title]Testrapportages[/submeasure-title]                                     |            |          | ✔              | ICTU, beheerorganisatie       |
| [submeasure-title]Documentatie voor deployment en operationeel beheer[/submeasure-title] |            |          | ✔              | ICTU                          |
| [submeasure-title]Software bill of materials[/submeasure-title]                          |            |          | ✔              | ICTU                          |
| [submeasure-title]Release notes[/submeasure-title]                                       |            |          | ✔              | ICTU                          |
| [submeasure-title]Vrijgaveadvies[/submeasure-title]                                      |            |          | ✔              | opdrachtgever                 |

### Business impact analyse

In een business impact analyse (BIA) legt de opdrachtgevende organisatie vast hoe belangrijk informatiebeveiliging is voor de eigen bedrijfsvoering/processen. Naast de gevoeligheid voor incidenten komt hierin ook de 'risk appetite' van de organisatie tot uiting: de risico’s die een organisatie bereid is te accepteren. Alleen de opdrachtgevende organisatie zelf kan hierover een uitspraak doen.

### Data protection impact assessment

In een data protection impact assessment (DPIA) legt de opdrachtgevende organisatie vast wat de privacy-gevoeligheid is van de gegevens die in een proces of informatiesysteem worden verzameld en verwerkt. De rechtmatigheid van de verwerking wordt beoordeeld. En de DPIA stelt grenzen aan de gegevens die mogen worden verzameld en verwerkt. Zicht op privacygevoelige gegevens en het (laten) treffen van adequate en afdoende beschermingsmaatregelen is een wettelijke plicht die een organisatie niet aan een andere partij kan overdragen.

Als een DPIA niet nodig is, dan is een verklaring daaromtrent vereist.

### Impact assessment mensenrechten en algoritmes

$IAMA$. Met een dergelijke impact assessment kan een interdisciplinaire dialoog gevoerd worden tussen relevante partijen bij de afweging om wel of niet een algoritmische toepassing te gaan ontwikkelen. En het helpt om de gekozen ontwikkeling en implementatie vervolgens op een verantwoorde manier te doen. In het IAMA worden verbanden gelegd met relevante regels, instrumenten en toetskaders op het gebied van algoritmen.

Een IAMA wordt ingezet in alle gevallen waarin een overheidsorgaan overweegt een algoritme te (laten) ontwikkelen, in te kopen, aan te passen en/of in te gaan zetten.

Zie [https://www.rijksoverheid.nl/documenten/rapporten/2021/02/25/impact-assessment-mensenrechten-en-algoritmes](https://www.rijksoverheid.nl/documenten/rapporten/2021/02/25/impact-assessment-mensenrechten-en-algoritmes).

Voor meer informatie over het gezamenlijk gebruik van IAMA en DPIA, zie [https://www.cip-overheid.nl/media/av0dmahv/20230614-gezamenlijk-gebruik-iama-en-model-dpia-rijksdienst-v1-0.pdf](https://www.cip-overheid.nl/media/av0dmahv/20230614-gezamenlijk-gebruik-iama-en-model-dpia-rijksdienst-v1-0.pdf).

### Projectstartarchitectuur en solution architectuur

Een projectstartarchitectuur (PSA) is bedoeld om te borgen dat nieuwe ontwikkelingen en veranderingen in samenhang worden gerealiseerd en passen binnen de toekomstig gewenste informatievoorziening. De PSA is een concreet en doelgericht ICT-architectuurkader waarbinnen het project moet worden uitgevoerd. In de PSA zijn de architectuurvisie, enterprise-architectuur en overige architecturen van de opdrachtgevende organisatie vertaald naar aan het product te stellen eisen. BIA, DPIA en IAMA zijn input voor de PSA. Een PSA bevat in ieder geval de volgende onderwerpen:

* Een beschrijving van de doelen en ambities waaraan het project bijdraagt en invulling geeft. Dus niet de projectdoelen en -ambitie.
* Een afbakening van het project en de context van de voorziening/oplossing die het project gaat realiseren. De PSA beschrijft niet de implementatie van de voorziening zelf (dit blijft een 'black box'), maar wel het gewenste gedrag in het grotere geheel. Denk o.a. ook aan relaties met andere projecten en generieke en specifieke diensten (services).
* De belangrijkste functies van de door het project te realiseren voorziening, informatiestromen en koppelvlakken.
* Een beschrijving van de belangrijkste belanghebbenden en/of betrokken ketenpartijen.
* Een concretisering van kaders en randvoorwaarden die van toepassing zijn.
* Beleidsuitgangspunten (drijfveren en doelen), zowel voor het specifieke project als algemeen voor de organisatie en visie (oplossingsrichting).
* Standaarden en normen (open standaarden van het Forum Standaardisatie en domeinspecifieke standaarden).

Zie [https://www.noraonline.nl/wiki/PSA](https://www.noraonline.nl/wiki/PSA).

Conform NORA werkt de opdrachtgevende organisatie na de start van het project de PSA uit in een solution architectuur (SA).

Zie [https://www.noraonline.nl/wiki/Solution-architectuur](https://www.noraonline.nl/wiki/Solution-architectuur).

### Afspraken met de beheerorganisatie

De opdrachtgevende organisatie heeft afspraken gemaakt met een (interne of externe) beheerorganisatie die voornemens is het beheer van de software uit te voeren. De afspraken omvatten in ieder geval de inzet van medewerkers van de beheerorganisatie tijdens de voorfase en het type beheer dat de beheerorganisatie voornemens is te gaan uitvoeren: operationeel beheer, applicatiebeheer en/of functioneel beheer.

De beheerorganisatie stelt relevante informatie ter beschikking aan het project zoals beveiligingsbeleid, beheeracceptatiecriteria, documentatie van de te gebruiken voorzieningen voor bijvoorbeeld authenticatie en autorisatie en verder te hanteren kaders en richtlijnen.

### Plan van aanpak

Het plan van aanpak voor de voorfase en het plan van aanpak voor de realisatiefase beschrijven de in deze fasen te realiseren producten en diensten, en de planning, werkwijze en verantwoordelijkheden voor de totstandkoming van die producten en diensten.

Als tijdens de realisatiefase van het project bestaande software dient te worden afgebouwd, onderhouden en/of herbouwd, bevat het plan van aanpak voor de voorfase een onderzoek naar de kwaliteit van deze software, zie [$M32$](#m32).

Als operationeel en/of applicatiebeheer onderdeel is van de te leveren dienstverlening tijdens de realisatiefase bevat het plan van aanpak voor de realisatiefase de hiervoor noodzakelijke afspraken met de opdrachtgevende organisatie en de beheerorganisatie. De afspraken omvatten zowel de te behalen kwaliteitsniveaus van de dienstverlening als de uit te voeren operationele en applicatiebeheertaken. Daarnaast beschrijft het plan hoe informatie zal worden verzameld over de software tijdens het gebruik en over de uitgevoerde beheeractiviteiten. En hoe hierover zal worden gerapporteerd. Ook worden de criteria voor het beëindigen van de dienstverlening vastgelegd. De te leveren dienstverlening is afgestemd op het beheerplan van de beheerorganisatie.

Beschikbare templates:

* [Template plan van aanpak voorfase]($BASE_URL$/$VERSIE$/ICTU-Template-Plan-van-Aanpak-Voorfase.docx).
* [Template plan van aanpak realisatiefase]($BASE_URL$/$VERSIE$/ICTU-Template-Plan-van-Aanpak-Realisatiefase.docx).

### Beschrijving van functionele eisen

De beschrijving van functionele eisen bestaat uit epics en/of user stories, eventueel aangevuld met use cases. De beschrijving bevat tevens eisen voor ondersteuning van beheerfuncties, die door de beoogd beheerder gesteld worden, en voor logging, inclusief de globale inhoud van te loggen business events (gebeurtenissen op procesniveau) en de daarvoor geldende bewaartermijnen.

Bronnen van de opdrachtgevende organisatie zoals de projectstartarchitectuur, een programma van eisen en procesbeschrijvingen vormen het startpunt voor de functionele eisen. Tijdens het project worden use cases in samenwerking met de product owner vertaald naar epics en user stories.

### Beschrijving van niet-functionele eisen

Niet-functionele eisen specificeren criteria om het functioneren van de software te beoordelen, maar beschrijven niet het specifieke gedrag zelf. Voor de beschrijving en onderverdeling van niet-functionele eisen maakt het project gebruik van:

* NEN-ISO/IEC 25010:2023,
* Wet beveiliging netwerk- en informatiesystemen (Wbni),
* Baseline Informatiebeveiliging Overheid (BIO),
* methode Grip op SDD (Secure Software Development) van het Centrum Informatiebeveiliging en Privacybescherming (CIP),
* Algemene verordening gegevensbescherming (AVG),
* ISO 9241-210:2019 Ergonomics of human-system interaction - Part 210: Human-centred design for interactive systems,
* Web Content Accessibility Guidelines versie 2.2, niveau A en AA. Hiermee wordt invulling gegeven aan hoofdstuk 9 van de Europese Standaard EN 301 549 die verwijst naar WCAG versie 2.1.

De beschrijving van niet-functionele eisen moet expliciet aandacht besteden aan de door de beoogd beheerder gewenste ondersteuning van beheerfuncties. Bepaalde niet-functionele eisen kunnen aanleiding zijn tot het treffen van beveiligingsmaatregelen. Door deze eisen expliciet in de voorfase te benoemen, wordt voorkomen dat de bijbehorende beveiligingsmaatregelen achteraf moeten worden toegevoegd.

Overheidsorganisaties moeten een [toegankelijkheidsverklaring](https://www.digitoegankelijk.nl/wetgeving/toegankelijkheidsverklaring) op hun websites plaatsen. Indien gewenst ondersteunt ICTU bij het opstellen van de toegankelijkheidsverklaring.

Bronnen van de opdrachtgevende organisatie zoals procesbeschrijvingen, data protection impact assessment (DPIA), beheeracceptatiecriteria, beveiligingsbeleid en projectstartarchitectuur vormen het startpunt voor de niet-functionele eisen.

Beschikbare templates:

* [Template niet-functionele eisen]($BASE_URL$/$VERSIE$/Neutraal-Template-Niet-Functionele-Eisen.docx).

### Product backlog

De product backlog is een geprioriteerd overzicht van alle nog te realiseren functionele en niet-functionele eigenschappen van de software. Al het werk dat het Scrumteam doet loopt via de product backlog, niet alleen werk aan de broncode zelf maar bijvoorbeeld ook het schrijven van beheerdocumentatie. De product owner is de eigenaar van de product backlog. De zaken op de lijst zijn normaal gesproken in de vorm van een epic of user story. Hierin staat:

* _Wat_ er gemaakt moet worden,
* _Waarom_,
* en voor _wie_.

De product owner is verantwoordelijk voor de inhoud en bepaalt de prioritering van de eisen. Er staan ook ruwe schattingen bij van de waarde voor de organisatie en van de ontwikkelkosten.

Zie [https://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog](https://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog).

### Ontwerp- en architectuurdocumentatie

De ontwerp- en architectuurdocumentatie beschrijft de opzet van de te bouwen software in de context waarbinnen deze moet opereren en de ontwerpkeuzes en -principes die zijn gevolgd. Die documentatie laat tevens zien hoe de software aan de gestelde functionele en niet-functionele eisen voldoet.

Het project legt ontwerp- en architectuurinformatie vast in verschillende documenten en producten, zoals een softwarearchitectuurdocument (SAD), een infrastructuurarchitectuur (IA), een globaal functioneel ontwerp (GFO) en een prototype en/of interactieontwerp.

Het softwarearchitectuurdocument verschaft een compleet overzicht van de architectuur van de te ontwikkelen software, en de rationale hiervoor, waarbij diverse relevante views diverse aspecten van de software belichten. Zie bijvoorbeeld [https://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf](https://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf); andere manieren van architectuurbeschrijving zijn ook toegestaan.

De infrastructuurarchitectuur beschrijft de topologie van de implementatie-omgeving waaronder protocollen, beveiligingsniveaus en services. Deze architectuur biedt een logische afbeelding van de eisen naar de implementatie-omgeving en geeft onderbouwing voor de gemaakte keuzes.

Een prototype is een eerste, ruwe versie van de applicatie. Het prototype illustreert waar men uiteindelijk met de toepassing naar toe wil. Het maakt ideeën tastbaar en creëert een eerste indruk van structuur, ontwerp en functionaliteit.

Beschikbare templates:

* [Template globaal functioneel ontwerp]($BASE_URL$/$VERSIE$/ICTU-Template-Globaal-Functioneel-Ontwerp.docx).
* [Template softwarearchitectuurdocument]($BASE_URL$/$VERSIE$/ICTU-Template-Software-architectuurdocument.docx).
* [Template infrastructuurarchitectuur]($BASE_URL$/$VERSIE$/Neutraal-Template-Infrastructuurarchitectuur.docx).

### Testplannen en -rapportages

De testplannen bestaan uit een mastertestplan (MTP), gemaakt op basis van een productrisicoanalyse (PRA), en detailtestplannen. Het doel van een mastertestplan is om betrokkenen bij het testproces te informeren over de strategie, aanpak, activiteiten, inclusief de onderlinge relaties en afhankelijkheden, en de op te leveren producten met betrekking tot het testtraject. Het mastertestplan beschrijft deze strategie, aanpak, activiteiten en eindproducten, die in de detailtestplannen verder worden gedetailleerd.

De opdrachtgevende organisatie is verantwoordelijk voor het mastertestplan. Het project maakt een detailtestplan voor de testsoorten die tijdens de realisatiefase door het project worden uitgevoerd. Voor testen die onder verantwoordelijkheid van het project door een derde partij worden uitgevoerd, denk aan penetratietesten en evaluaties van gebruikskwaliteit, worden aparte detailtestplannen gemaakt. Deze hebben doorgaans de vorm van een offerteaanvraag gemaakt door ICTU en een offerte met plan van aanpak gemaakt door de leverancier.

Logische testgevallen worden vastgelegd en gekoppeld met use cases en user stories. Fysieke testgevallen worden vastgelegd in het formaat van de gebruikte tooling en gekoppeld met de logische testgevallen. Op basis hiervan worden testrapportages gegenereerd die laten zien dat alle use cases en user stories zijn getest en dat die tests zijn geslaagd.

Beschikbare templates:

* [Template mastertestplan]($BASE_URL$/$VERSIE$/Neutraal-Template-Mastertestplan.docx).
* [Template detailtestplan softwarerealisatie]($BASE_URL$/$VERSIE$/ICTU-Template-Detailtestplan-Softwarerealisatie.docx).

### Informatiebeveiligingsplan

Het informatiebeveiligingsplan vormt een praktisch toepasbaar document dat uitlegt binnen welke kaders bescherming geleverd wordt tegen welke dreigingen en met welke maatregelen die bescherming vorm krijgt. Belangrijkste bronnen voor het informatiebeveiligingsplan zijn de projectstartarchitectuur (PSA), business impact analyse (BIA), data protection impact assessment (DPIA) en de threat and vulnerability assessment (TVA).

Het Besluit Voorschrift Informatiebeveiliging Rijksdienst 2007 (VIR 2007) bevat een methode om te komen tot een systematische aanpak van informatiebeveiliging. Eén van de vereisten van het VIR 2007 is dat voor elk informatiesysteem en voor elk verantwoordelijkheidsgebied een afhankelijkheids- en kwetsbaarheidsanalyse (A&K-analyse) wordt uitgevoerd.

Bij ICTU wordt daarvoor een TVA gebruikt. Hierin worden de betrouwbaarheidseisen, die aan de bedrijfsprocessen en dientengevolge aan het informatiesysteem of verantwoordelijkheidsgebied worden gesteld, tijdens een afhankelijkheidsanalyse geïnventariseerd. Vervolgens worden de bedreigingen geïdentificeerd en geanalyseerd. De TVA levert zodoende een deel van een traceerbare onderbouwing voor de te treffen beveiligingsmaatregelen. De TVA wordt tijdens de voorfase opgesteld op basis van de PSA, de BIA, een eventuele DPIA en de inhoud van de ontwerp- en architectuurdocumentatie.

### Kwaliteitsplan

Het ICTU-kwaliteitsplan beschrijft de standaard kwaliteitsmaatregelen die ICTU-projecten treffen om software te realiseren die voldoet aan de kwaliteitseisen van de opdrachtgevende organisatie en andere belanghebbenden en aan de kwaliteitsnormen van ICTU.

Als er bijzondere of hoge niet-functionele eisen zijn, beschrijft het ICTU-kwaliteitsplan ook de extra projectspecifieke kwaliteitsmaatregelen die het project treft om deze eisen te realiseren.

Als de opdrachtgevende organisatie een overkoepelend kwaliteitsplan heeft zorgt het project dat het ICTU-kwaliteitsplan aansluit op het overkoepelende kwaliteitsplan.

Beschikbare templates:

* [Template kwaliteitsplan]($BASE_URL$/$VERSIE$/ICTU-Template-Kwaliteitsplan.docx).

### Deploybare versie van de software

Het project levert deploybare versies van de software in een formaat dat is afgestemd met de beheerorganisatie.

### Documentatie voor deployment en operationeel beheer

De deploymentdocumentatie bevat informatie over de eisen die een applicatie stelt aan een omgeving en de stappen die nodig zijn om de applicatie in die omgeving veilig te installeren en configureren. De documentatie bevat daartoe onder meer aanwijzingen voor de HTTP-header en -request-configuratie van de webserver en voor het verwijderen van overbodige header-informatie zoals de 'Server'-header. Ook zijn er aanwijzingen voor veilige configuratie(s) van (externe) toegang tot de beheerinterface. De documentatie bevat daarnaast in ieder geval een beschrijving van de protocollen en services die de applicatie aanbiedt, de protocollen, services en accounts die het product gebruikt en de protocollen, services en accounts die de applicatie gebruikt voor beheer.

De documentatie voor operationeel beheer bevat tenminste informatie over: back-up/recovery, procedures bij calamiteiten, regelmatig terugkerende beheeractiviteiten, opstart- en afsluitprocedures.

### Software bill of materials

Voor elke release stelt het project een "software bill of materials" op: een overzicht van de gebruikte libraries, frameworks, componenten en andere software(deel)producten in de release. Software draagt inherent het risico in zich van verborgen fouten. Deze fouten kunnen mogelijk misbruikt worden, waardoor (beveiligings)problemen ontstaan. Met dit overzicht heeft de opdrachtgevende organisatie of diens beheerorganisatie informatie over de gebruikte software(deel)producten, die geraadpleegd kan worden wanneer fouten in software bekend wordt, zodat een risico-inschatting gemaakt kan worden en eventueel actie kan worden ondernomen.

### Release notes

Voor elke release stelt het project release notes op: een overzicht van de wijzigingen in de release. Software delivery manager en opdrachtgever maken afspraken over de opzet van de release notes.

### Vrijgaveadvies

De opdrachtgevende organisatie organiseert dat voor elke release de betrokken partijen informatie aanleveren voor een vrijgaveadvies.

Het project levert bij elke release informatie aan de opdrachtgevende organisatie over nog openstaande testbevindingen en geconstateerde beveiligingsbevindingen; zie ook [$M26$](#m26) en [$M16$](#m16). Als er issues zijn, bijvoorbeeld rondom kwaliteit of beveiliging, zijn deze voorzien van een beschrijving van de voorziene impact.

### Aanvullende informatie

Waar mogelijk stelt de opdrachtgevende organisatie ook andere relevante informatie ter beschikking aan het project zoals een eventueel programma van eisen, procesbeschrijvingen van te ondersteunen bedrijfsprocessen, documentatie van te koppelen systemen en verder te hanteren kaders en richtlijnen.

### Samenhang voorfaseproducten

![Business impact analyse (BIA), data protection impact assessment (DPIA), impact assessment mensenrechten en algoritmes (IAMA) en projectstartarchitectuur (PSA) zijn input voor de voorfase. Functionele eisen (FE), niet-functionele eisen (NFE), informatiebeveiligingsplan (IB), product backlog (PB), ontwerp en architectuur (O&A), kwaliteitsplan (KP) en testplannen (TP) zijn de output van de voorfase. De relaties tussen de verschillende producten zijn als volgt. De business impact analyse, de data protection impact analyse en de impact assessment mensenrechten en algoritmes vormen input voor de PSA. De projectstartarchitectuur vormt input voor functionele eisen, niet-functionele eisen en informatiebeveiligingsplan. De functionele eisen vormen input voor de product backlog en voor ontwerp en architectuur. De niet-functionele eisen vormen input voor product backlog, ontwerp en architectuur en kwaliteitsplan. Het informatiebeveiligingsplan vormt input voor ontwerp en architectuur en kwaliteitsplan. De product backlog en ontwerp en architectuur, tenslotte, zijn input voor de testplannen.](relaties-tussen-producten.png "Relaties tussen producten")

Bovenstaande figuur laat de belangrijkste relaties zien tussen de verschillende producten die de input en output van de voorfase vormen. Naast de informatiestromen zoals door de pijlen weergegeven zijn er in de praktijk nog meer verbanden tussen de producten. Zo kan de gekozen oplossing in de architectuur van invloed zijn op de maatregelen in het informatiebeveiligingsplan of leiden niet-functionele eisen tot extra functionele eisen.

Omdat in de praktijk niet alle informatie uit business impact analyse, data protection impact assessment en impact assessment mensenrechten en algoritmes in detail in de projectstartarchitectuur kan worden opgenomen stelt opdrachtgever deze documenten ook ter beschikking aan het project. Projectmedewerkers kunnen zo deze documenten raadplegen bij het opstellen van de functionele en niet-functionele eisen en het informatiebeveiligingsplan.

### Rationale

Het uniformeren van op te leveren producten biedt voordelen voor planning (het is bekend welke producten gemaakt moeten worden), voor bemensing (het is bekend welke expertise nodig is) en voor het uitwisselen van medewerkers.

De genoemde producten die voor start beschikbaar zijn hebben tot doel om de benodigde omvang, kosten en doorlooptijd van de voorfase te kunnen schatten. De projectstartarchitectuur inclusief de daarvoor uitgevoerde assessments (BIA, DPIA en IAMA) vormen input voor de tijdens de voorfase te ontwikkelen producten zoals functionele en niet-functionele eisen, informatiebeveiligingsplan, functioneel ontwerp en softwarearchitectuur.

Als deze producten er niet zijn, niet actueel zijn, en/of niet compleet zijn, dan moeten ze in de voorfase alsnog worden gemaakt, bijgewerkt en/of aangevuld. Dit vereist grote betrokkenheid van de opdrachtgevende organisatie, en is in de regel lastig op korte termijn te organiseren.

De genoemde producten uit de voorfase hebben tot doel om enerzijds de omvang, kosten en doorlooptijd van de realisatiefase te kunnen schatten en anderzijds om de kaders voor de realisatiefase te bepalen, zodat de scope, aanpak en oplossingsrichting in grote lijnen bekend zijn.

De voorgeschreven producten uit de realisatiefase stellen de beheerorganisatie in staat om de opgeleverde software uit te rollen, te beheren en eventueel te onderhouden. Daarnaast is duidelijk welke eventueel openstaande punten er nog zijn. De voorgeschreven producten bieden voldoende verantwoording richting de ontvanger voor uitgevoerde werkzaamheden.
