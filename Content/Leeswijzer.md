# Leeswijzer

## Doelgroep

Dit document "$KWALITEITSAANPAK$", verder ook aangeduid met 'de Kwaliteitsaanpak', is bedoeld voor software en gerelateerde producten, voor processen waarmee die producten worden gerealiseerd en voor de overkoepelende organisatie waarin op projectbasis wordt gewerkt (ICTU). Dit betekent dat deze Kwaliteitsaanpak betrekking heeft op de drie aspecten van softwareontwikkeling:

<!-- begin: slide -->
1. Producten - Het eerste deel van de Kwaliteitsaanpak betreft de eigenschappen van de ontwikkelde producten. De broncode valt hieronder, maar ook alle andere producten, zoals eisen, ontwerpen en testscripts.
2. Processen - Het tweede deel gaat over het ontwikkelproces; werkwijze, gebruik van hulpmiddelen en projectaanpak.
3. Organisatie - Het derde deel betreft de organisatie waarbinnen projecten worden uitgevoerd: ICTU; dit gaat over de samenhang tussen projecten en de faciliteiten die projecten ter beschikking moeten hebben.
<!-- end: slide -->

## Maatregelen

Om de risico's die samenhangen met softwareontwikkeling te mitigeren treft ICTU risicobeheersmaatregelen. Deze risicobeheersmaatregelen, verder maatregelen genoemd, vormen de kern van de Kwaliteitsaanpak. De maatregelen zijn onderverdeeld naar de genoemde aspecten *product*, *proces* en *organisatie*.

De onderverdeling is in overeenstemming met de praktijkrichtlijn “Risicobeheersing bij ontwikkeling en onderhoud van maatwerksoftware” [NEN NPR 5326:2019]. Deze praktijkrichtlijn beschrijft veelvoorkomende risico's van maatwerksoftwareontwikkeling en adviseert bijbehorende risicobeheersmaatregelen. Bijlage [Relatie met NEN NPR 5326](#relatie-met-nen-npr-5326) beschrijft hoe de maatregelen in deze Kwaliteitsaanpak samenhangen met de maatregelen die de NPR 5326 adviseert.

De beschrijving van elke maatregel is voorzien van een rationale: waarom behoort de maatregel tot de Kwaliteitsaanpak? Waar mogelijk verwijst de rationale naar maatregelen uit standaarden en richtlijnen die overeenkomen met de door ICTU getroffen maatregelen.

## Rollen

Bij de omschrijving van de maatregelen is gebruik gemaakt van de volgende rollen om aan te geven wie verantwoordelijkheid draagt voor het uitvoeren van de maatregelen:

* Project: de tijdelijke organisatie die de software ontwikkelt, onderhoudt en/of operationeel beheert. Het project bestaat uit medewerkers van ICTU, van de opdrachtgevende organisatie en mogelijk ook van de beheerorganisatie of andere partijen. De softwareontwikkeling binnen het project gebeurt door één of meer Scrumteams, bestaande uit een product owner, ontwikkelaars en een Scrummaster. De product owner is altijd een medewerker van de opdrachtgevende organisatie. Als het project de software ook operationeel beheert past ICTU DevOps toe en maken ook DevOps-engineers deel uit van een Scrumteam. Eén van de ontwikkelaars heeft de rol van softwarearchitect.
* Projectleider: de ICTU-medewerker verantwoordelijk voor uitvoering van het project,
* Software delivery manager: organiseert het ontwikkelen en opleveren van software conform de vastgestelde eisen en de Kwaliteitsaanpak, rapporteert aan de projectleider,
* Kwaliteitsmanager: controleert en borgt de kwaliteit van software conform de vastgestelde eisen en de Kwaliteitsaanpak, rapporteert aan de projectleider. Voor de rol van kwaliteitsmanager is een [inwerkplan template]($BASE_URL$/$VERSIE$/ICTU-Template-Inwerkplan-Kwaliteitsmanager.docx) beschikbaar.

## Ondersteuning

Projecten bij ICTU die software ontwikkelen en/of onderhouden volgens deze Kwaliteitsaanpak, kunnen ondersteuning krijgen van de afdelingen ICTU Software Diensten (ISD) en ICTU Software Expertise (ISE). ISD levert ontwikkel- en testomgevingen, tools en ondersteunende diensten. ISE levert expertise in de vorm van software delivery managers, kwaliteitsmanagers en software-ontwikkelaars. ISE onderhoudt tevens deze Kwaliteitsaanpak. ISD en ISE zijn niet verantwoordelijk voor de projectuitvoering, maar voor het bieden van expertise en diensten om projecten in staat te stellen efficiënt en effectief volgens de Kwaliteitsaanpak te werken.

## Versionering

Elke release van de Kwaliteitsaanpak heeft een versienummer in de vorm majornummer.minornummer.patchnummer.

* Het patchnummer wordt opgehoogd als een nieuwe versie alleen niet-inhoudelijke wijzigingen bevat. Denk aan spellingscorrecties en visuele aanpassingen.
* Het minornummer wordt opgehoogd als er inhoudelijke wijzigingen zijn, maar die wijzigingen geen invloed hebben op de self-assessment. Dat wil zeggen, een project dat een self-assessment doet met versie 2.3 zou dezelfde uitkomst moeten krijgen als het, op min of meer hetzelfde moment, een self-assessment doet met versie 2.4. Voorbeelden van minor wijzigingen zijn aanpassingen aan de rationale van maatregelen en veranderingen in templates.
* Het majornummer wordt opgehoogd als er wijzigingen zijn die van invloed zijn op de self-assessment. Met andere woorden, als self-assessments tegen twee opeenvolgende versie van de Kwaliteitsaanpak niet zonder meer vergelijkbaar zijn. Voorbeelden van major wijzigingen zijn het splitsen en samenvoegen van maatregelen.

## Terminologie

Deze Kwaliteitsaanpak heeft betrekking op de ICTU-projecten waarin software ontwikkeld wordt. De terminologie in dit document is daarop afgestemd en sluit, waar relevant, aan op andere begrippenkaders. De bijlage [Terminologie en afkortingen](#terminologie-en-afkortingen) bevat een lijst met veel gebruikte begrippen en afkortingen.
