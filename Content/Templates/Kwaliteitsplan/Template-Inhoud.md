# Kwaliteitsmaatregelen tijdens het project

De onderstaande kwaliteitsmaatregelen zijn van toepassing gedurende het gehele project, waaronder de voorfase en de realisatiefase. De navolgende hoofdstukken beschrijven aanvullende kwaliteitsmaatregelen voor respectievelijk de voorfase, de realisatiefase en de projectafsluiting. De M-nummers verwijzen naar maatregelen uit de $KWALITEITSAANPAK$, zie [https://www.ictu.nl/kwaliteitsaanpak](https://www.ictu.nl/kwaliteitsaanpak).

## Projectmanagement

### Wekelijks projectoverleg

Het project houdt een wekelijks intern projectoverleg (IPO) waarin planning, voortgang, kwaliteitsrapportage, acties, risico's en overige relevante zaken worden besproken ($M10$). Het doel is om informatie uit te wisselen binnen het project, belemmeringen voor de voortgang die het Scrumteam niet zelf kan oplossen te melden en eventueel te besluiten over escalaties buiten het project.

De IPO-agenda bevat minimaal: mededelingen, kwaliteit, voortgang, risico's, acties en rondvraag. Aanwezig zijn in ieder geval de projectleider, de software delivery manager, de kwaliteitsmanager, de Scrummaster en een vertegenwoordiger uit elk Scrumteam.

De kwaliteitsmanager controleert of deze overleggen plaatsvinden.

### Actie- en besluitenlijst

Het project houdt een actie- en besluitenlijst bij. De actie- en besluitenlijst wordt digitaal bijgehouden door de software delivery manager en wordt tijdens het wekelijks projectoverleg besproken. Quality-time, het kwaliteitssysteem van ICTU, bewaakt de actualiteit van de actie- en besluitenlijst.

### Risicomanagement

Het project houdt een risicolog bij. De risicolog wordt digitaal bijgehouden door de software delivery manager en periodiek besproken tijdens het projectoverleg. Iedere projectmedewerker kan risico's melden bij de software delivery manager. De omvang van risico's wordt ingeschat en indien nodig voorzien van een of meer maatregelen. Quality-time bewaakt de actualiteit van het risicolog.

### Ontwikkelproces

Voor de realisatiefase wordt de agile ontwikkelmethode Scrum gebruikt ($M05$). Als operationeel beheer onderdeel is van de dienstverlening wordt gebruik gemaakt van de DevOps-principes. Afwijkingen hierop worden alleen toegestaan met goedkeuring van de software delivery manager en kwaliteitsmanager.

### Bewaken van kwaliteitsnormen

De kwaliteitsmanager rapporteert {frequentie/als onderdeel van de managementrapportage} over het al dan niet behalen van de kwaliteitsnormen. De rapportage bestaat uit {geschreven rapportage en/of Quality-time export}. De kwaliteitsmanager verstuurt de rapportage per mail aan {ontvangers} en archiveert de verstuurde rapportages {op Sharepoint}.

De volgende rapportage/escalatielijnen worden gehanteerd indien kwaliteitsnormen niet tijdig worden behaald:

1. De kwaliteitsmanager bespreekt de situatie met de software delivery manager;
2. Indien 1. niet tot resultaat leidt, escaleert de kwaliteitsmanager de situatie naar de ICTU-projectleider;
3. Indien 2. niet tot resultaat leidt, escaleert de kwaliteitsmanager de situatie naar het hoofd van de afdeling ICTU Software Expertise (ISE).

Als ontdekte kwaliteitsproblemen daartoe aanleiding geven, worden dit kwaliteitsplan en/of Quality-time uitgebreid met nieuwe maatregelen en metrieken om de problemen in de toekomst te signaleren en te voorkomen. Dat gebeurt ook proactief, bijvoorbeeld naar aanleiding van ervaringen in andere projecten of als er nieuwe tools beschikbaar komen. De projectleiders van {opdrachtgevende organisatie}, de beheerorganisatie en ICTU zorgen er gezamenlijk voor dat de gewenste uitbreidingen worden gerealiseerd.

## Projectdocumenten

### Versiebeheer documenten

Alle documenten die een deliverable van het project zijn, zoals architectuurdocumenten, functioneel ontwerp en installatiehandleidingen, worden in de digitale samenwerkruimte van het project geplaatst. De opgeleverde documenten worden in pdf-formaat opgeslagen en bevatten een versienummer in de naam. De versies van de bronbestanden van deliverables worden opgeslagen in een online werkomgeving en moeten beschikbaar zijn om later aangepast te kunnen worden. Dit project gebruikt {Git, Sharepoint, Samenwerkingsruimte}.

Bij elk formele release moeten de documenten geactualiseerd zijn en formeel opgeleverd worden.

### Documentreview

Alle deliverables worden gereviewd. De auteur van een deliverable zorgt, in overleg met de software delivery manager, dat de juiste reviewers benoemd zijn; hiertoe behoort in ieder geval de kwaliteitsmanager. De auteur van het document zorgt voor een correct versiebeheer van het document.

Reviewers worden uitgenodigd door de auteur van het document en ontvangen de juiste versie van de auteur. De werkwijze wordt in overleg door de software delivery manager en kwaliteitsmanager bepaald.

De opstellers verwerken het commentaar. Vervolgens sturen de opstellers een toelichting op de wijze waarop het commentaar al dan niet is verwerkt naar de reviewers.

# Kwaliteitsmaatregelen voorfase

Het doel van de voorfase is tweeledig: het voorbereiden van de realisatiefase, zodat ICTU verantwoord een projectovereenkomst kan opstellen voor de realisatiefase, en het identificeren van risico’s die van toepassing zijn op de realisatiefase en het verdere verloop van het project.

{opdrachtgevende organisatie} zorgt dat het project bij de start van de voorfase inzicht heeft in de informatie die typisch wordt vastgelegd in een projectstartarchitectuur, business impact analyse en privacy impact assessment. Waar nodig werkt {opdrachtgevende organisatie} de informatie bij tijdens de voorfase en realisatiefase.

Dit kwaliteitsplan wordt opgesteld tijdens de voorfase, maar is tevens al deels van toepassing, in ieder geval aan het eind van de voorfase. Voor de voorfase gelden de onderstaande kwaliteitsmaatregelen.

## Belanghebbenden

De kwaliteit van de deliverables wordt mede bepaald door de verwachtingen van de belanghebbenden. Het is van belang dat alle belanghebbenden zijn geïdentificeerd en hun verwachtingen zijn vastgelegd, geanalyseerd en vertaald naar de eisen voor het te implementeren systeem. De belanghebbenden worden geïdentificeerd in het projectvoorstel voor de voorfase. De eisen aan het te ontwikkelen systeem worden vastgelegd in Backlog en NFE-document.

De tijdens de voorfase geïdentificeerde eisen vormen het startpunt van {opdrachtgevende organisatie} en kunnen gedurende de vervolgfases in overeenstemming met de opdrachtnemer aangepast worden. De product owner vertegenwoordigt gedurende de vervolgfasen de geïdentificeerde belanghebbenden.

## Verwerking eisen

### Functionele eisen

Het programma van eisen en de projectstartarchitectuur, beide opgesteld door {opdrachtgevende organisatie}, zijn de basis voor de op te leveren ICTU-documenten, zoals architectuur en ontwerpdocumenten.

### Niet-Functionele eisen

Niet-functionele eisen aan het te ontwikkelen systeem worden vastgelegd op basis van de projectstartarchitectuur en aan de hand van de NEN-ISO/IEC 25010-standaard in een NFE-document. De ISO-25010-kwaliteitsattributen worden door de belanghebbenden geprioriteerd in een of meer workshops (PRA – zie ook testen). Voor de kwaliteitsattributen worden SMART-eisen geformuleerd.

Niet-functionele eisen voor onderstaande kwaliteitsattributen worden als volgt verwerkt:

* De informatiebeveiligingseisen worden in een afzonderlijk informatiebeveiligingsplan vastgelegd. De software zal zodanig worden voortgebracht en {in geval van operationeel en/of applicatiebeheer:} beheerd dat deze de BIO-compliance van {opdrachtgevende organisatie} niet zal hinderen.
* Gebruikskwaliteit (usability) is ingebed in de standaard werkwijze van ICTU voor de realisatie van maatwerksoftware. Dit aspect wordt geborgd door opname in het plan van aanpak, het ontwerp en de testplannen.
* Toegankelijkheid is een wettelijke verplichting voor webgebaseerde en mobiele applicaties, zie de EN 301 549 en de WCAG 2.2, niveau A en AA. Toegankelijkheid wordt geborgd via toegankelijkheidstesten, zie de kwaliteitsmaatregelen in paragraaf [Toegankelijkheidstesten](#toegankelijkheidstesten).
* Performance- en securityeisen worden via performance- en securitytests geborgd, zie de kwaliteitsmaatregelen in paragraaf [Testen](#testen). Voor de borging van andere niet-functionele eisen moeten projectspecifieke maatregelen getroffen worden. Deze worden in dit kwaliteitsplan opgenomen.
* {Als operationeel beheer onderdeel is van de dienstverlening:} Eisen aan het operationeel beheer worden vastgelegd als beheerafspraken in het plan van aanpak voor de realisatiefase en geborgd door te rapporteren over de software tijdens het gebruik en over de uitgevoerde beheeractiviteiten.

### Compleetheid deliverables voorfase

In aanvulling op de maatregelen met betrekking tot reviews, zie paragraaf [Documentreview](#documentreview), reviewt de kwaliteitsmanager de deliverables van de voorfase op compleetheid. Hiervoor vormt de $KWALITEITSAANPAK$ het referentiekader.

### Tracering eisen

{Als de eisen traceerbaar moeten zijn vanuit de Backlog/NFE-document/Informatiebeveiligingsplan via GFO en SAD naar broncode, beschrijf dan hier de wijze waarop de eisen uniek identificeerbaar zijn gemaakt, hoe de relaties tussen eisen en ontwerp(beslissingen) worden bijgehouden en hoe de relaties tussen ontwerp(beslissingen) en code worden bijgehouden. Beschrijf hier ook wie deze relaties op welke momenten verifieert en hoe de verificatie wordt gedocumenteerd.}

# Kwaliteitsmaatregelen realisatiefase

De onderstaande kwaliteitsmaatregelen zijn van toepassing gedurende de realisatiefase.

## Entry- en exitcriteria

ICTU volgt een agile aanpak bij het realiseren van software, waarbij gewerkt wordt in korte iteraties (sprints) waarin user stories worden omgezet in werkende software. De resultaten van één of meer sprints worden gebundeld in (major) releases. Hierbij worden entry- en exitcriteria gebruikt om te bepalen of werk kan worden opgepakt of gereed is: Definition of Ready (entry criteria) en Definition of Done (exit criteria) voor user stories en het vrijgaveadvies voor releases (exit criteria).

### Definition of Ready

Het project definieert en hanteert een Definition of Ready (DoR) voor user stories. Een user story kan pas in een sprint worden opgepakt als deze aan de DoR voldoet. De kwaliteitsmanager controleert of er een DoR is gedefinieerd en controleert periodiek of deze wordt gehanteerd.

De Definition Of Ready van het project bevat de volgende criteria ({vul aan en pas aan}):

1. De beschrijving voldoet aan het user story formaat “als <rol> wil ik <actie> zodat <reden>”;
2. De annotaties en screenshots/prototype zijn gereed;
3. Afhankelijkheden met derden zijn in kaart (bijvoorbeeld: een koppelvlakbeschrijving is beschikbaar);
4. De story is ingeschat door het Scrumteam;
5. De story is goedgekeurd door de product owner;
6. De story is goedgekeurd door de reviewer binnen het Scrumteam;
7. Het verwachte aantal logische testgevallen is ingevuld;
8. Er is ingeschat of de user story mogelijk impact heeft op performance, beveiliging, infrastructuur of andere niet-functionele aspecten. {Zie de bijlage "Gebruik van Jira" voor meer informatie.}

### Definition of Done

Het project definieert en hanteert een Definition of Done (DoD) voor user stories. De kwaliteitsmanager controleert of er een DoD is gedefinieerd en controleert periodiek of deze wordt gehanteerd.

De Definition Of Done van het project bevat de volgende criteria ({vul aan en pas aan}):

1. De broncode voldoet aan de codeerstandaard en is gereviewed,
1. Nieuwe testgevallen zijn gereviewd en geaccordeerd door reviewer,
1. Functionele testen zijn succesvol afgerond,
1. De dekkingsgraad van de functionele testen is minstens 80% (maar meer indien mogelijk),
1. Integratietesten zijn succesvol afgerond,
1. Performancetesten zijn succesvol afgerond,
1. Toegankelijkheidstesten zijn succesvol afgerond,
1. Relevante documentatie, zoals GFO en deploymentdocument, is bijgewerkt,
1. De demo van de user story is voorbereid.

### Vrijgaveadvies

Voor elke major release stelt de opdrachtgevende organisatie (bijvoorbeeld de testmanager) een vrijgaveadvies op. Het project levert daartoe informatie aan. De kwaliteitsmanager reviewt de aangeleverde informatie.

Aan te leveren informatie ten behoeve van het vrijgaveadvies ({vul aan en pas aan}):

1. Welke functionele en niet-functionele eisen in deze release gerealiseerd zijn en hoe dit getoetst en/of getest is,
2. Openstaande bugs,
3. Afwijkingen kwaliteitsrapportage ("rode metrieken") en hieruit voortvloeiende risico's,
4. Overige risico's,
5. Het advies van ICTU wat betreft ingebruikname van de release.

### Release notes

Voor elke release stelt het project release notes op, een overzicht van de wijzigingen in de release. De release notes worden opgesteld door {rol} namens ICTU.

## ICTU-kwaliteitssysteem

Gedurende de realisatiefase gebruikt ICTU Quality-time, het kwaliteitssysteem van ICTU, om automatisch metrieken te meten. Deze metrieken hebben zowel betrekking op het proces als op het product (broncode). De metrieken worden meerdere keer per uur bijgewerkt, zodat er altijd een goed inzicht is in de softwarekwaliteit. Zie het [overzicht van mogelijke metrieken](https://quality-time.readthedocs.io/en/latest/reference.html#metrics) en de daarbij horende standaard normen; de kwaliteitsmanager zal in samenwerking met het realisatieteam de te gebruiken metrieken en normen instellen.

{Als operationeel beheer onderdeel is van de dienstverlening:} Het project gebruikt {monitoringapplicatie} om het gedrag en de kwaliteit van de applicatie in de operationale situatie te bewaken.

De actuele kwaliteitsrapportage wordt dagelijks besproken tijdens de daily scrum en wekelijks in het intern projectoverleg (IPO). De kwaliteitsmanager onderhoudt en bewaakt de kwaliteitsrapportage.

Ondanks dat het de voorkeur heeft zoveel mogelijk kwaliteitsaspecten van de software en het softwareproces geautomatiseerd te meten is dit niet altijd mogelijk of kosteneffectief. Daarom voert het project self-assessments uit en doet de kwaliteitsmanager periodiek ook handmatige controles. Zie bijlage E.

## Kwaliteit van de broncode

### Codeerstandaard

Het project hanteert de volgende codeerstandaarden:

| Programmeertaal     | Codeerstandaard     | Controle         |
|:--------------------|:--------------------|:-----------------|
| {programmeertaal A} | {codeerstandaard A} | {broncodereview} |
| {programmeertaal B} | {codeerstandaard B} | {tool B}         |

De keuze van programmeertalen en andere technologie staat beschreven in het SAD.

### Linters, formatters, checkers

Ontwikkelaars in het project gebruiken de volgende tools in hun IDE (Integrated Development Environment) {vul aan/pas aan}:

| Programmeertaal   | Tool               | Soort        |
|:------------------|:-------------------|:-------------|
| DotNet            | ReSharper          | Linter       |
| DotNet            | StyleCop           | Linter       |
| DotNet            | Dotnet-format      | Formatter    |
| Java              | Checkstyle         | Linter       |
| Java              | ErrorProne         | Bug checker  |
| Java              | Google Java Format | Formatter    |
| JavaScript        | ESLint             | Linter       |
| JavaScript        | JSLint             | Linter       |
| JavaScript        | Prettier           | Formatter    |
| Python            | Pylint             | Linter       |
| Python            | Ruff               | Linter       |
| Python            | Black              | Formatter    |
| Python            | Mypy               | Type checker |
| Diverse           | SonarLint          | Linter       |
| {Programmeertaal} | {Tool}             | {Soort}      |

De configuratie van de tools wordt {wel/niet} gedeeld in de broncode-repository.

### Broncodereviews

Het project hanteert de volgende werkwijze voor broncodereviews:

* Elke merge request wordt door minimaal {X} ontwikkelaar(s) gereviewed.
* Er zijn {Y} goedkeuringen nodig voordat een merge request mag worden gemerged.
* Na goedkeuring wordt de merge request gemerged door de {ontwikkelaar/reviewer}.

Quality-time bewaakt of de reviews hebben plaatsgevonden.

### Complexiteit van broncode limiteren

Om de onderhoudbaarheid van de software te bevorderen dienen methoden en klassen niet te complex te zijn. Het uitgangspunt is dat de cyclomatische complexiteit van individuele methoden, zoals berekend door SonarQube, niet groter is dan 10. De norm is dat 0% van de methoden een te hoge cyclomatische complexiteit hebben. Quality-time bewaakt de complexiteit van de broncode.

### Duplicatie van broncode beperken

Om de onderhoudbaarheid van de software te bevorderen dient er zo min mogelijk duplicatie van broncode aanwezig te zijn. Het uitgangspunt is dat SonarQube met de standaard instellingen 0% duplicatie rapporteert. Quality-time bewaakt de duplicatie in broncode.

### Omvang van het systeem beperken

Om de onderhoudbaarheid van de software te bevorderen dient de totale omvang beperkt te blijven, gemeten in mensjaren herbouwtijd. De SIG/TüVIT-standaard geeft een maximale herbouwtijd en vertaalt deze in een maximum omvang van de software gemeten in regels code. Die maximale omvang verschilt per programmeertaal. Quality-time bewaakt de totale omvang van het systeem.

Voor dit project gelden de volgende normen:

| Programmeertaal     | Maximale omvang in regels code |
|:--------------------|:-------------------------------|
| {programmeertaal A} | {maximale omvang}              |
| {programmeertaal B} | {maximale omvang}              |

### Omvang van methoden beperken

Om de onderhoudbaarheid van de software te bevorderen dienen methoden niet te groot te zijn. ICTU stelt de norm op maximaal 20 non-comment source statements (NCSS) per methode, zoals gemeten door SonarQube. In het systeem als geheel mag maximaal 0% (afgerond) van de methoden deze norm overschrijden. Quality-time bewaakt de omvang van methoden.

### Omvang van unit interfaces beperken

Om de onderhoudbaarheid van de software te bevorderen, dienen methoden niet te veel parameters te hebben. ICTU stelt de norm op maximaal vijf parameters per methode, zoals gemeten door SonarQube. In het systeem als geheel mag maximaal 0% (afgerond) van de methoden deze norm overschrijden. Quality-time bewaakt de omvang van unit interfaces.

## Versiebeheer broncode

Broncode, zowel van productiesoftware als van geautomatiseerde tests, wordt in een versiebeheersysteem geplaatst. Alleen projectmedewerkers hebben toegang tot de broncode. Quality-time bewaakt of branches worden gemerged met de default branch (meestal *main* of *develop* genoemd).

## Testen

Gedurende de realisatiefase worden de use cases in samenwerking met de product owner vertaald naar user stories. Per user story worden één of meer logische testgevallen opgesteld; per logisch testgeval worden één of meer fysieke testgevallen opgesteld. De user stories, logische testgevallen en fysieke testgevallen zijn expliciet aan elkaar gekoppeld. User stories en logische testgevallen worden vastgelegd in Jira; zie de bijlagen voor de te gebruiken typen en relaties. Afwijkingen op deze standaard aanpak zijn alleen toegestaan met goedkeuring van de kwaliteitsmanager.

Het mastertestplan (MTP) beschrijft welke testsoorten met welke intensiteit voor de realisatie- en beheerfase worden uitgevoerd. Het MTP wordt gebaseerd op in ieder geval PSA, NFE, SAD en GFO. Daarnaast is een product risicoanalyse (PRA) is uitgevoerd als basis voor de vaststelling van de diepgang waarmee de gedefinieerde testsoorten uitgevoerd moeten worden.

## Unit tests

Om de correcte werking van de software te borgen, schrijven ontwikkelaars unit tests. De unit tests draaien als onderdeel van de geautomatiseerde pijplijn en de broncodedekking van de unit tests wordt gemeten. Quality-time rapporteert over het aantal unit tests, het al dan niet slagen van de unit tests en broncodedekking van de unit tests.

De default normen voor broncodedekking met unit tests zijn 90% line coverage en 80% branch coverage. De norm geldt niet voor gegenereerde code, code van derde-partijen die ICTU zelf niet onderhoudt en triviale code zoals getters/setters/framework boilerplate-code.

## Systeemtesten

Om de correcte werking van de software te borgen maken de ontwikkelaars systeemtesten. Deze bestaan uit een combinatie van handmatige eenmalige testen, handmatige regressietesten en automatische regressietesten. De automatische regressietesten draaien als onderdeel van de geautomatiseerde pijplijn en de broncode dekking van de automatische regressietesten wordt gemeten. Quality-time rapporteert over het aantal handmatige regressietesten, de hoeveelheid tijd die het kost de handmatige regressietesten uit te voeren en de laatste datum dat ze zijn uitgevoerd. Quality-time rapporteert ook over het aantal automatische regressietesten, of ze al dan niet falen en de broncodedekking van de geautomatiseerde regressietesten.

De default normen voor broncodedekking met geautomatiseerde regressietesten zijn 80% line coverage en 70% branch coverage. De norm geldt niet voor gegenereerde code, code van derde-partijen die ICTU zelf niet onderhoudt en triviale code zoals getters/setters/framework boiler plate code.

## Unit tests en systeemtesten gecombineerd

Quality-time kan ook de geaggregeerde broncodedekking van unit tests en automatische regressietesten samen rapporteren. In dat geval zijn de default normen voor geaggregeerde broncodedekking 90% line coverage en 85% branch coverage.

Het is, ook als de geaggregeerde dekking gemeten wordt, nog steeds handig te weten welke code de automatische regressietesten (ART) en unit tests elk voor zich raken. Het is aan het project te beslissen welke norm nuttig is ART-dekking en unittest-dekking en of daar überhaupt normen voor nodig zijn.

Het uitgangspunt is dat zoveel mogelijk van de software die ICTU maakt, geautomatiseerd getest wordt en dat daarbij bewuste keuzes zijn gemaakt over de code die niet geautomatiseerd wordt getest. Om die keuzes goed te kunnen maken is het belangrijk dat het deel van de code, dat niet wordt geraakt door geautomatiseerde testen, relatief klein is; daardoor blijft de benodigde hoeveelheid handmatig testwerk beperkt en de risico's van handmatig testen beperkt.

## Performancetesten

Om de performance van de software te borgen voert het project performancetesten uit. Het MTP beschrijft de gekozen aanpak; de performance-eisen zijn vastgelegd in het NFE-document.

ICTU voert drie soorten performancetesten uit, die inzicht geven in de volgende facetten:
1. snelheid van handelingen en voldoen aan eisen (loadtest)
2. stabiliteit op langere termijn (duurtest)
3. schaalbaarheid en maximale belastbaarheid (stresstest).

Deze performancetesten worden uitgevoerd in de {performancetestomgeving}. De loadtest draait dagelijks. De duurtest en stresstest draaien wekelijks.

Quality-time rapporteert over de geautomatiseerde performancetesten. Als de verantwoordelijke tester performancerisico's ontdekt die ook aanwezig zijn in een versie van de software die reeds is opgeleverd, rapporteert de tester deze risico's aan het Scrumteam. Issues die voortkomen uit performancetesten worden opgenomen in Jira met het label "performance_bevinding".

{Als operationeel beheer geen onderdeel is van de dienstverlening:} De testen van ICTU kunnen geen uitsluitsel geven over de uiteindelijke performance in de productie-omgeving: ze geven niet meer dan een relatief resultaat ten opzichte van eerdere testen in dezelfde testomgeving. Toch hanteert ICTU ze als een standaard kwaliteitsmaatregel, vóór de oplevering van een nieuwe versie van de software. Want ze geven het inzicht of de performance voor wat betreft de software geen achteruitgang betekent ten opzichte van de bestaande situatie. De uiteindelijke performance in de productieomgeving dient {opdrachtgevende organisatie} zelf te (laten) testen.

## Security-testen

De eisen aan de beveiliging worden in de documenten projectstartarchitectuur en niet-functionele eisen gedefinieerd. De in te richten testen dienen aan te tonen dat aan de gestelde beveiligingseisen wordt voldaan.

De geautomatiseerde broncodereviews en rapportages uit Quality-time bevatten diverse metrieken voor beveiligingsaspecten, zoals de OWASP Top-10-criteria. De applicatie wordt gescand met behulp van SonarQube, OWASP Dependency-Check en/of Dependency-Track en ZAP by Checkmarx.

Om de beveiliging van de software te testen kan deze met enige regelmaat getest worden door een externe partij. Het MTP beschrijft de gekozen aanpak.

Elke beveiligingstest resulteert in een beveiligingstestrapportage met daarin de aangetroffen beveiligingsissues. Issues die voortkomen uit deze testen worden opgenomen in Jira met het label "security_bevinding". Voor beveiligingsissues gelden de volgende oplostermijnen:

| Kwalificatie beveiligingsissue                    | Oplostermijn bij software die wel in productie is   | Oplostermijn bij software die niet in productie is |
|:--------------------------------------------------|:----------------------------------------------------|:---------------------------------------------------|
| Hoog (hoog risico en/of hoge impact)              | Zo snel mogelijk, resulteert in een bug fix release | Voor de eerste productierelease                    |
| Midden (gemiddeld risico en/of gemiddelde impact) | Voor de eerstvolgende major productierelease        | Voor de eerste productierelease                    |
| Laag (laag risico en lage impact)                 | In overleg met de product owner                     | In overleg met de product owner                    |

Quality-time rapporteert of gevonden beveiligingsissues niet te lang open staan.

{Als operationeel beheer geen onderdeel is van de dienstverlening:} Merk op: de beveiliging van de software in de acceptatie- en productieomgeving kan niet door ICTU getest worden. Deze test moet de opdrachtgevende organisatie of de beheerorganisatie uitvoeren.

## Toegankelijkheidstesten

Om de toegankelijkheid van webapplicaties te testen gebruikt ICTU Axe; Axe is ingericht in de pijplijn. Quality-time rapporteert over de toegankelijkheidsrapportage van Axe. Daarnaast worden handmatige toegankelijkheidstesten uitgevoerd, door deskundige leden van het Scrumteam {of door externe deskundigen}. Het MTP beschrijft de gekozen aanpak voor het testen van WCAG-2.2-richtlijnen die niet geautomatiseerd kunnen worden getest.

## Usability-testen

{Verwijder deze paragraaf indien usability-testen niet van toepassing zijn}

Om de usability van de software te testen worden usability-testen uitgevoerd, door deskundige leden van het Scrumteam {of door externe deskundigen}. Het MTP beschrijft de gekozen aanpak.

Issues die voortkomen uit usability-testen worden opgenomen in Jira met het label "usability_bevinding".

## Technische schuld

Technische schuld zijn eigenschappen van de software die de lange-termijninzetbaarheid en onderhoudbaarheid van de software bedreigen; denk hierbij aan hoge complexiteit, lage testdekking, ontbrekende testsoorten en ontbrekende documentatie.

Als het Scrumteam of de kwaliteitsmanager constateert dat er technische schuld is, markeert de kwaliteitsmanager deze technische schuld in Quality-time als zodanig om te voorkomen dat de technische schuld ongemerkt verder toeneemt. Vervolgens vraagt de kwaliteitsmanager het Scrumteam, in overleg met de software delivery manager, om de omvang van de technische schuld in te schatten in user-storypunten. Vervolgens wordt een plan gemaakt om de technische schuld in een beheerst tempo - de ontwikkeling/onderhoud van de software moet wel doorgang vinden - weg te werken. Uitgangspunt is ongeveer 10% van de user-storypunten die het Scrumteam normaal in een sprint realiseert; dit kan in principe zonder overleg met de opdrachtgevende organisatie, omdat het leveren van kwaliteit onderdeel van het werk is.

## Beheer

Ten behoeve van de beheerfase wordt gedurende de realisatiefase een implementatie- en beheerplan opgesteld. Hierin worden de kaders aangegeven op welke wijze het beheer ingericht, geïmplementeerd en uitgevoerd wordt.

{Werk dit kwaliteitsplan bij zodra er meer informatie beschikbaar is over de werkwijze ten aanzien van implementatie en beheer}

## Externe testen, toetsen en certificeringen

De volgende externe testen, toetsen en certificeringen zijn gepland:

| Aspect                  | Opdrachtnemer                               | Planning          |
|:------------------------|:--------------------------------------------|:------------------|
| Penetratietest          | {Leverancier uit de ICTU-mantel IT-audits } | {Sprint/Kwartaal} |
| Onderhoudbaarheidstoets | {Leverancier uit de ICTU-mantel IT-audits } | {Sprint/Kwartaal} |
| Toegankelijkheidstoets  | {Leverancier}                               | {Sprint/Kwartaal} |
| {Certificering}         | {Leverancier}                               | {Sprint/Kwartaal} |

Een certificeringenplan wordt opgesteld indien het op te leveren systeem aan specifieke certificeringseisen moet voldoen. Dit plan bevat de activiteiten op welke wijze de certificatie wordt uitgevoerd. Eisen voor te behalen certificaten moeten in het PvE en/of NFE-document benoemd zijn; bijvoorbeeld NEN-ISO/IEC 27001:2017 compliancy.

## Projectspecifieke maatregelen

{Verwijder deze paragraaf indien er geen projectspecifieke kwaliteitsmaatregelen nodig zijn}

Deze paragraaf bevat maatregelen voor functionele en niet-functionele eisen, die via de standaardmaatregelen uit de ICTU-kwaliteitsaanpak en in dit kwaliteitsplan niet voldoende worden geborgd.

| Eis      | Omschrijving                                                           | Extra maatregelen                        | Hoe controleren         | Verificatie                                                       |
|:---------|:-----------------------------------------------------------------------|:-----------------------------------------|:------------------------|:------------------------------------------------------------------|
| {Nummer} | {voorbeeld: onderdeel A moet kunnen worden vervangen door onderdeel B} | {voorbeeld: scenariotest opnemen in MTP} | {voorbeeld: review MTP} | {voorbeeld: dd/mm/jjjj review MTP, test opgenomen in hoofdstuk x} |
| {Nummer} | {Omschrijving}                                                         | {Maatregelen}                            | {Controle}              | {Verificatie}                                                     |

# Kwaliteitsmaatregelen projectafsluiting

De kwaliteitsmanager controleert of de projectafsluiting conform de afspraken daarover in het plan van aanpak van de voorfase en/of de realisatiefase is uitgevoerd.
