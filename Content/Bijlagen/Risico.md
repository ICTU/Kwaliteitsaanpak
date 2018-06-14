### Risico's van softwareontwikkeling

Softwareontwikkeling brengt risico's met zich mee. De ICTU Softwarerealisatie Kwaliteitsaanpak beoogt een deel van die risico's te mitigeren. Als raamwerk en startpunt voor het classificeren van risico's maakt de kwaliteitsaanpak gebruik van *Taxonomy-Based Risk Identification* van het Software Engineering Institute (CMU/SEI-93-TR-6), een taxonomie van risico's.

Deze bijlage geeft eerst een overzicht van de taxonomie van risico's en vervolgens een lijst van veelvoorkomende risico's. Voor elk van die risico's is aangegeven door welke maatregel(en) uit de kwaliteitsaanpak ze worden verminderd en geclassificeerd bij welke onderdelen van de risicotaxonomie ze horen. Hoe en waarom de maatregelen de risico's precies verminderen moet nog worden uitgewerkt.

#### Gebruik van de risicotaxonomie

De taxonomie benoemt zelf geen risico's, maar is een middel om risico's te ordenen. Naast het kunnen classificeren van risico's biedt het gebruik van de taxonomie de volgende voordelen:

- Eenduidige terminologie: de taxonomie bestaat uit een lijst van begrippen met een vaste betekenis, die het mogelijk maakt om risico's te vergelijken en te classificeren.

- Controle op volledigheid: voor elk element uit de taxonomie kan de vraag gesteld worden “bevat de kwaliteitsaanpak maatregelen voor risico's bij dit element?”

- Betere rationale: door aan te geven op welke in de taxonomie genoemde risicogebieden een maatregel betrekking heeft is duidelijker wat de maatregel beoogt te bereiken.

#### Risicotaxonomie

1. Productontwikkeling
    1. Requirements
        1. Stabiliteit: de mate waarin requirements veranderen en de mate waarin veranderende requirements invloed hebben op de kwaliteit, de functionaliteit, de planning, het ontwerp, de integratie en het testen van het product.
        2. Volledigheid: de volledigheid van requirements en de mate waarin op basis van ongecontroleerde aannames moet worden gewerkt.
        3. Duidelijkheid: de mate waarin requirements duidelijk, precies en niet ambigu zijn.
        4. Validiteit: de mate waarin de verzamelde requirements overeenstemmen met de intenties van de opdrachtgever, bijvoorbeeld veroorzaakt door misverstanden of ongeschreven, impliciete verwachtingen.
        5. Haalbaarheid: de complexiteit van requirements of de aanwezigheid van tegenstrijdige requirements.
        6. Precedent: systeemeigenschappen en -functies die nog niet eerder succesvol zijn geïmplementeerd in een bestaand systeem of buiten de ervaring van de medewerkers of de organisatie liggen.
        7. Schaal: de invloed van de schaal van het te realiseren product, of de omstandigheden waaronder dat moet plaatsvinden, op techniek en beheersing.
    2. Ontwerp
        1. Functionaliteit: het omzetten van functionele requirements naar een realiseerbaar en aantoonbaar werkend ontwerp of algoritme.
        2. Complexiteit: de complexiteit van functionele requirements of ontwerprequirements.
        3. Interfaces: alle software en hardware interfaces binnen de scope van het project vallen.
        4. Performance: de performance-eisen, zoals responstijd en throughput, die aan het product worden gesteld.
        5. Testbaarheid: de geschiktheid van het ontwerp om getest te worden, de aanwezigheid van faciliteiten om testen te faciliteren en de betrokkenheid van testers bij het ontwerpproces.
        6. Hardware-eisen: eisen met betrekking tot de hardware waarop het product moet draaien en de afhankelijkheid van hardware om systeem- en performance-eisen te halen.
        7. Software van derden: de inzet van extern verkregen software die niet ontworpen is volgens de productrequirements en de mate waarin die externe software aantoonbaar voldoet aan de requirements.
    3. Code en Unit Test
        1. Uitvoerbaarheid: de invloed van de kwaliteit of complexiteit van ontwerp of specificatie op de mate waarin tests zijn uit te voeren.
        2. Unit Test: de mate waarin unit testing is voorzien, gepland en gefaciliteerd met testgevallen.
        3. Coding/Implementatie: de gevolgen van beperkingen bij implementatie, zoals te trage hardware, te weinig geheugen, vereiste programmeertalen en verschillen tussen ontwikkelomgeving en productieomgeving.
    4. Integratie en Test
        1. Omgeving: de hardware- en software- faciliteiten ten behoeve van integratie en test en de aanwezigheid van rresentatieve testgevallen.
        2. Productintegratie: de integratie van softwarecomponenten onderling en met het doelplatform en het testen van het contractueel op te leveren volledige product.
        3. Systeemintegratie: de integratie van het eindproduct met andere systemen en sites.
    5. Specialiteiten
        1. Onderhoudbaarheid: de effecten van slechte softwarearchitectuur, ontwerp, code of documentatie op onderhoudbaarheid of het gebrek aan analyse van onderhoudbaarheid.
        2. Betrouwbaarheid: de invloed van hardware op betrouwbaarheids- en beschikbaarheidseisen op het eindproduct en de mate waarin die eisen onafhankelijk van de hardware opgesteld en testbaar zijn.
        3. Veiligheid: de complexiteit van veiligheidseisen en de mate waarin die in een gesimuleerde onveilige situatie getoetst kunnen worden.
        4. Beveiliging: de ervaring met en mogelijke onderschatting van eisen met betrekking tot beveiliging, verificatiemethoden en certificering.
        5. Menselijke Factoren: kennis van de operationele omgeving van het eindproduct en de mate waarin verwachtingen van opdrachtgever en gebruikers zijn opgenomen in de requirements en zijn afgestemd.
        6. Specificaties: de specificaties van het systeem, de hardware, de software, de koppelvlakken, de mate waarin die stabiel, compleet, duidelijk en controleerbaar zijn.
2. Ontwikkelomgeving
    1. Ontwikkelproces
        1. Formaliteit: de mate waarin een consistent proces is gedefinieerd, beschreven en gecommuniceerd voor alle fasen van de realisatie en inproductiename.
        2. Geschiktheid: de geschiktheid van de gekozen processen, methoden en tools.
        3. Procesbeheersing: de mate waarin het gedefinieerde proces wordt gevolgd en de monitoring en verbetering van het proces.
        4. Bekendheid: bekendheid en ervaring van de medewerkers met het voorgeschreven proces.
        5. Productbeheersing: de traceerbaarheid van requirements naar de gerealiseerde oplossing, zodanig dat tests aantonen dat het product voldoet aan die requirements.
    2. Ontwikkelsysteem
        1. Capaciteit: de mate waarin faciliteiten, zoals computers, processorcapaciteit en opslag, beschikbaar zijn voor ontwikkeling, test en ondersteunende activiteiten.
        2. Geschiktheid: de geschiktheid van het ontwikkelsysteem voor ontwikkeling, sturing, documentatie en configuratiemanagement.
        3. Bruikbaarheid: de documentatie, de toegankelijkheid en het gebruiksgemak van het ontwikkelsysteem.
        4. Bekendheid: bekendheid van medewerkers met het ontwikkelsysteem.
        5. Betrouwbaarheid: de betrouwbaarheid en foutloze werking van het ontwikkelsysteem.
        6. Ondersteuning: de training in het gebruik, toegang tot ervaren gebruikers en de oplossing van technische problemen van het ontwikkelsysteem.
        7. Overdraagbaarheid: de overdraagbaarheid van het ontwikkelsysteem aan de opdrachtgever.
    3. Managementproces
        1. Wendbaarheid: de mate waarin een plan is gedefinieerd dat kan omgaan met onvoorziene omstandigheden en lange- termijndoelstellingen, dat is opgesteld met de input van de betrokkenen en dat voorziet in formele wijzigingen als die noodzakelijk zijn.
        2. Projectorganisatie: de organisatie van het project, de rollen en verantwoordelijkheden en de verzekering dat die bekend zijn bij de medewerkers.
        3. Managementervaring: de ervaring van de betrokken managers met het sturen van softwareontwikkelprojecten, het toepassingsdomein, de schaal en complexiteit van het product, het gekozen ontwikkelproces en softwareontwikkeling.
        4. Communicatiekanalen: de interactie tussen managers binnen het project met projectmedewerkers en met externe betrokkenen, zoals de opdrachtgever, ICTU- management en collega-projectleiders.
    4. Managementmethode
        1. Monitoring: het opstellen van en acteren op statusrapportages en het gebruiken en onderhouden van metrieken voor voortgang.
        2. Personeelsbeheer: de selectie en training van medewerkers, het zorgen voor hun betrokkenheid bij planning en communicatie met de opdrachtgever, voor het werken volgens planning en voor de ondersteuning die ze nodig hebben.
        3. Kwaliteitsborging: de procedures voor het volgen van het contractueel afgesproken proces en de afgesproken standaarden en de adequate invulling van kwaliteitsborging binnen het project.
        4. Configuratiebeheer: de adequate bemensing en hulpmiddelen ten behoeve van configuratiebeheer.
    5. Werkomgeving
        1. Attitude: de mate waarin de medewerkers kwalitatief goed werk verrichten en voldoen aan kwaliteitsstandaarden vooproces en product.
        2. Samenwerking: de samenwerking en teamgevoel binnen het team van medewerkers en de mate waarin het management aantoonbaar probeert obstakels voor medewerkers weg te nemen.
        3. Communicatie: de communicatie over de projectdoelstelling, de requirements en het projectbelang.
        4. Moraal: het enthousiasme van het team en de invloed daarvan op prestatie, productiviteit en creativiteit.
3. Projectvoorwaarden: deze groep heeft betrekking op externe factoren voor het project; deze factoren liggen buiten de controle van het project, maar kunnen grote invloed hebben op het projectsucces.
    1. Middelen
        1. Planning: de stabiliteit van de planning met betrekking tot interne en externe gebeurtenissen of afhankelijkheden en de haalbaarheid van de planning.
        2. Bemensing: de stabiliteit van de bemensing in termen van aantallen, kennis- en vaardigheidsniveaus, ervaring in relevante techniek en applicatiedomein en de beschikbaarheid.
        3. Budget: de stabiliteit van het beschikbare budget met betrekking tot interne en externe gebeurtenissen en afhankelijkheden en de haalbaarheid van de gemaakte financiële schattingen.
        4. Faciliteiten: de beschikbaarheid van adequate faciliteiten voor de ontwikkeling, integratie en test van het product.
    2. Contract
        1. Contracttype: de contractuele afspraken met betrekking tot financiering, requirements en de betrokkenheid van de opdrachtgever.
        2. Beperkingen: de contractueel vastgelegde beperkingen met betrekking tot de realisatie van het product, zoals specifieke ontwikkelmethoden, hulpmiddelen of te gebruiken software van derden.
        3. Afhankelijkheden: de contractuele afhankelijkheden van externe aannemers, leveranciers, middelen, software en andere producten en diensten buiten de controle van het project.
    3. Raakvlakken
        1. Opdrachtgever: het kennis- en ervaringsniveau van de opdrachtgever in het betreffende applicatiedomein en de relatie en communicatie met de opdrachtgever.
        2. Co-aannemers: de mate waarin co-aannemers conflicterende politieke agenda’s hebben, waarin koppelvlakken met systemen die bij co-aannemers worden ontwikkeld tot problemen leiden en het gebrek aan samenwerking en afstemming met co-aannemers.
        3. Onderaannemers: de inzet van onderaannemers die afstemming van werkzaamheden en te gebruiken technologie vereist alsmede relatiebeheer.
        4. Hoofdaannemer: de uitvoering van een project als onderaannemer met betrekking tot afstemming van werkzaamheden, rapportages en afhankelijkheden van technische en procesmatige kennis.
        5. Organisatiemanagement: de relatie met het management van de organisatie waarbinnen het project wordt uitgevoerd.
        6. Leveranciers: de afhankelijkheden van externe leveranciers.
        7. Politiek: de politieke invloeden van relaties met de eigen organisatie, de organisatie van de opdrachtgever en andere contractpartijen.

#### Risico's en maatregelen

De onderstaande lijst bevat een aantal algemene, veelvoorkomende risico's bij softwareontwikkel- projecten. Elk beschreven risico is geclassificeerd volgens de risicotaxonomie en is voorzien van de bijbehorende maatregelen uit de kwaliteitsaanpak.

---

**Risico: De software is niet gebruiksgereed, maar de benodigde middelen zijn uitgeput of niet langer beschikbaar (tijd, geld, mensen, kennis, tools).**

Maatregelen:

- M05 Iteratief en incrementeel ontwikkelproces
- M07 Continuous delivery pipeline
- M10 Periodiek projectoverleg
- M14 Projecten splitsen in een voorbereidingsfase
- M15 Open source tools

Classificatie:

- Projectvoorwaarden ➞ Middelen

---

**Risico: De software heeft niet alle gewenste functionaliteit, maar de benodigde middelen zijn uitgeput of niet langer beschikbaar (tijd, geld, mensen, kennis, tools).**

Maatregelen:

- M05 Iteratief en incrementeel ontwikkelproces - De product owner bepaalt de prioriteiten tijdens de ontwikkeling en kan er zo voor zorgen dat de belangrijkste functionaliteit zo vroeg mogelijk wordt gerealiseerd.
- M04 Geautomatiseerde regressietests
- M07 Continuous delivery pipeline
- M10 Periodiek projectoverleg
- M14 Projecten splitsen in een voorbereidingsfase
- M17 Snel beschikbare tools
- M18 Ondersteuning verplichte tools
- M19 Digitale werkomgeving - Testers kunnen efficiënt werken dankzij een afgezonderde testomgeving.

Classificatie:

- Productontwikkeling ➞ Requirements
- Projectvoorwaarden ➞ Middelen

---

**Risico: De software heeft niet de gewenste kwaliteit, maar de benodigde middelen zijn uitgeput of niet langer beschikbaar (tijd, geld, mensen, kennis, tools).**

Maatregelen:

- M02 Continu voldoen aan kwaliteitsnormen
- M06 Frequente meting
- M07 Continuous delivery pipeline
- M08 Technische schuld
- M14 Projecten splitsen in een voorbereidingsfase
- M15 Open source tools
- M17 Snel beschikbare tools
- M18 Ondersteuning verplichte tools
- M21 Kwaliteit van medewerkers
- M28 Self-assessment

Classificatie:

- Productontwikkeling ➞ Requirements
- Projectvoorwaarden ➞ Middelen
- Productontwikkeling ➞ Specialiteiten ➞ Onderhoudbaarheid
- Productontwikkeling ➞ Specialiteiten ➞ Betrouwbaarheid
- Productontwikkeling ➞ Specialiteiten ➞ Beveiliging

---

**Risico: De software voldoet niet aan de eisen en wensen van de opdrachtgever.**

Maatregelen:

- M01 Op te leveren producten
- M03 Traceerbaar voldoen aan eisen
- M05 Iteratief en incrementeel ontwikkelproces
- M06 Frequente meting
- M08 Technische schuld
- M14 Projecten splitsen in een voorbereidingsfase
- M28 Self-assessment

Classificatie:

- Productontwikkeling ➞ Requirements ➞ Volledigheid
- Productontwikkeling ➞ Requirements ➞ Duidelijkheid
- Productontwikkeling ➞ Requirements ➞ Validiteit
- Productontwikkeling ➞ Requirements ➞ Haalbaarheid

---

**Risico: Na oplevering blijkt de software niet te voldoen aan niet eerder expliciet gemaakte eisen en wensen.**

Maatregelen:

- M10 Periodiek projectoverleg
- M13 Dekking ISO-25010
- M28 Self-assessment

Classificatie:

- Productontwikkeling ➞ Requirements ➞ Volledigheid
- Productontwikkeling ➞ Requirements ➞ Validiteit

---

**Risico: De opdrachtgever of het project leggen te veel nadruk op de te realiseren functionaliteit, ten koste van niet-functionele eigenschappen van de software.**

Maatregelen:

- M02 Continu voldoen aan kwaliteitsnormen
- M06 Frequente meting
- M08 Technische schuld
- M13 Dekking ISO-25010
- M14 Projecten splitsen in een voorbereidingsfase - De voorbereidingsfase heeft minder last van de "dagelijkse druk" die later tijdens het traject vaak ontstaat.
- M28 Self-assessment

Classificatie:

- Ontwikkelomgeving ➞ Managementmethode ➞ Kwaliteitsborging
- Ontwikkelomgeving ➞ Werkomgeving ➞ Attitude

---

**Risico: Opgeleverde software blijkt defecten te bevatten.**

Maatregelen:

- M02 Continu voldoen aan kwaliteitsnormen
- M03 Traceerbaar voldoen aan eisen
- M04 Geautomatiseerde regressietests
- M06 Frequente meting
- M07 Continuous delivery pipeline
- M13 Dekking ISO-25010
- M21 Kwaliteit van medewerkers
- M28 Self-assessment

Classificatie:

- Productontwikkeling ➞ Ontwerp ➞ Testbaarheid
- Productontwikkeling ➞ Integratie en Test
- Productontwikkeling ➞ Engineering Specialiteiten ➞ Betrouwbaarheid
- Ontwikkelomgeving ➞ Ontwikkelproces ➞ Productbeheersing

---

**Risico: Er treden fouten op bij installatie van de software in de doelomgeving.**

Maatregelen:

- M01 Op te leveren producten
- M07 Continuous delivery pipeline

Classificatie:

- Productontwikkeling ➞ Ontwerp ➞ Hardware-eisen
- Productontwikkeling ➞ Integratie en Test ➞ Productintegratie
- Productontwikkeling ➞ Integratie en Test ➞ Systeemintegratie

---

**Risico: Bij overdracht naar een derde partij is niet alle relevante en benodigde documentatie beschikbaar.**

Maatregelen:

- M01 Op te leveren producten
- M28 Self-assessment

Classificatie:

- Productontwikkeling ➞ Specialiteiten ➞ Onderhoudbaarheid
