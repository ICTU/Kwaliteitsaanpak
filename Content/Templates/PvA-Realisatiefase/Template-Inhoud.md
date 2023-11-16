# Projectresultaat

De te {ontwikkelen en/of onderhouden} software {beschrijving functionaliteit in hoofdlijnen van de software}.
De software komt tot stand door middel van een agile aanpak met een doorlooptijd van {doorloop} weken, waarbij ICTU de softwareontwikkeling uitvoert; zie hiervoor het hoofdstuk “Werkwijze”.

## Producten en diensten

ICTU levert de volgende producten en diensten op:

1. Werkende software met de functionaliteiten zoals hierboven beschreven.
1. Per release:
    a. een vrijgaveadvies,
    a. de release notes,
    a. een bijgewerkte installatiehandleiding,
    a. een bijgewerkt software-architectuurdocument (SAD),
    a. een bijgewerkt globaal functioneel ontwerp (GFO),
    a. de broncode, inclusief unit testen,
    a. een set van automatische regressietesten (ART),
    a. een beschrijving van de logische testgevallen,
    a. een actuele versie van de kwaliteitsrapportage,
    a. {eventueel bijgewerkte andere documentatie waarvoor ICTU verantwoordelijk en/of penvoerder is, zoals testplannen en kwaliteitsplan}.

{Als operationeel beheer onderdeel is van de dienstverlening: Het DevOps-team voert operationele beheertaken uit, conform overeengekomen kwaliteitsniveaus (quality of services). Hiertoe maakt het project beheerafspraken met de opdrachtgever en de beheerorganisatie en legt deze vast in een dossier afspraken en procedures (DAP). Het vastleggen en rapporteren van informatie over de software tijdens het gebruik en over de uitgevoerde beheeractiviteiten kan hiervan deel uitmaken. De afspraken zijn afgestemd op het beheerplan van de beheerorganisatie, waarin is beschreven hoe de verschillende vormen van beheer van de applicaties en de infrastructuur worden uitgevoerd.}

{Als operationeel en/of applicatiebeheer onderdeel is van de dienstverlening: beschrijf wanneer en hoe de dienstverlening eindigt of verlengd wordt. Bijvoorbeeld, geef aan wat de minimale hoeveelheid aan ontwikkel- en onderhoudwerk is waarbij ICTU nog een geschikte partij is om het operationeel en applicatiebeheer uit te voeren.}

## Scope

Binnen de scope van de opdracht valt de {ontwikkeling en/of het onderhoud} van {de software}, inclusief:

* Ontwikkel, test- en demo-omgevingen,
* Engineering tools voor versiebeheer (GitLab of Azure DevOps), bouwen en testen (Azure DevOps, GitLab en/of Jenkins), kwaliteitscontrole (SonarQube), beveiligingscontrole (SonarQube, OWASP Dependency Checker, OWASP ZAP, OpenVAS), toegankelijkheid (Axe), performancetesten (JMeter) en integrale kwaliteitsrapportage (Quality-time),
* {Als operationeel beheer onderdeel is van de dienstverlening:} Uitrollen in de productieomgeving (Ansible), container registry (Harbor), performance monitoring (APM), security monitoring ({vul aan met concreet product}), controle van kwetsbaarheden in frameworks ({vul aan met concreet product}), controle van images van containers (Trivy), registratie van incidenten bij gebruik en beheer (Topdesk of Jira).
* Backlog management tools (Jira en/of Azure DevOps),
* Beveiligings- en performancetesten in de ICTU-testomgevingen. ICTU voert deze tests uit voordat een nieuwe versie van de software wordt opgeleverd. {Beschrijf hier eventuele andere afspraken met opdrachtgever}.

{Als operationeel beheer geen onderdeel is van de dienstverlening:} Buiten de scope van de opdracht valt:

* Acceptatie- en productieomgevingen en de installatie van de software op acceptatie- en productieomgevingen,
* Beveiligings- en performancetesten in acceptatie- en productieomgevingen, die onder verantwoordelijkheid van de opdrachtgever worden uitgevoerd,
* Keten- en integratietesten met aanpalende systemen in acceptatie- en productieomgevingen,
* Testen met (geanonimiseerde) productiedata,
* Beheeractiviteiten door ICTU.

# Werkwijze

Het succes van het uit te voeren realisatietraject is sterk afhankelijk van de beschikbaarheid en inzet van alle betrokkenen. Deze betrokkenheid dient daarom voor aanvang van het project expliciet te worden geborgd door de betrokken organisaties. Dit zal door de projectleider ICTU en {opdrachtgever} gemonitord worden.

## Scrum-aanpak

Tijdens dit project wordt agile gewerkt volgens de Scrum-aanpak. ICTU propageert de kernwaarden van Scrum. Dit vertaalt zich concreet in:

* Een Scrumteam, bestaande uit een product owner, door {opdrachtgever} aangesteld, die de uiteindelijke inhoudelijke keuzes maakt, en ontwikkelaars (zoals programmeurs, testers en ontwerpers) en een Scrummaster, door ICTU aangesteld.
* Een proces met sprints van {twee of drie} weken waarin de Scrumactiviteiten sprint planning, sprint refinement, daily scrum, sprint demonstratie/review en retrospective plaatsvinden.
* Een definition of ready en een definition of done voor respectievelijk het beginnen en afronden van werk.
* Een product backlog en een sprint backlog.

## DevOps-werkwijze

{Verwijder deze paragraaf indien niet van toepassing}

Tijdens het project wordt DevOps toegepast. Dit vertaalt zich concreet in:

* Het na elke sprint in productie brengen van de nieuwe release.
* Het monitoren van de software tijdens het gebruik en het afhandelen van monitoring-alerts.
* Het oplossen van incidenten.
* Het ondersteunen van functioneel beheerders.
* Rapporteren over de beheerafspraken.
* Het maken van backups en restoren indien nodig.
* {Vul aan en pas aan waar nodig}

## Werving

Direct na de opdrachtverstrekking start ICTU met de bemensing van het project ten behoeve van de realisatiefase. {Beschrijf de eventueel te werven functies}

## Kick-off

Voor een goede start wordt er, bij aanvang van de realisatiefase, een kick-off georganiseerd met alle projectmedewerkers, beoogde stuurgroepleden en de opdrachtgever. In de kick-off komen, naast een kennismaking, eventuele acties aan bod die nog uitgevoerd moeten worden voordat daadwerkelijk met de realisatiefase kan worden begonnen. {Als er al dergelijke acties bekend zijn, voeg ze eventueel hier in.} Ook worden de risico’s geïdentificeerd die van toepassing zijn op de realisatiefase en het verdere verloop van het project. Na opdrachtverstrekking zal de projectleider van ICTU de kick-off voorbereiden en plannen.

## Samenwerking

{Opdrachtgever/partijen} en ICTU werken gezamenlijk aan de op te leveren software in een Scrumteam. Voor een goed resultaat is het van belang dat er minimaal {aantal} {dagen/dagdelen} per week door alle partijen wordt samengewerkt. {partij} stelt hiervoor {fysieke en/of online} ruimte en samenwerkhulpmiddelen beschikbaar; projectmedewerkers zorgen zelf voor een laptop. {Als met hulpmiddelen van ICTU wordt gewerkt: Om deze bij ICTU te gebruiken moeten de laptops voldoen aan de bij ICTU geldende beveiligingsnormen, welke zijn opgenomen in het ICTU-voorschrift Zakelijk gebruik ICT-diensten en voorzieningen.}

Vertegenwoordigers van het project nemen deel aan de volgende overleggen met de opdrachtgever en de beheerorganisatie:
* het architectuuroverleg,
* het informatiebeveiligingsoverleg,
* het beheeroverleg,
* {vul aan en pas aan, indien nodig}

## Projectbesturing

{Beschrijf kort de governancestructuur: stuurgroep, rapportage- en escalatielijnen}

## Oplevering software

De realisatiefase bestaat uit {aantal} sprints. Tijdens elke sprint verwerkt het Scrumteam door de product owner geselecteerde functionaliteit in de software. Geselecteerde functionaliteit die niet afkomt tijdens de sprint kan door de product owner opnieuw geselecteerd worden voor de volgende sprint, of voor een latere sprint. Als er na afronding van de realisatiefase nieuwe wensen of fouten aan het licht komen, dan kan {opdrachtgever} deze later alsnog verwerken of ICTU vragen dit in een eventuele vervolgopdracht uit te voeren.
{Beschrijf hier de afspraken tussen ICTU en opdrachtgever over de opzet van vrijgaveadvies, release notes en goedkeuringsproces.}

## Kwaliteitsbeheersing

De kwaliteitsbeheersing is door ICTU beschreven in het Kwaliteitsplan. Eén van de kwaliteitsmaatregelen is dat ICTU een geautomatiseerd kwaliteitssysteem (Quality-time) inricht dat de kwaliteit van de software en het ontwikkelproces bewaakt. De ICTU-kwaliteitsmanager configureert de metrieken in Quality-time en bewaakt de metingen.

## Inzet {opdrachtgever/partijen}

Betrokkenheid van inhoudsdeskundigen van {opdrachtgever/partijen} is randvoorwaardelijk voor de uitvoering van de opdracht. Van de betrokken medewerkers van deze organisatie{s} wordt het volgende verwacht:

* Actief bijdragen aan workshops en demo's;
* Buiten de workshops uitzoeken van onduidelijkheden en binnen de eigen organisatie(s) op zoek gaan naar antwoorden;
* Opstellen, onderhouden en/of reviewen van documenten namens opdrachtgever.

Onderstaand is de verwachte inzet van {opdrachtgever/partijen} voor de uitvoering van dit plan van aanpak (één persoon kan eventueel meer dan één rol vervullen):

{Selecteer de juiste rollen en vul aan, vul ook de juiste verantwoordelijkheden in, onderstaande is een eerste opzet met zoveel mogelijk rollen}

| Rollen                                        | Verwachte inzet per week | Verantwoordelijkheden                                                                                                        |
|:----------------------------------------------|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| Projectleider (Opdrachtgever)                 | {aantal} dagen           | Bespreken voortgang en eventuele exceptions met de projectleider (opdrachtnemer), deelname aan demo's en eventuele workshops |
| Product owner                                 | {aantal} dagen           | Prioritering user stories, sprintplanning, demo, onderhouden backlog                                                         |
| Business analist                              | {aantal} dagen           | Epics opstellen voor de product backlog, eventueel uitgewerkt in user stories                                                |
| Architect                                     | {aantal} dagen           | Bewaken en onderhouden van de softwarearchitectuur                                                                           |
| Infrastructuurarchitect                       | {aantal} dagen           | Bewaken en onderhouden infrastructuurarchitectuur, opstellen infrastructuurarchitectuur (IA)                                 |
| Testmanager                                   | {aantal} dagen           | Testen van nieuwe softwarereleases voordat deze voor gebruik worden vrijgegeven                                              |
| Expert informatiebeveiliging                  | {aantal} dagen           | Bewaken en onderhouden BIA, opstellen TVA en IB-plan                                                                         |
| Privacy-expert                                | {aantal} dagen           | Bewaken en onderhouden PIA                                                                                                   |
| Diverse inhoudelijk deskundigen               | {aantal} dagen           | Inbrengen domeinexpertise en vertegenwoordiging van (eind)gebruikers en belanghebbenden                                      |
| Technisch beheerder beheerorganisatie         | {aantal} dagen           | Leveren en beheer acceptatie- en productieomgeving                                                                           |
| Functioneel beheerder                         | {aantal} dagen           | Functioneel beheer                                                                                                           |
| Servicedeskmedewerker                         | {aantal} dagen           | Gebruikersondersteuning en incidentbeheer                                                                                    |
| Diverse technisch en inhoudelijk specialisten | ad hoc                   | Inzet op ad-hocbasis ter ondersteuning van de andere rollen                                                                  |

## Afstemming met gerelateerde projecten

{Beschrijf de afstemming met gerelateerde projecten, indien van toepassing}

## Projectafsluiting

Omdat ICTU tijdens het project de software, inclusief documentatie, regelmatig oplevert is er geen speciale eindoplevering nodig. ICTU archiveert de projectartifacten zoals beschreven in de bijlage "Projectafsluiting".

# Planning en doorlooptijd

De start van het project vindt uiterlijk {aantal} weken na ondertekening van het voorstel inclusief projectovereenkomst plaats. In deze periode bemensen zowel ICTU als {opdrachtgever} het project. Daarbij is rekening gehouden met de doorlooptijd van de werving en selectie van de geschikte mensen.

De verwachte doorlooptijd van de uitvoering van dit plan van aanpak is {aantal} weken.

Met een eventuele vakantieperiode is nog geen rekening gehouden, dit zal direct na de “go” op het voorstel inclusief projectovereenkomst afgestemd worden. Mogelijk wordt hierdoor de doorlooptijd langer. Op dat moment wordt ook de verdere invulling van de planning en de sprints afgestemd.

{Hieronder een voorbeeld van een planning}

| Onderdeel/week                       | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:-------------------------------------|:--|:--|:--|:--|:--|:--|:--|:--|:--|:---|:---|:---|
| Bemensen project                     | X | X | X |   |   |   |   |   |   |    |    |    |
| Voorbereiden en plannen kick-off     |   | X | X |   |   |   |   |   |   |    |    |    |
| Kick-off                             |   |   |   | X |   |   |   |   |   |    |    |    |
| Inrichten ontwikkelstraat sprint 0   |   |   |   | X | X |   |   |   |   |    |    |    |
| Realisatie producten sprint 1        |   |   |   |   |   | X | X |   |   |    |    |    |
| Realisatie producten sprint 2        |   |   |   |   |   |   |   | X | X |    |    |    |
| Realisatie producten sprint 3        |   |   |   |   |   |   |   |   |   | X  | X  |    |
| Afronden en afsluiten realisatiefase |   |   |   |   |   |   |   |   |   |    |    | X  |

# Randvoorwaarden

Voor de uitvoering van de realisatiefase gelden de volgende randvoorwaarden:

| Nr           | Randvoorwaarde                                                                                                                                |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| R01          | De vereiste inzet van betrokkenen van {opdrachtgever/partijen} is georganiseerd en gegarandeerd.                                              |
| R02          | De product owner is gemandateerd om zelfstandig besluiten te nemen over de functionaliteit van de software.                                   |
| R03          | Er is een afgestemde en afgesproken werkwijze tussen {opdrachtgever}, {beheerorganisatie} en ICTU. Deze is in lijn met de $KWALITEITSAANPAK$. |
| R04          | De voorfaseproducten {producten} zijn beschikbaar voor aanvang van de realisatiefase.                                                         |
| R05          | Koppelvlakbeschrijvingen van aanpalende systemen zijn beschikbaar.                                                                            |
| {volgnummer} | {randvoorwaarde}                                                                                                                              |

# Projectrisico’s

De onderstaande projectrisico’s, die het succes van de realisatiefase kunnen belemmeren, zijn reeds onderkend; daarbij zijn per risico de maatregelen benoemd.

De risico’s worden door het project bijgehouden in het risicolog. De risico’s en de mitigerende maatregelen worden in de realisatiefase bewaakt en waar nodig geactualiseerd.

{Deze tabel dient op basis van het concrete project en voorstel aangepast te worden.}

| Projectrisico                                                                                                                                                            | Maatregel                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Verwachtingen over dit project tussen verschillende partijen ({partijen}, ICTU) kunnen niet waargemaakt worden, waardoor vertraging ontstaat                             | Wekelijks projectoverleg, samenwerken door middel van werkgroepen en fysiek bij elkaar komen, kick-off met alle betrokkenen waarbij {opdrachtgever} de productvisie uiteenzet. |
| Scope-uitbreiding, gebrek aan focus                                                                                                                                      | Scope bewaken, alleen de scope uitbreiden als dit noodzakelijk is voor {doel}                                                                                                  |
| Onvoldoende bemensing door vakanties                                                                                                                                     | Rekening houden met langere doorlooptijd dan de (te) eenvoudige rekensom suggereert.                                                                                           |
| {Bij DevOps werkwijze} Onduidelijkheid over de verdeling van verantwoordelijkheden tussen DevOps-team en beheerorganisatie (incident management, backup & restore, etc.) | Afspraken over onderlinge samenwerking vastleggen in een dossier afspraken en procedures (DAP).                                                                                |
| {risico}                                                                                                                                                                 | {maatregel}                                                                                                                                                                    |

# Verwachte inzet ICTU

Onderstaand is de verwachte inzet van ICTU voor de uitvoering van dit plan van aanpak:

{Selecteer de rollen die nodig zijn en vul ze aan. Vul de juiste verantwoordelijkheden in. De onderstaande tabel is een eerste opzet met veel voorkomende rollen.}

| Rol                                    | Verwachte inzet | Verantwoordelijkheden                                                                                                                             |
|:---------------------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| Software-architect/senior ontwikkelaar | {x} uur         | Onderhouden SAD, bewaken architectuurkeuzes, ontwerpen, ontwikkelen en testen van de software                                                     |
| Scrummaster                            | {x} uur         | Bewaken Scrumproces, faciliteren Scrumevents                                                                                                      |
| Ontwikkelaar                           | {x} uur         | Ontwerpen, ontwikkelen en testen van de software                                                                                                  |
| DevOps-engineer                        | {x} uur         | Ontwerpen, ontwikkelen en testen van de software, daarnaast uitvoeren beheeractiviteiten, waaronder het oplossen van incidenten                   |
| Tester                                 | {x} uur         | Opstellen logische testgevallen, ontwikkelen en uitvoeren fysieke testgevallen, opstellen testrapportages en vrijgaveadvies                       |
| Functioneel ontwerper                  | {x} uur         | Onderhouden GFO, ondersteunen product owner bij opstellen en uitwerken van de user stories                                                        |
| Database administrator                 | {x} uur         | Onderhouden logisch datamodel en fysiek database ontwerp, ontwikkelen migratiescripts, database tuning                                            |
| UX-designer                            | {x} uur         | Gebruikersonderzoek, onderhouden UX-richtlijnen, maken en onderhouden prototype {of wireframe/mockup/animatie}, toetsen prototypes met gebruikers |
| Informatiebeveiligingsexpert           | {x} uur         | Onderhouden IB-plan, toetsen IB-maatregelen                                                                                                       |
| Kwaliteitsmanager                      | {x} uur         | Inrichten, onderhouden en bewaken kwaliteitsrapportage                                                                                            |
| Software delivery manager              | {x} uur         | Bewaken plan van aanpak realisatiefase, faciliteren en coördineren van het Scrumteam, inhoudelijke rapportage                                     |
| Projectleider                          | {x} uur         | Bewaken overeenkomst realisatiefase, opleveren tussentijdse rapportage, bespreken voortgang en exceptions met opdrachtgever                       |
| Projectsecretaris                      | {x} uur         | Ondersteuning, rapportage, administratie                                                                                                          |
| Diverse technisch specialisten         | {x} uur         | Ondersteunen, adviseren en meeschrijven daar waar nodig op onderdelen waar kennis of tijd van teamleden niet toereikend is                        |
| **Totaal**                             | **{x} uur**     |                                                                                                                                                   |

{In de projectovereenkomst moet in de begroting met onderstaande opmerkingen rekening worden gehouden.}

{Voor de begroting wordt uitgegaan van een gemiddeld bruto tarief. De werkelijke kosten worden bekend als de projectmedewerkers bekend zijn. Wanneer overschrijding van het budget dreigt (bijvoorbeeld vanwege substantieel hogere tarieven), wordt dit tijdig met de opdrachtgever besproken.}

Naast kosten voor de inzet van ICTU-medewerkers worden de volgende kosten voor door ICTU te benutten diensten verwacht:

| Dienst                    | Verwachte kosten | Toelichting |
|:--------------------------|:-----------------|:------------|
| Performancetests          |                  |             |
| Securitytests             |                  |             |
| Onderhoudbaarheidstoetsen |                  |             |
| Usabilitytests            |                  |             |
| Toegankelijkheidstests    |                  |             |