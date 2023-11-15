## $M01$

#include "Content/Maatregelen/M01/Definitie.md"

Opdrachtgever, ICTU, beheerorganisatie en andere meewerkende partijen leveren de onderstaande informatie op. Voor een aantal documenten zijn als onderdeel van de Kwaliteitsaanpak templates beschikbaar. Ook kan gebruik worden gemaakt van bestaande templates uit bijvoorbeeld de NORA. Zie [$M29$](#m29).

De onderstaande tabel bevat de in deze paragraaf beschreven producten. Het ✔ geeft aan in welke fase ze worden opgeleverd.

| Product                                                                     | Voor start | Voorfase | Realisatiefase |
|-----------------------------------------------------------------------------|------------|----------|----------------|
| Plan van aanpak: voorfase                                                   | ✔          |          |                |
| Beschrijving van functionele eisen                                          |            | ✔        | ✔              |
| Beschrijving van niet-functionele eisen                                     |            | ✔        | ✔              |
| Product backlog                                                             |            | ✔        | ✔              |
| Ontwerp- en architectuurdocumentatie (software, interactie, infrastructuur) |            | ✔        | ✔              |
| Mastertestplan                                                              |            | ✔        | ✔              |
| Detailtestplannen                                                           |            | ✔        | ✔              |
| Informatiebeveiligingsplan                                                  |            | ✔        | ✔              |
| Kwaliteitsplan                                                              |            | ✔        | ✔              |
| Plan van aanpak: realisatiefase                                             |            | ✔        |                |
| Deploybare versie van de software                                           |            |          | ✔              |
| Testrapportages                                                             |            |          | ✔              |
| Documentatie voor deployment en operationeel beheer                         |            |          | ✔              |
| Software bill of materials                                                  |            |          | ✔              |
| Release notes                                                               |            |          | ✔              |
| Vrijgaveadvies                                                              |            |          | ✔              |

### Plan van aanpak

Het plan van aanpak voor de voorfase en het plan van aanpak voor de realisatiefase beschrijven de in deze fasen te realiseren producten en diensten, en de planning, werkwijze en verantwoordelijkheden voor de totstandkoming van die producten en diensten.

Als operationeel en/of applicatiebeheer onderdeel is van de te leveren dienstverlening tijdens de realisatiefase bevat het plan van aanpak voor de realisatiefase de hiervoor noodzakelijke afspraken met de opdrachtgever en de beheerorganisatie. De afspraken omvatten zowel de te behalen kwaliteitsniveaus van de dienstverlening als de uit te voeren operationele en applicatiebeheertaken. Daarnaast beschrijft het plan hoe informatie zal worden verzameld over de software tijdens het gebruik en over de uitgevoerde beheeractiviteiten. En hoe hierover zal worden gerapporteerd. Ook worden de criteria voor het beëindigen van de dienstverlening vastgelegd. De te leveren dienstverlening is afgestemd op het beheerplan van de beheerorganisatie.

### Beschrijving van functionele eisen

De beschrijving van functionele eisen bestaat uit epics en/of user stories, eventueel aangevuld met use cases. De beschrijving bevat tevens eisen voor ondersteuning van beheerfuncties, die door de beoogd beheerder gesteld worden, en voor logging, inclusief de globale inhoud van te loggen business events (gebeurtenissen op procesniveau) en de daarvoor geldende bewaartermijnen.

Bronnen van de opdrachtgever zoals de projectstartarchitectuur, een programma van eisen en procesbeschrijvingen vormen het startpunt voor de functionele eisen. Tijdens het project worden use cases in samenwerking met de product owner vertaald naar epics en user stories.

### Beschrijving van niet-functionele eisen

Niet-functionele eisen specificeren criteria om het functioneren van de software te beoordelen, maar beschrijven niet het specifieke gedrag zelf. Voor de beschrijving en onderverdeling van niet-functionele eisen maakt het project gebruik van:

* NEN-ISO/IEC 25010,
* Wet beveiliging netwerk- en informatiesystemen (Wbni),
* Baseline Informatiebeveiliging Overheid (BIO),
* methode Grip op SDD (Secure Software Development) van het Centrum Informatiebeveiliging en Privacybescherming (CIP),
* Algemene verordening gegevensbescherming (AVG),
* ISO 9241-210:2019 Ergonomics of human-system interaction - Part 210: Human-centred design for interactive systems,
* hoofdstuk 9 van de Europese Standaard EN 301 549 — dit is gelijk aan de Web Content Accessibility Guidelines versie 2.1, niveau A en AA.

De beschrijving van niet-functionele eisen moet expliciet aandacht besteden aan de door de beoogd beheerder gewenste ondersteuning van beheerfuncties. Bepaalde niet-functionele eisen kunnen aanleiding zijn tot het treffen van beveiligingsmaatregelen. Door deze eisen expliciet in de voorfase te benoemen, wordt voorkomen dat de bijbehorende beveiligingsmaatregelen achteraf moeten worden toegevoegd.

Overheidsorganisaties moeten een [toegankelijkheidsverklaring](https://www.digitoegankelijk.nl/wetgeving/toegankelijkheidsverklaring) op hun websites plaatsen. Indien gewenst ondersteunt ICTU bij het opstellen van de toegankelijkheidsverklaring.

Bronnen van de opdrachtgever zoals procesbeschrijvingen, privacy impact assessment (PIA), beheeracceptatiecriteria, beveiligingsbeleid en projectstartarchitectuur vormen het startpunt voor de niet-functionele eisen.

### Product backlog

De product backlog is een geprioriteerd overzicht van alle nog te realiseren functionele en niet-functionele eigenschappen van de software. Al het werk dat het Scrumteam doet loopt via de backlog, niet alleen werk aan de broncode zelf maar bijvoorbeeld ook het schrijven van beheerdocumentatie. De product owner is de eigenaar van de product backlog. De zaken op de lijst zijn normaal gesproken in de vorm van een epic of user story. Hierin staat:

* _Wat_ er gemaakt moet worden,
* _Waarom_,
* en voor _wie_.

De product owner is verantwoordelijk voor de inhoud en bepaalt de prioritering van de eisen. Er staan ook ruwe schattingen bij van de waarde voor de organisatie en van de ontwikkelkosten.

Zie [https://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog](https://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog).

### Ontwerp- en architectuurdocumentatie (software, interactie, infrastructuur)

De ontwerp- en architectuurdocumentatie beschrijft de opzet van de te bouwen software in de context waarbinnen deze moet opereren en de ontwerpkeuzes en -principes die zijn gevolgd. Die documentatie laat tevens zien hoe de software aan de gestelde functionele en niet-functionele eisen voldoet.

Het project legt ontwerp- en architectuurinformatie vast in verschillende documenten en producten, zoals een softwarearchitectuurdocument (SAD), een infrastructuurarchitectuur (IA), een globaal functioneel ontwerp (GFO) en een prototype en/of interactieontwerp.

Het softwarearchitectuurdocument verschaft een compleet overzicht van de architectuur van de te ontwikkelen software, en de rationale hiervoor, waarbij diverse relevante views diverse aspecten van de software belichten. Zie bijvoorbeeld [https://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf](https://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf); andere manieren van architectuurbeschrijving zijn ook toegestaan.

De infrastructuurarchitectuur beschrijft de topologie van de implementatie-omgeving waaronder protocollen, beveiligingsniveaus en services. Deze architectuur biedt een logische afbeelding van de eisen naar de implementatie-omgeving en geeft onderbouwing voor de gemaakte keuzes.

Een prototype is een eerste, ruwe versie van de applicatie. Het prototype illustreert waar men uiteindelijk met de toepassing naar toe wil. Het maakt ideeën tastbaar en creëert een eerste indruk van structuur, ontwerp en functionaliteit.

### Testplannen en -rapportages

De testplannen bestaan uit een mastertestplan (MTP), gemaakt op basis van een productrisicoanalyse (PRA), en detailtestplannen. Het doel van een mastertestplan is om betrokkenen bij het testproces te informeren over de strategie, aanpak, activiteiten, inclusief de onderlinge relaties en afhankelijkheden, en de op te leveren producten met betrekking tot het testtraject. Het mastertestplan beschrijft deze strategie, aanpak, activiteiten en eindproducten, die in de detailtestplannen verder worden gedetailleerd.

Opdrachtgever is verantwoordelijk voor het mastertestplan. Het project maakt een detailtestplan voor de testsoorten die tijdens de realisatiefase door het project worden uitgevoerd. Voor testen die onder verantwoordelijkheid van het project door een derde partij worden uitgevoerd, denk aan penetratietesten en evaluaties van gebruikskwaliteit, worden aparte detailtestplannen gemaakt.

Logische testgevallen worden vastgelegd en gekoppeld met use cases en user stories. Fysieke testgevallen worden vastgelegd in het formaat van de gebruikte tooling en gekoppeld met de logische testgevallen. Op basis hiervan worden testrapportages gegenereerd die laten zien dat alle use cases en user stories zijn getest en dat die tests zijn geslaagd.

### Informatiebeveiligingsplan

Het informatiebeveiligingsplan vormt een praktisch toepasbaar document dat uitlegt binnen welke kaders bescherming geleverd wordt tegen welke dreigingen en met welke maatregelen die bescherming vorm krijgt. Mogelijke bronnen voor het informatiebeveiligingsplan zijn de business impact analysis (BIA), privacy impact assessment (PIA) en de threat and vulnerability assessment (TVA).

Het Besluit Voorschrift Informatiebeveiliging Rijksdienst 2007 (VIR 2007) bevat een methode om te komen tot een systematische aanpak van informatiebeveiliging. Eén van de vereisten van het VIR 2007 is dat voor elk informatiesysteem en voor elk verantwoordelijkheidsgebied een afhankelijkheids- en kwetsbaarheidsanalyse (A&K-analyse) wordt uitgevoerd.

Bij ICTU wordt daarvoor een TVA gebruikt. Hierin worden de betrouwbaarheidseisen, die aan de bedrijfsprocessen en dientengevolge aan het informatiesysteem of verantwoordelijkheidsgebied worden gesteld, tijdens een afhankelijkheidsanalyse geïnventariseerd. Vervolgens worden de bedreigingen geïdentificeerd en geanalyseerd. De TVA levert zodoende een deel van een traceerbare onderbouwing voor de te treffen beveiligingsmaatregelen. De TVA wordt tijdens de voorfase opgesteld op basis van de resultaten van de BIA, de eventuele PIA en de inhoud van de ontwerp- en architectuurdocumentatie.

### Kwaliteitsplan

Het ICTU-kwaliteitsplan beschrijft de standaard kwaliteitsmaatregelen die ICTU-projecten treffen om software te realiseren die voldoet aan de kwaliteitseisen van de opdrachtgever en andere belanghebbenden en aan de kwaliteitsnormen van ICTU.

Als er bijzondere of hoge niet-functionele eisen zijn, beschrijft het ICTU-kwaliteitsplan ook de extra projectspecifieke kwaliteitsmaatregelen die het project treft om deze eisen te realiseren.

Als de opdrachtgever een overkoepelend kwaliteitsplan heeft zorgt het project dat het ICTU-kwaliteitsplan aansluit op het overkoepelende kwaliteitsplan.

### Deploybare versie van de software

Het project levert deploybare versies van de software in een formaat dat is afgestemd met de beheerorganisatie.

### Documentatie voor deployment en operationeel beheer

De deploymentdocumentatie bevat informatie over de eisen die een applicatie stelt aan een omgeving en de stappen die nodig zijn om de applicatie in die omgeving veilig te installeren en configureren. De documentatie bevat daartoe onder meer aanwijzingen voor de HTTP-header en -request-configuratie van de webserver en voor het verwijderen van overbodige header-informatie zoals de 'Server'-header. Ook zijn er aanwijzingen voor veilige configuratie(s) van (externe) toegang tot de beheerinterface. De documentatie bevat daarnaast in ieder geval een beschrijving van de protocollen en services die de applicatie aanbiedt, de protocollen, services en accounts die het product gebruikt en de protocollen, services en accounts die de applicatie gebruikt voor beheer.

De documentatie voor operationeel beheer bevat tenminste informatie over: back-up/recovery, procedures bij calamiteiten, regelmatig terugkerende beheeractiviteiten, opstart- en afsluitprocedures.

### Software bill of materials

Voor elke release stelt het project een "software bill of materials" op: een overzicht van de gebruikte libraries, frameworks, componenten en andere software(deel)producten in de release. Software draagt inherent het risico in zich van verborgen fouten. Deze fouten kunnen mogelijk misbruikt worden, waardoor (beveiligings)problemen ontstaan. Met dit overzicht heeft de opdrachtgever of diens beheerorganisatie informatie over de gebruikte software(deel)producten, die geraadpleegd kan worden wanneer fouten in software bekend wordt, zodat een risico-inschatting gemaakt kan worden en eventueel actie kan worden ondernomen.

### Release notes

Voor elke release stelt het project release notes op: een overzicht van de wijzigingen in de release. Software delivery manager en opdrachtgever maken afspraken over de opzet van de release notes.

### Vrijgaveadvies

Voor elke release stelt het project een vrijgaveadvies op. Het vrijgaveadvies bevat tenminste alle nog openstaande testbevindingen en geconstateerde beveiligingsbevindingen; zie ook [$M26$](#m26) en [$M16$](#m16). Als er issues zijn, bijvoorbeeld rondom kwaliteit of beveiliging, zijn deze voorzien van een beschrijving van de voorziene impact.

Software delivery manager en opdrachtgever maken afspraken over de opzet van het vrijgaveadvies en de verantwoordelijkheden van betrokken partijen bij de totstandkoming ervan, waaronder ook de beheerorganisatie.

### Samenhang voorfaseproducten

![Projectstartarchitectuur (PSA), business impact analysis (BIA) en privacy impact assessment (PIA) zijn input voor de voorfase. Functionele eisen (FE), niet-functionele eisen (NFE), informatiebeveiligingsplan (IB), backlog (BL), ontwerp en architectuur (O&A), kwaliteitsplan (KP) en testplannen (TP) zijn de output van de voorfase. De relaties tussen de verschillende producten zijn als volgt. De projectstartarchitectuur vormt input voor functionele eisen en niet-functionele eisen. De business impact analyse vormt input voor de niet-functionele eisen en informatiebeveiligingsplan. De privacy impact analyse vormt input voor de niet-functionele eisen en het informatiebeveiligingsplan. De functionele eisen vormen input voor de backlog en voor ontwerp en architectuur. De niet-functionele eisen vormen input voor backlog, ontwerp en architectuur en kwaliteitsplan. Het informatiebeveiligingsplan vormt input voor ontwerp en architectuur en kwaliteitsplan. De backlog en ontwerp en architectuur, tenslotte, zijn input voor de testplannen.](relaties-tussen-producten.png "Relaties tussen producten")

Bovenstaande figuur laat de belangrijkste relaties zien tussen de verschillende producten die de input en output van de voorfase vormen. Naast de informatiestromen zoals door de pijlen weergegeven zijn er in de praktijk nog meer verbanden tussen de producten. Zo kan de gekozen oplossing in de architectuur van invloed zijn op de maatregelen in het informatiebeveiligingsplan of leiden niet-functionele eisen tot extra functionele eisen.

### Verantwoordelijkheden

De opdrachtgever is primair verantwoordelijk voor het beschrijven van de functionele en niet-functionele eisen, de geprioriteerde backlog, het mastertestplan en het informatiebeveiligingsplan.

ICTU is primair verantwoordelijk voor plan van aanpak, softwarearchitectuurdocumentatie, globaal functioneel ontwerp, prototype, detailtestplannen en testrapportages voor bouwtesten, kwaliteitsplan, deploybare versie van de software, documentatie voor deployment en operationeel beheer, release notes en vrijgaveadvies.

Als tijdens een project bestaande software dient te worden afgebouwd, onderhouden en/of herbouwd, vindt een onderzoek plaats naar de kwaliteit van deze software, zie [$M32$](#m32). In dat geval levert het project ook de onderzoeksresultaten daarvan en maakt een transitieplan, en indien van toepassing, een plan voor het aflossen van technische schuld.

De beheerorganisatie is primair verantwoordelijk voor de infrastructuurarchitectuur en -ontwerp en detailtestplannen en testrapportages voor infrastructuurtesten.

### Rationale

Het uniformeren van op te leveren producten biedt voordelen voor planning (het is bekend welke producten gemaakt moeten worden), voor bemensing (het is bekend welke expertise nodig is) en voor het uitwisselen van medewerkers.

De voorgeschreven producten stellen de beheerorganisatie in staat om de opgeleverde software uit te rollen, te beheren en eventueel te onderhouden. Daarnaast is duidelijk welke eventueel openstaande punten er nog zijn. De voorgeschreven producten bieden voldoende verantwoording richting de ontvanger voor uitgevoerde werkzaamheden.

De genoemde producten uit de voorfase hebben tot doel om enerzijds de omvang, kosten en doorlooptijd van de realisatiefase te kunnen schatten en anderzijds om de kaders voor de realisatiefase te bepalen, zodat de scope, aanpak en oplossingsrichting in grote lijnen bekend zijn.
