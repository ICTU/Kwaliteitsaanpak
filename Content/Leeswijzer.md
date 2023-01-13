# Leeswijzer

## Doelgroep

Dit document "$KWALITEITSAANPAK$", verder ook aangeduid met 'de Kwaliteitsaanpak', is bedoeld voor software en gerelateerde producten, voor processen waarmee die producten worden gerealiseerd en voor de overkoepelende organisatie waarin op projectbasis wordt gewerkt (ICTU). Dit betekent dat deze Kwaliteitsaanpak betrekking heeft op de drie aspecten van softwareontwikkeling:

<!-- begin: slide -->
1. Producten - Het eerste deel van de Kwaliteitsaanpak betreft de eigenschappen van de ontwikkelde producten. De broncode valt hieronder, maar ook alle andere producten, zoals eisen, ontwerpen en testscripts.
2. Processen - Het tweede deel gaat over het ontwikkelproces; werkwijze, gebruik van hulpmiddelen en projectaanpak.
3. Organisatie - Het derde deel betreft de organisatie waarbinnen projecten worden uitgevoerd: ICTU; dit gaat over de samenhang tussen projecten en de faciliteiten die projecten ter beschikking moeten hebben.
<!-- end: slide -->

## Maatregelen

De drie aspecten komen hieronder in meer detail aan bod in de vorm van maatregelen die ICTU heeft getroffen om de risico's die samenhangen met softwareontwikkeling te mitigeren. De praktijkrichtlijn “Risicobeheersing bij ontwikkeling en onderhoud van maatwerksoftware” (NPR 5326:2019) beschrijft veelvoorkomende risico's van maatwerksoftwareontwikkeling en adviseert bijbehorende risicobeheersmaatregelen. Bijlage [Relatie met NEN NPR 5326](#relatie-met-nen-npr-5326) beschrijft hoe de maatregelen in deze Kwaliteitsaanpak samenhangen met de maatregelen die de NPR 5326 adviseert.

De beschrijving van elke maatregel is voorzien van een rationale: waarom behoort de maatregel tot de Kwaliteitsaanpak? Waar mogelijk verwijst de rationale naar maatregelen uit standaarden en richtlijnen die overeenkomen met de door ICTU getroffen maatregelen.

## Rollen

Bij de omschrijving van de maatregelen is gebruik gemaakt van de volgende rollen om aan te geven wie verantwoordelijkheid draagt voor het uitvoeren van de maatregelen:

* Project: de tijdelijke organisatie die de software ontwikkelt, onderhoudt en/of operationeel beheert. Het project bestaat uit medewerkers van ICTU, van de opdrachtgever en mogelijk ook van de beheerorganisatie of andere partijen. De softwareontwikkeling binnen het project gebeurt door één of meer Scrumteams, bestaande uit een product owner, ontwikkelaars en een Scrummaster. De product owner is altijd een medewerker van de opdrachtgevende organisatie. Als het project de software ook operationeel beheert past ICTU DevOps toe en maken ook DevOps-engineers deel uit van een Scrumteam.
* Projectleider: de ICTU-medewerker verantwoordelijk voor uitvoering van het project,
* Software delivery manager: organiseert het ontwikkelen en opleveren van software conform de vastgestelde eisen en de Kwaliteitsaanpak, rapporteert aan de projectleider,
* Kwaliteitsmanager: controleert en borgt de kwaliteit van software conform de vastgestelde eisen en de Kwaliteitsaanpak, rapporteert aan de projectleider.

## Ondersteuning

Projecten bij ICTU die software ontwikkelen en/of onderhouden volgens deze Kwaliteitsaanpak, kunnen ondersteuning krijgen van de afdelingen ICTU Software Diensten (ISD) en ICTU Software Expertise (ISE). ISD levert ontwikkel- en testomgevingen, tools en ondersteunende diensten. ISE levert expertise in de vorm van software delivery managers, kwaliteitsmanagers en software-ontwikkelaars. ISE onderhoudt tevens deze Kwaliteitsaanpak. ISD en ISE zijn niet verantwoordelijk voor de projectuitvoering, maar voor het bieden van expertise en diensten om projecten in staat te stellen efficiënt en effectief volgens de Kwaliteitsaanpak te werken.

## Evolutie van de aanpak zelf

De Kwaliteitsaanpak is een evoluerende aanpak, gebaseerd op de ervaringen die ICTU continu opdoet in de projecten waarin ICTU samen met opdrachtgevers maatwerksoftware ontwikkelt en onderhoudt. ICTU hanteert daarbij de vuistregel dat als tenminste 80% van de projecten minstens 80% van de tijd een bepaalde werkwijze hanteren, voor die werkwijze een maatregel in de Kwaliteitsaanpak wordt opgenomen. Maar het kan ook voorkomen dat maatregelen om andere redenen landen in de Kwaliteitsaanpak; denk aan het toegankelijk maken van software dat wettelijk verplicht is.

## Voorschrijvend of beschrijvend?

De maatregelen vormen het startpunt voor de aanpak van ieder ICTU-softwareproject, maar bieden daarbij ruimte voor variatie of alternatieve invulling. Bijvoorbeeld stelt de Kwaliteitsaanpak: software wordt minimaal bij iedere grote release of tenminste twee keer per jaar onderworpen aan een beveiligingstest door beveiligingsexperts die ICTU daarvoor inhuurt (zie [$M26$](#m26)). Een alternatief is dat de opdrachtgever de verantwoordelijkheid neemt voor het laten uitvoeren van beveiligingstests. Hierover maakt de projectleider nadere afspraken met de opdrachtgever. De Kwaliteitsaanpak is dus zowel voorschrijvend als beschrijvend. Voorschrijvend omdat ICTU verwacht dat projecten die maatwerksoftware ontwikkelen en onderhouden de aanpak toepassen, en alleen aanpassen als daar een goede reden voor is, en mits dat wettelijk is toegestaan. Tegelijkertijd is de aanpak beschrijvend omdat de meeste maatregelen voor de meeste projecten de meeste tijd van toepassing zijn en worden toegepast. Zoals blijkt uit de self-assessment die ICTU regelmatig uitvoert op de toepassing van de Kwaliteitsaanpak.

## Versionering

Elke release van de Kwaliteitsaanpak heeft een versienummer in de vorm majornummer.minornummer.patchnummer.

- Het patchnummer wordt opgehoogd als een nieuwe versie alleen niet-inhoudelijke wijzigingen bevat. Denk aan spellingscorrecties en visuele aanpassingen.
- Het minornummer wordt opgehoogd als er inhoudelijke wijzigingen zijn, maar die wijzigingen geen invloed hebben op de self-assessment. Dat wil zeggen, een project dat een self-assessment doet met versie 2.3 zou dezelfde uitkomst moeten krijgen als het, op min of meer hetzelfde moment, een self-assessment doet met versie 2.4. Voorbeelden van minor wijzigingen zijn aanpassingen aan de rationale van maatregelen en veranderingen in templates.
- Het majornummer wordt opgehoogd als er wijzigingen zijn die van invloed zijn op de self-assessment. Met andere woorden, als self-assessments tegen twee opeenvolgende versie van de Kwaliteitsaanpak niet zonder meer vergelijkbaar zijn. Voorbeelden van major wijzigingen zijn het splitsen en samenvoegen van maatregelen.
