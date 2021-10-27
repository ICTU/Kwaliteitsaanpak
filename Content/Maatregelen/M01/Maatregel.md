## $M01$

#include "Content/Maatregelen/M01/Definitie.md"

Opdrachtgever, ICTU, beheerpartij en andere meewerkende partijen, leveren samen de volgende informatie op:

**Plan van aanpak**
Het plan van aanpak voor de voorfase en het plan van aanpak voor de realisatiefase beschrijven de in deze fasen te realiseren producten, en de planning, werkwijze en verantwoordelijkheden voor de totstandkoming van die producten.

**Beschrijving van functionele eisen**
De beschrijving van functionele eisen bestaat uit epics en/of user stories, eventueel aangevuld met use cases. De beschrijving bevat tevens eisen voor ondersteuning van beheerfuncties, die door de beoogd beheerder gesteld worden, en voor logging, inclusief de globale inhoud van te loggen business events (gebeurtenissen op procesniveau) en de daarvoor geldende bewaartermijnen.

Bronnen van de opdrachtgever zoals de projectstartarchitectuur, een programma van eisen en procesbeschrijvingen vormen het startpunt voor de functionele eisen. Tijdens het project worden use cases in samenwerking met de product owner vertaald naar user stories.

**Beschrijving van niet-functionele eisen**
Niet-functionele eisen specificeren criteria om het functioneren van de software te beoordelen, maar beschrijven niet het specifieke gedrag zelf. Voor de beschrijving en onderverdeling van niet-functionele eisen gebruikt ICTU:

* NEN-ISO/IEC 25010,
* Wet beveiliging netwerk- en informatiesystemen (Wbni),
* Baseline Informatiebeveiliging Overheid (BIO),
* methode Grip op SDD (Secure Software Development) van het Centrum Informatiebeveiliging en Privacybescherming (CIP),
* Algemene verordening gegevensbescherming (AVG),
* ISO 9241-210:2019 Ergonomics of human-system interaction - Part 210: Human-centred design for interactive systems,
* hoofdstuk 9 van de Europese Standaard EN 301 549 — dit is gelijk aan de Web Content Accessibility Guidelines versie 2.1, niveau A en AA.

De beschrijving van niet-functionele eisen moet expliciet aandacht besteden aan de door de beoogd beheerder gewenste ondersteuning van beheerfuncties. Bepaalde niet-functionele eisen kunnen aanleiding zijn tot het treffen van beveiligingsmaatregelen. Door deze eisen expliciet in de voorfase te benoemen, wordt voorkomen dat de bijbehorende beveiligingsmaatregelen achteraf moeten worden toegevoegd.

Overheidsorganisaties moeten een [toegankelijkheidsverklaring](https://www.digitoegankelijk.nl/verklaring) op hun websites plaatsen. Indien gewenst ondersteunt ICTU bij het opstellen van de toegankelijkheidsverklaring.

Bronnen van de opdrachtgever zoals procesbeschrijvingen, privacy impact assessment (PIA), beheeracceptatiecriteria, beveiligingsbeleid en projectstartarchitectuur vormen het startpunt voor de niet-functionele eisen.

**Product backlog**
De product backlog is een geprioriteerd overzicht van alle nog te realiseren functionele en niet-functionele eigenschappen van de software. De product owner is de eigenaar van de product backlog. De zaken op de lijst zijn normaal gesproken in de vorm van een epic of user story. Hierin staat:

* *Wat* er gemaakt moet worden,
* *Waarom*,
* en voor *wie*.

De product owner is verantwoordelijk voor de inhoud en bepaalt de prioritering van de eisen. Er staan ook ruwe schattingen bij van de waarde voor de organisatie en van de ontwikkelkosten.

Zie [http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog](http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog).

**Ontwerp- en architectuurdocumentatie (software, interactie, infrastructuur)**
De ontwerp- en architectuurdocumentatie beschrijft de opzet van de te bouwen software in de context waarbinnen het moet opereren en de ontwerpkeuzes en -principes die zijn gevolgd. Die documentatie laat tevens zien hoe de software aan de gestelde functionele en niet-functionele eisen voldoet.

Het project legt ontwerp- en architectuurinformatie vast in verschillende documenten en producten, zoals een softwarearchitectuurdocument (SAD), een infrastructuurarchitectuur (IA), een globaal functioneel ontwerp (GFO) en een prototype en/of interactieontwerp.

Het softwarearchitectuurdocument verschaft een compleet overzicht van en rationale voor de architectuur van de te ontwikkelen software, waarbij diverse relevante views diverse aspecten van de software belichten. Zie bijvoorbeeld [http://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf); andere manieren van architectuurbeschrijving zijn ook toegestaan.

De infrastructuurarchitectuur beschrijft de topologie van de implementatie-omgeving waaronder protocollen, beveiligingsniveaus en services. Deze architectuur biedt een logische afbeelding van de eisen naar de implementatie-omgeving en geeft onderbouwing voor de gemaakte keuzes.

Een prototype is een eerste, ruwe versie van de applicatie. Het prototype illustreert waar men uiteindelijk met de toepassing naar toe wil. Het maakt ideeën tastbaar en creëert een eerste indruk van structuur, ontwerp en functionaliteit.

**Testdocumentatie**
De testplannen bestaan uit een mastertestplan (MTP), gemaakt op basis van een productrisicoanalyse (PRA), en detailtestplannen. Het doel van een mastertestplan is om betrokkenen bij het testproces te informeren over de strategie, aanpak, activiteiten, inclusief de onderlinge relaties en afhankelijkheden, en de op te leveren producten met betrekking tot het testtraject. Het mastertestplan beschrijft deze strategie, aanpak, activiteiten en eindproducten, die in de detailtestplannen verder worden gedetailleerd.

Opdrachtgever is verantwoordelijk voor het mastertestplan. ICTU maakt een detailtestplan voor de testsoorten die tijdens de realisatiefase door ICTU worden uitgevoerd. Voor testen die onder verantwoordelijkheid van ICTU door een derde partij worden uitgevoerd, denk aan penetratietesten en evaluaties van gebruikskwaliteit, worden aparte detailtestplannen gemaakt.

Logische testgevallen worden vastgelegd en gekoppeld met use cases en user stories. Fysieke testgevallen worden vastgelegd in het formaat van de gebruikte tooling en gekoppeld met de logische testgevallen. Op basis hiervan worden testrapportages gegenereerd die laten zien dat alle use cases en user stories zijn getest en dat die tests zijn geslaagd.

**Informatiebeveiligingsplan**
Het informatiebeveiligingsplan vormt een handzaam document dat uitlegt binnen welke kaders bescherming geleverd wordt tegen welke dreigingen en hoe die bescherming vorm krijgt. Mogelijke bronnen voor het informatiebeveiligingsplan zijn de business impact analysis (BIA), privacy impact assessment (PIA) en de threat and vulnerability assessment (TVA). De TVA wordt tijdens de voorfase opgesteld op basis van de resultaten van de BIA, de eventuele PIA en inhoud van de ontwerp- en architectuurdocumentatie. Een TVA levert een deel van een traceerbare onderbouwing voor de te treffen beveiligingsmaatregelen.

Het Besluit Voorschrift Informatiebeveiliging Rijksdienst 2007 (VIR 2007) bevat een methode om te komen tot een systematische aanpak van informatiebeveiliging. Eén van de vereisten van het VIR 2007 is dat voor elk informatiesysteem en voor elk verantwoordelijkheidsgebied een afhankelijkheids- en kwetsbaarheidsanalyse (A&K-analyse) wordt uitgevoerd. Bij ICTU wordt daarvoor een TVA gebruikt. De betrouwbaarheidseisen, die aan de bedrijfsprocessen en dientengevolge aan het informatiesysteem of verantwoordelijkheidsgebied worden gesteld, worden tijdens een afhankelijkheidsanalyse geïnventariseerd. Vervolgens worden de bedreigingen geïdentificeerd en geanalyseerd.

**Kwaliteitsplan**
Het kwaliteitsplan beschrijft de standaard kwaliteitsmaatregelen die ICTU-projecten treffen om goede kwaliteit software te realiseren. Als er bijzondere of hoge niet-functionele eisen zijn, beschrijft het kwaliteitsplan ook de extra projectspecifieke kwaliteitsmaatregelen die het project treft om deze eisen te realiseren.

**Deploybare versie van de software**
ICTU levert deploybare versies van de software in een formaat dat is afgestemd met de beheerpartij.

**Broncode, inclusief de benodigdheden voor het bouwen van de software**
ICTU levert de broncode, inclusief configuratiebestanden en buildscripts, nodig voor het bouwen van de software.

**Regressietests, inclusief de benodigdheden voor het uitvoeren van de tests**
ICTU levert de regressietests, inclusief configuratiebestanden en scripts nodig voor het uitoveren van de tests.

**Deploymentdocumentatie**
De deploymentdocumentatie bevat informatie over de eisen die een applicatie stelt aan een omgeving en de stappen die nodig zijn om de applicatie in die omgeving veilig te installeren en configureren. De documentatie bevat daartoe onder meer aanwijzingen voor de HTTP-header en -request-configuratie van de webserver en voor het verwijderen van overbodige header-informatie zoals de 'Server'-header. Ook zijn er aanwijzingen voor veilige configuratie(s) van (externe) toegang tot de beheerinterface. De documentatie bevat daarnaast in ieder geval een beschrijving van de protocollen en services die de applicatie aanbiedt, de protocollen, services en accounts die het product gebruikt en de protocollen, services en accounts die de applicatie gebruikt voor beheer.

**Release notes**
Voor elke release stelt het project release notes op; een overzicht van de wijzigingen in de release. ICTU en opdrachtgever maken afspraken over de opzet van de release notes.

**Vrijgaveadvies**
Voor elke release stelt het project een vrijgaveadvies op. Het vrijgaveadvies bevat tenminste alle nog openstaande testbevindingen en geconstateerde beveiligingsbevindingen; zie ook [$M26$](#m26) en [$M16$](#m16). Als er issues zijn, bijvoorbeeld rondom kwaliteit of beveiliging, zijn deze voorzien van een beschreven voorziene impact.

**Due diligence**
Als tijdens een project bestaande software dient te worden afgebouwd, onderhouden en/of herbouwd, vindt een onderzoek plaats naar de compleetheid en consistentie van de bestaande softwareproducten aan de hand van de onderstaande tabel (inclusief de deliverables in de kolom 'Realisatiefase') en wordt de kwaliteit van de bestaande softwareproducten getoetst. Dit onderzoek, dat bij ICTU een "due diligence" heet, is onderdeel van de voorfase en wordt uitgevoerd door vertegenwoordigers van ICTU en medewerkers van het desbetreffende project, samen met vertegenwoordigers van de opdrachtgever.

De uitkomsten van het onderzoek bestaan uit een rapportage met tenminste de bevindingen, risico's voor opdrachtgever en ICTU, en mitigerende maatregelen. Daarnaast maakt ICTU een transitieplan dat de activiteiten beschrijft die nodig zijn om de software af te bouwen of te herbouwen en te onderhouden. Als er significante technische schuld aanwezig is de bestaande software maakt ICTU een plan voor het aflossen van deze schuld.

**Samenhang voorfaseproducten**

![Projectstartarchitectuur, business impact analysis en privacy impact assessment zijn input voor de voorfase. Functionele eisen, niet-functionele eisen, informatiebeveiligingsplan, backlog, ontwerp en architectuur, kwaliteitsplan en testplannen zijn de output van de voorfase. De relaties tussen de verschillende producten zijn als volgt. De projectstartarchitectuur vormt input voor functionele eisen en niet-functionele eisen. De business impact analyse vormt input voor de niet-functionele eisen en informatiebeveiligingsplan. De privacy impact analyse vormt input voor de niet-functionele eisen en het informatiebeveiligingsplan. De functionele eisen vormen input voor de backlog en voor ontwerp en architectuur. De niet-functionele eisen vormen input voor backlog, ontwerp en architectuur en kwaliteitsplan. Het informatiebeveiligingsplan vormt input voor ontwerp en architectuur en kwaliteitsplan. De backlog en ontwerp en architectuur, tenslotte, zijn input voor de testplannen.](/work/Content/Images/relaties-tussen-producten.png "Relaties tussen producten")

Bovenstaande figuur laat de belangrijkste relaties zien tussen de verschillende producten die de input en output van de voorfase vormen. Naast de informatiestromen zoals door de pijlen weergegeven zijn er in de praktijk nog meer verbanden tussen de producten. Zo kan de gekozen oplossing in de architectuur van invloed zijn op de maatregelen in het informatiebeveiligingsplan of leiden niet-functionele eisen tot extra functionele eisen.

**Overzicht**
De onderstaande tabel bevat de hierboven genoemde producten en geeft aan in welke fase ze van belang zijn en worden opgeleverd, ook als ze zijn opgesteld door externe auteurs.

| Product                                                                             | Voorfase | Realisatiefase |
|---------------------------------------------------------------------------------------------------------|---|---|
| Plan van aanpak                                                                                         | ✔ | ✔ |
| Beschrijving van functionele eisen                                                                      | ✔ | ✔ |
| Beschrijving van niet-functionele eisen                                                                 | ✔ | ✔ |
| Product backlog                                                                                         | ✔ | ✔ |
| Ontwerp- en architectuurdocumentatie (software, interactie, infrastructuur)                             | ✔ | ✔ |
| Testdocumentatie: testplannen                                                                           | ✔ | ✔ |
| Testdocumentatie: testgevallen, rapportages                                                             |   | ✔ |
| Informatiebeveiligingsplan                                                                              | ✔ | ✔ |
| Kwaliteitsplan                                                                                          | ✔ | ✔ |
| Deploybare versie van de software                                                                       |   | ✔ |
| Broncode, inclusief de benodigdheden voor het bouwen van de software                                    |   | ✔ |
| Regressietests, inclusief de benodigdheden voor het uitvoeren van de tests                              |   | ✔ |
| Deploymentdocumentatie                                                                                  |   | ✔ |
| Release notes                                                                                           |   | ✔ |
| Vrijgaveadvies                                                                                          |   | ✔ |
| Bij due diligence: uitkomsten onderzoek (bevindingen, risico's, mitigerende maatregelen)                | ✔ |   |
| Bij due diligence: transitieplan voor af te bouwen, te onderhouden en/of te herbouwen softwareproducten | ✔ |   |
| Bij due diligence: plan voor aflossen technische schuld, indien van toepassing                          | ✔ |   |

**Verantwoordelijkheden**

De opdrachtgever is primair verantwoordelijk voor het beschrijven van de functionele en niet-functionele eisen, de geprioriteerde backlog, het mastertestplan en het informatiebeveiligingsplan.

ICTU is primair verantwoordelijk voor plan van aanpak, softwarearchitectuurdocumentatie, globaal functioneel ontwerp, prototype, detailtestplannen en testrapportages voor bouwtesten, kwaliteitsplan, deploybare versie van de software, broncode, regressietests, deploymentdocumentatie, release notes en vrijgaveadvies. Als er een due diligence plaatsvindt, levert ICTU de onderzoeksresultaten en maakt een transitieplan, en indien van toepassing, een plan voor het aflossen van technische schuld.

De beheerpartij is primair verantwoordelijk voor de infrastructuurarchitectuur en -ontwerp en detailtestplannen en testrapportages voor infrastructuurtesten.

### Rationale

Het uniformeren van op te leveren producten biedt voordelen voor planning (het is bekend welke producten gemaakt moeten worden), voor bemensing (het is bekend welke expertise nodig is) en voor het uitwisselen van medewerkers.

De voorgeschreven producten stellen de beheerpartij in staat om de opgeleverde software uit te rollen, te beheren en eventueel te onderhouden. Daarnaast is duidelijk welke eventueel openstaande punten er nog zijn. De voorgeschreven producten bieden voldoende verantwoording richting de ontvanger voor uitgevoerde werkzaamheden.

De genoemde producten uit de voorfase hebben tot doel om enerzijds de omvang, kosten en doorlooptijd van de realisatiefase te kunnen schatten en anderzijds om de kaders voor de realisatiefase te bepalen, zodat de scope, aanpak en oplossingsrichting in grote lijnen bekend zijn.

### Referenties

Zie ook:

* [$M14$](#m14)
* [$M31$](#m31)
