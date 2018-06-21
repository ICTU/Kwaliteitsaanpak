### Documenten voor Maatregel 1: Op te leveren producten

ICTU hanteert de onderstaande documenten en documentstandaarden in de voorbereidingsfase.

#### Geprioriteerde backlog

De product backlog is een overzicht van alle nog te realiseren functionele en niet-functionele eigenschappen van de software. De product owner is de eigenaar van de product backlog. De zaken op de lijst zijn normaal gesproken in de vorm van een epic of user story. Hierin staat:

- WAT er gemaakt moet worden
- WAAROM
- en voor WIE.

Iedereen kan er dingen aan toevoegen, maar de product owner is en blijft verantwoordelijk. Er staan ook ruwe schattingen bij van de waarde voor de organisatie en van de ontwikkelkosten. De product owner bepaalt de volgorde (en dus prioritering) van de items op de backlog.

Zie [http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog](http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog).

#### Beschrijving van functionele eisen

De beschrijving van functionele eisen moet expliciet aandacht besteden aan de door de beoogd beheerder gewenste ondersteuning van beheerfuncties en aan logging. Functionele eisen op deze vlakken kunnen aanleiding zijn tot het treffen van beveiligingsmaatregelen. Door ook deze eisen expliciet in de voorfase te benoemen wordt voorkomen dat de bijbehorende beveiligingsmaatregelen achteraf moeten worden toegevoegd.

#### Beschrijving van niet-functionele eisen

Niet-functionele eisen (requirements) specificeren criteria om het functioneren van het systeem te beoordelen, maar beschrijven niet het specifieke gedrag zelf. Deze niet-functionele requirements kunnen verder onderverdeeld worden in requirements betreffende performance, onderhoud, veiligheid, betrouwbaarheid, of menig ander aspect.

ICTU gebruikt in ieder geval ISO 25010, het normenkader van de Baseline Informatiebeveiliging Rijksdienst (BIR:2017) en Secure Software Development van Centrum voor Informatiebeveiliging en Privacybescherming om de niet-functionele requirements te structureren en inventariseren. De niet-functionele eisen zijn geprioriteerd.

De beschrijving van niet-functionele eisen moet expliciet aandacht besteden aan de door de beoogd beheerder gewenste ondersteuning van beheerfuncties, aan logging en aan het gewenste gedrag van de te realiseren software bij uitval van infrastructurele diensten zoals een log server. Niet-functionele eisen op deze vlakken kunnen aanleiding zijn tot het treffen van beveiligingsmaatregelen. Door deze eisen expliciet in de voorfase te benoemen wordt voorkomen dat de bijbehorende beveiligingsmaatregelen achteraf moeten worden toegevoegd.

#### Ontwerp- en architectuurdocumentatie (software, interactie, infrastructuur)

De ontwerp- en architectuurdocumentatie bestaat uit een projectstartarchitectuur (PSA), een softwarearchitectuurdocument (SAD), een infrastructuurarchitectuur (IA), een globaal functioneel ontwerp (GFO) en een prototype en/of interactieontwerp.

##### Projectstartarchitectuur (PSA) op basis van NORA

Een PSA (Project Start Architectuur) is bedoeld om te borgen dat nieuwe ontwikkelingen en veranderingen in samenhang worden gerealiseerd en passen binnen de toekomstig gewenste informatievoorziening.

Een PSA bevat in ieder geval:

- Een beschrijving van de doelen en ambities waaraan het project bijdraagt en invulling geeft. Dus niet de projectdoelen en -ambitie!
- Een afbakening van het project en de context van de voorziening/oplossing die het project gaat realiseren gezien als een 'black box'. Denk o.a. ook aan relaties met andere projecten en generieke en specifieke diensten (services).
- De belangrijkste functies van de door het project te realiseren voorziening, informatiestromen en koppelvlakken.
- Een beschrijving van de belangrijkste betrokken stakeholders en/of ketenpartijen. een concretisering van van toepassing zijnde kaders en randvoorwaarden.
- Beleidsuitgangspunten (drijfveren en doelen), zowel voor het specifieke project als algemeen voor de organisatie en visie (oplossingsrichting).
- Standaarden en normen (open standaarden van het Forum Standaardisatie en domeinspecifieke standaarden).

Zie [http://www.noraonline.nl/wiki/PSA_(Project_Startarchitectuur)](http://www.noraonline.nl/wiki/PSA_(Project_Startarchitectuur)).

##### Software architectuur document (SAD)

Het Software Architectuur Document verschaft een compleet overzicht van en rationale voor de architectuur van het te bouwen systeem, waarbij diverse relevante views (zoals use-case, logisch, implementatie, deployment) diverse aspecten van het systeem belichten.

Zie bijvoorbeeld: [http://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Kruchten-4+1-view.pdf).

##### Infrastructuurarchitectuur

De infrastructuurarchitectuur beschrijft de topologie van de implementatie-omgeving waaronder protocollen, beveiligingsniveaus en services. Deze architectuur biedt een logische afbeelding van eisen naar implementatie-omgeving en geeft onderbouwing voor gemaakte keuzes.

##### Globaal functioneel ontwerp (GFO)

Het globaal functioneel ontwerp heeft als belangrijkste onderdeel een use case model. Een use case model is een overkoepelend overzicht van de onderkende actoren en use cases, hun samenhang, gewicht en classificatie. Per onderkende use case is er een nauwkeurig geformuleerde maar beknopte beschrijving. Use cases worden gedurende het project nader gedetailleerd.

Zie bijvoorbeeld: [https://www.ivarjacobson.com/sites/default/files/field_iji_file/article/use-case_2_0_jan11.pdf]( [https://www.ivarjacobson.com/sites/default/files/field_iji_file/article/use-case_2_0_jan11.pdf).

##### Prototype

Een prototype is een eerste, ruwe versie van de applicatie. Het prototype illustreert waar men uiteindelijk met de toepassing naar toe wil. Het maakt ideëen tastbaar en creëert een eerste indruk van structuur, design en functionaliteit.

#### Testdocumentatie: testplannen

De testplannen bestaan uit een master testplan, gemaakt op basis van een productrisicoanalyse (PRA), en detailtestplannen. Het doel van een mastertestplan (MTP) is om betrokkenen bij het testproces te informeren over de aanpak, de activiteiten, inclusief de onderlinge relaties en afhankelijkheden, en de op te leveren (eind)producten met betrekking tot het testtraject. Het mastertestplan beschrijft deze aanpak, activiteiten en (eind)producten welke in de verschillende andere (detail)testplannen verder dienen te worden gedetailleerd. Deze (detail)testplannen dienen te worden afgeleid van dit mastertestplan. ICTU gebruikt een generiek mastertestplan als basis voor projectspecifieke mastertestplannen.

#### Testdocumentatie: testgevallen, rapportages

Logische testgevallen worden vastgelegd in Jira en gekoppeld met use cases en user stories. Fysieke testgevallen worden vastgelegd in het formaat van de gebruikte tooling (bijvoorbeeld TestX) en gekoppeld met de logische testgevallen. Op basis hiervan worden testrapportages gegenereerd die laten zien dat alle use cases en user stories zijn getest en dat die tests zijn geslaagd.

#### Informatiebeveiligingsplan

Het IB-plan vormt een handzaam document dat uitlegt binnen welke kaders bescherming geleverd wordt tegen welke dreigingen en hoe die bescherming vorm krijgt. Naast BIA, eventuele PIA en TVA krijgen ook de geselecteerde IB-maatregelen een plaats in dit document.

Het Voorschrift Informatiebeveiliging Rijksdienst (VIR) bevat een methode om te komen tot een systematische aanpak van informatiebeveiliging. Eén van de vereisten van het VIR is dat voor elk informatiesysteem en voor elk verantwoordelijkheidsgebied een afhankelijkheids- en kwetsbaarheidsanalyse (A&K-analyse) wordt uitgevoerd. Bij ICTU wordt daarvoor een TVA (threat and vulnerability assessment) gebruikt. De betrouwbaarheidseisen, die aan de bedrijfsprocessen en dientengevolge aan het informatiesysteem of verantwoordelijkheidsgebied worden gesteld, worden tijdens een afhankelijkheidsanalyse geïnventariseerd. Vervolgens worden de bedreigingen geïdentificeerd en geanalyseerd.

Op basis van de resultaten van de TVA wordt voor elk informatiesysteem en voor elk verantwoordelijkheidsgebied een informatiebeveiligingsplan opgesteld.

#### Kwaliteitsplan

Het kwaliteitsplan beschrijft welke maatregelen de projectenorganisatie treft om de niet-functionele eisen te realiseren. ICTU gebruikt een generiek kwaliteitsplan als basis voor projectspecifieke kwaliteitsplannen.
