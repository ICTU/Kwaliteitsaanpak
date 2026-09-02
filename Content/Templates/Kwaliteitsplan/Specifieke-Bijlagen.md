## Gebruik van Jira

Gedurende de realisatiefase wordt voor de vastlegging van diverse objecten, zoals user stories en logische testgevallen, gebruik gemaakt van Jira. Scrumteams registreren specifieke informatie gedurende de gehele projectduur. Deze bijlage beschrijft welke informatie vastgelegd wordt in Jira, welke Jira-issuetypen hierbij gebruikt worden en wat de onderlinge relaties zijn. Het project richt hiervoor haar eigen Jira-project in.

### Jira-typen

De gebruikte Jira-typen ondersteunen verschillende inzichten in het project:

**Systeembeschrijving**: De te gebruiken typen geven gezamenlijk de actuele situatie weer van de te ontwikkelen of aan te passen applicatie. Informatie wordt vastgelegd over de use cases en logische testgevallen in respectievelijk de Jira-typen _Use Case_ en _Logical Test Case_. Zie nadere toelichting hieronder.

**Realisatie-activiteiten**: De te gebruiken typen geven gezamenlijk inzicht in de realisatie-activiteiten: te plannen, onderhanden en/of afgeronde activiteiten. Informatie wordt vastgelegd over epics, stories en onderhanden taken in respectievelijk de Jira-typen _Epic_, _Story_ en _Technical Task_. Zie nadere toelichting hieronder.

**Bugs**: Bugs gevonden na oplevering in de acceptatieomgeving worden geregistreerd. Dit kunnen ook bugs zijn uit de productieomgeving die opgelost moeten worden in de applicatie. De informatie over bugs wordt vastgelegd met het Jira-type _Bug_. Zie nadere toelichting hieronder.

### Workflow

Elk Jira-type maakt gebruik van een standaard workflow. Omdat de kwaliteitsrapportage gebruik maakt van deze statussen, is het afwijken van deze stadia ongewenst. Binnen het project worden afspraken gemaakt op welke wijze deze Jira workflow in het realisatie proces wordt geïntegreerd. Mogelijke statussen zijn:

* Status Open: Deze status wordt bereikt na een _Create_- of _Stop Progress_-actie;
* Status In Progress: wordt bereikt na de actie _Start Progress_;
* Status Resolved: wordt bereikt na de actie _Resolve Issue_;
* Status Closed: wordt bereikt na het afsluiten van een issue (_Close Issue_);
* Status Reopened: wordt bereikt na de actie _Reopen Issue_.

### Systeembeschrijving

Het op te leveren systeem is beschreven in documenten zoals globaal functioneel ontwerp (GFO) en software-architectuurdocument (SAD). De actuele situatie van het systeem kan anders zijn in situatie waarin gefaseerd het gewenste systeem wordt opgeleverd of waarin het systeem door de agile manier van werken reeds vooruitloopt op het GFO. Om de actuele situatie te beschrijven wordt gebruik gemaakt van use cases. Logische testgevallen beschrijven hoe de use cases worden getest.

#### Use cases

De te realiseren functionaliteit wordt met behulp van de user stories geïmplementeerd. De delen van de systeemfuncties die gerealiseerd zijn, worden met use cases door het Scrumteam vastgelegd (meestal een functioneel ontwerper) door issues aan te maken van het type _Use Case_. De verzameling use cases beschrijft de functionele as-is situatie van het systeem.

#### Logische testgevallen

Logische testgevallen worden door de Scrumteams (normaal gesproken de tester) vastgelegd in Jira door een issue te maken van het type _Logical Test Case_ (LTC). Het logisch testgeval wordt middels een Jira link van het type _Tests_ gekoppeld aan zowel de use case als de user story die hiermee getest wordt.

Het logische testgeval zelf wordt beschreven volgens het Given/When/Then formaat. De Jira-issue heeft hiervoor drie velden:

* De _Given_ van een logisch testgeval beschrijft welke niet-triviale informatie aanwezig wordt verondersteld of in welke context een gebruiker zich bevindt. Bijvoorbeeld: "Gegeven een afgesloten inspectierapport" of "Gegeven een medewerker die zich net heeft geregistreerd". Context die vanzelfsprekend is, bijvoorbeeld dat een gebruiker is ingelogd, hoeft niet expliciet te worden opgeschreven.
* De _When_ van een logisch testgeval beschrijft welke actie de gebruiker doet. Bijvoorbeeld: "Als de inspecteur het afgesloten inspectierapport heropent" of "Als de medewerker zijn registratie bekijkt". Passief taalgebruik ("een rapport wordt geopend") is niet toegestaan, omdat dan niet duidelijk is wie de actie doet. Let ook op dat het testgeval logisch is, dat wil zeggen, geen user interface elementen beschrijft. Dus niet "Als de gemeentemedewerker op het dropdown menu klikt", maar "Als de gemeentemedewerker een type kinderopvang kiest".
* De _Then_ van een logisch testgeval beschrijft hoe het systeem reageert op de actie van de gebruiker, met een focus op datgene wat het testgeval beoogt te testen. Bijvoorbeeld: "Dan toont het systeem het inspectierapport met als startdatum de datum van vandaag" of "Dan toont het systeem de registratie van de gebruiker en dat aantal inlogpogingen 0 is".
Logische testgevallen worden als geautomatiseerd (Automated), handmatig (Manual) of eenmalig te testen (Will not execute) gemarkeerd. Geautomatiseerd betekent dat fysieke testgevallen worden opgenomen in de automatische regressietest (ART) van het project. Handmatig betekent dat het logische testgeval elke sprint handmatig zal worden getest door de testers. Eenmalig betekent dat de tester eenmalig handmatig het logische testgeval zal uitvoeren. In principe dienen alle logische testgevallen te worden geautomatiseerd, tenzij er goede redenen zijn om dat niet te doen, bijvoorbeeld omdat het technisch niet mogelijk is het testgeval te automatiseren. Eenmalige testen doen we bij triviale wijzigingen zoals het aanpassen van een label of de layout van een scherm.

### Realisatie-activiteiten

Gedurende de realisatie sprints worden user stories uitgevoerd. Omdat stories slechts een klein deel van gewenste functionaliteiten bevatten (om story punten niet te hoog te laten zijn), worden epics als containers gedefinieerd. Indien een story wordt opgepakt door het Scrumteam worden sub-taken gedefinieerd door middel van het Jira type Technical Task. Wanneer gedurende de ontwikkeling issues vastgelegd moeten worden, kan dit met behulp van het type _Custom Issue_.

#### Epic

Epics zijn ‘brokken’ functionaliteit die door de user stories worden geïmplementeerd. Ze worden door de Scrumteams (meestal de functioneel ontwerper) vastgelegd in Jira door een issue te maken van het type _Epic_. Een epic wordt middels een Jira link van het type _Realizes_ aan de use case gekoppeld waarvoor functionaliteiten worden geïmplementeerd.

#### User story
User stories worden door de Scrumteams (meestal de product owner of een functioneel ontwerper) vastgelegd in Jira door een issue te maken van het type _Story_. Een story wordt middels een Jira link van het type Changes aan de use case gekoppeld waarvoor functionaliteiten worden geïmplementeerd, en middels het veld Epic link aan de epic die gerealiseerd wordt.

De user story zelf wordt beschreven in het formaat: "Als <rol> wil ik <actie> zodat <rationale die duidelijk maakt wat de business waarde is>". Voorbeelden zijn: "Als medewerker van ICTU wil ik een parkeerplaats voor een bezoeker kunnen reserveren zodat deze niet op zoek hoeft naar een parkeerplaats" of "Als aankomend medewerker in de kinderopvang wil ik mijn VOG registreren in het register voor medewerkers in de kinderopvang omdat ik anders niet mag werken in de kinderopvang". De tekst van de user story dienst in het description veld van het issue te worden vastgelegd zodat de user story tekst goed in de rapportages komt.

Bij elke user story kan worden vastgelegd wat het risico van de verandering is op verschillende aspecten zoals planning, performance en security. Dit maakt het mogelijk om user stories te filteren op, bijvoorbeeld, hoog risico voor security en die lijst als input voor een securitytest te gebruiken.

#### Technical tasks

Gedurende de realisatie van een user story worden door het Scrumteam diverse activiteiten uitgevoerd. Om de sprint voortgang eenvoudiger te kunnen monitoren, wordt gebruik gemaakt van sub-taken binnen een user story. Deze kunnen automatisch aangemaakt worden (aanvragen via Jira), of handmatig door het Scrumteam vastgelegd worden door _Create Sub-task_ type _Technical Task_. Een technical task heeft het formaat <werkwoord> <onderwerp>. Voorbeelden zijn: Opstellen logische testgevallen, Review testgevallen, Ontwikkelen <module>, Uitvoeren handmatige testen, Ontwikkelen ART, Controleren kwaliteitsrapportages, Bijwerken use cases, Check code kwaliteit en testcoverage, etc.

#### Bugs

Bugs zijn afwijkingen tussen verwacht gedrag en actuele situatie die is gedetecteerd. Het kunnen bugs zijn die gevonden worden tijdens acceptatietesten of productieverstoringen. De bugs worden vastgelegd door Jira issues aan te maken van het type _Bug_.

De bug moet bij registreren alle informatie bevatten die nodig is om de geconstateerde afwijking, gebruikte omgeving en situatie te beschrijven, de prioriteit i.r.t. impact en urgentie, specifieke labels die gebruikt worden in de kwaliteitsrapportage om type bugs te kunnen onderkennen (bijvoorbeeld Security, Performance), en de referentie naar het gebruikte testgeval i.g.v. testen.

* Blocker: applicatie of bedrijfskritische functies/processen kunnen niet gebruikt worden;
* Critical: bedrijfskritische functies/processen worden negatief beïnvloed en er is geen workaround mogelijk;
* Major: critical, maar workaround mogelijk;
* Minor/Trivial: raakt geen bedrijfskritische functies/processen.

Indien de bug opgelost gaat worden, zal er een Jira link van het type _Is realized by_ gelegd worden naar die betreffende user story waarin de bug wordt opgepakt; middels comments wordt informatie toegevoegd over de analyse, de alternatieven en de uiteindelijk gekozen oplossing.

## Periodieke handmatige controles

Ondanks dat het de voorkeur heeft zoveel mogelijk kwaliteitsaspecten van de software en het softwareproces geautomatiseerd te meten is dit niet altijd mogelijk of kosteneffectief. Daarom voert de kwaliteitsmanager periodiek onderstaande controles handmatig uit.

{Pas onderstaande lijst van controles aan waar nodig. Voeg indien relevant kolommen toe voor frequentie, uitvoerder, datum laatste controle, status, vervolgacties, datum volgende controle, etc.}

| Onderwerp                                    | Referentie               | Controle                                                                                                                             |
|:---------------------------------------------|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Verwerking informatiebeveiligingsplan        | M01                      | Actuele beveiligingsmaatregelen zijn verwerkt in SAD, GFO en kwaliteitsplan                                                          |
| Traceerbaarheid functionele eisen            | M03                      | Functionele functionele eisen zijn traceerbaar naar logische en fysieke testgevallen                                                 |
| Traceerbaarheid niet-functionele eisen       | M03                      | Niet-functionele eisen zijn traceerbaar naar SAD, MTP en detailtestplannen                                                           |
| Verificatie realisatie niet-functionele eisen     | Niet-functionele eisen   | Verificatie van aan ICTU toegewezen niet-functionele eisen is actueel                                               |
| Implementatie nieuwe versie Kwaliteitsaanpak | M28                      | De meest recente versie van de Kwaliteitsaanpak is geïmplementeerd in het project                                                    |
| Gebruik tools                                | M16                      | Het project gebruikt de geadviseerde tools                                                                                           |
| Actualiteit tools                            | M16                      | Het project gebruikt actuele versies van tools                                                                                       |
| Uitvoering self-assessment                   | M28                      | Het project heeft recent een self-assessment uitgevoerd waarin de verschillende maatregelen ook inhoudelijk zijn beoordeeld          |
| Actualiteit self-assessment                  | M28                      | De kwaliteitsrapportage bevat een metriek voor de actualiteit van de self-assessment                                                 |
| Versiebeheer van documenten                  | Kwaliteitsplan §3.2.1    | Documenten zijn met de juiste meta-informatie op de afgesproken plaats en wijze opgeslagen                                           |
| Review van documenten                        | Kwaliteitsplan §3.2.2    | Documenten zijn op de afgesproken wijze gereviewd                                                                                    |
| Projectspecifieke kwaliteitsmaatregelen      | Kwaliteitsplan §5.1      | Projectspecifieke maatregelen zijn uitgevoerd zoals afgesproken                                                                      |
| Definition of Ready                          | Kwaliteitsplan §5.2.1    | Scrumteams hebben en gebruiken een DoR                                                                                               |
| Definition of Done                           | Kwaliteitsplan §5.2.2    | Scrumteams hebben en gebruiken een DoD, waarin het voldoen aan de kwaliteitsnormen is opgenomen                                      |
| Vrijgaveadvies                               | Kwaliteitsplan §5.2.3    | Het project levert de afgesproken informatie ten behoeve van het vrijgaveadvies                                                      |
| Kwaliteit broncode                           | Kwaliteitsplan §5.4      | Onderdrukte SonarQube-waarschuwingen zijn afgestemd en (nog steeds) terecht                                                          |
| Kwaliteit broncode                           | Kwaliteitsplan §5.4      | De kwaliteit van de broncode voldoet bij een steekproefsgewijze, handmatige inspectie aan de eisen                                   |
| Beveiliging broncode                         | Kwaliteitsplan §5.11     | Onderdrukte beveiligingsbevindingen uit OWASP Dependency-Check, Dependency-Track en SonarQube zijn afgestemd en (nog steeds) terecht |
| Beveiligingstesten                           | Kwaliteitsplan §5.11     | Beveiligingsissues uit securitytesten zijn opgenomen in Jira en volgens de oplostermijnen opgelost                                   |
| Projectafsluiting                            | Kwaliteitsplan §6        | Projectafsluiting is conform de afspraken uitgevoerd                                                                                 |
| Gebruik van Jira                             | Kwaliteitsplan bijlage D | Jira wordt gebruikt zoals afgesproken                                                                                                |
| Actualiteit kwaliteitsplan                   |                          | De kwaliteitsrapportage bevat een metriek voor de actualiteit van het kwaliteitsplan                                                 |
| Nieuwe teamleden                             |                          | Nieuwe teamleden zijn op de hoogte van de Kwaliteitsaanpak, het kwaliteitssysteem (Quality-time) en het kwaliteitsplan               |
| Vertrokken teamleden                         |                          | Alle rechten in tools (GitLab, GitHub, Trello, SharePoint, VPN, Jira, Signal, Slack, etc.) van vertrokken teamleden zijn ingetrokken |

## ICTU-spelregels voor het beheer van dependencies

Het beheren en bijwerken van dependencies is een belangrijk onderdeel van softwareontwikkeling en -onderhoud. Enerzijds bieden nieuwe versies van dependencies nieuwe en/of verbeterde functionaliteit en repareren fouten en beveiligingskwetsbaarheden. Anderzijds brengen nieuwe versies het risico op nieuwe fouten, beveiligingskwetsbaarheden en supply-chain attacks met zich mee. Voor het beheren en bijwerken van dependencies gelden dan ook onderstaande spelregels, waarbij afwijken kan, maar met een goede reden.

De spelregels gelden voor alle dependencies in de software en de CI-pipeline: directe en indirecte dependencies, inclusief images gebruikt in Dockerfiles, Helm charts, pre-commit hooks en CI-pipeline definities.

### Dependencies toevoegen

Het beheren en bijwerken van een dependency is alleen nodig als die dependency er überhaupt is. De eerste spelregel gaat dan ook over het toevoegen van dependencies.

1. Controleer voor toevoegen van een nieuwe dependency of deze wordt onderhouden. Kijk naar licentie, supportopties, community chatter, aantal actieve maintainers, recente releases en release beleid (zijn er LTS releases, hebben major releases een geplande EOL), commit activiteit, open security issues, open pull requests en eventuele projectarchivering. Als een dependency niet onderhouden lijkt, kies dan een andere dependency, bouw de functionaliteit zelf of vendor de dependency.

### Dependencies specificeren

Doel van de spelregels voor het specificeren van dependencies is om te voorkomen dat er onbedoeld en ongemerkt andere versies van dependencies worden geïnstalleerd dan gedacht. Dit vermindert de kwetsbaarheid voor supply-chain attacks en is ook beter voor de herhaalbaarheid van builds.

2. Gebruik geen unpinned tags: dus geen `latest` of andere tags die niet naar één versie wijzen, zoals `trixie` of `windows`. Gebruik in plaats daarvan versietags, bijvoorbeeld `13.6.0`, of snapshottags, bijvoorbeeld `trixie-20260713`.
3. Pin dependencies met de grootste precisie die mogelijk is: dus `3.14.5` in plaats van `3.14` of `3`. Gebruik dus ook geen versierange, zoals `requests>=2.34`, tenzij de software een library is.
4. Pin dependencies met hashes (digests, commit SHA, integrity hashes) waar mogelijk. Package managers doen dit veelal zelf met een lockfile. Plaats in dat geval de lockfile onder versiebeheer en gebruik deze om dependencies te installeren zonder ook te updaten (bijvoorbeeld `npm ci` of `uv sync --locked` in build pipelines). Gebruik voor dependencies zonder package manager een tool als Renovate, Dependabot of Update-time. Het registeren van én een versie én een hash lijkt wellicht dubbele administratie, maar aan de hash pin is niet eenvoudig te zien welke versie gebruikt wordt en tools kunnen veelal beiden tegelijk bijwerken.
5. Haal dependencies binnen via de interne registry of proxy van het project, bijvoorbeeld Nexus of Harbor, en niet rechtstreeks van publieke registries. Controleer de herkomst van een dependency waar dat mogelijk is, bijvoorbeeld via ondertekende releases, provenance-attestaties of ondertekende images.

### Dependencies bijwerken

Doel van de spelregels voor het bijwerken van dependencies is om de risico's die nieuwe versies met zich meebrengen te beperken.

6. Gebruik een cooldown van minstens 7 dagen voor het toepassen van een nieuwe versie. Weeg bij het kiezen van een langere cooldownperiode bewust het lagere risico op supply-chain attacks af tegen het hogere beveiligingsrisico door het later ontvangen van security fixes. Sla bij een kritische security fix de cooldown eventueel (incidenteel) over. Configuur de voor updates gebruikte tools om de cooldown te hanteren, bijvoorbeeld `min-release-age` in `.npmrc` of uv's `exclude-newer` in `pyproject.toml`.
7. Beoordeel voor het updaten naar een major release van een dependency het risico van de nieuwe release. Kijk of de nieuwe release veranderingen bevat die het risico op regressies vergroten, zoals veel nieuwe functionaliteit, backwards-incompatible changes of grote refactorings. Wacht in dat geval op de eerste of tweede patchrelease voor het bijwerken van de versie.
8. Gebruik tooling om dependencies periodiek (bijvoorbeeld éénmaal per sprint) te updaten, bijvoorbeeld met de package manager, Renovate, Dependabot of Update-time.
9. Behandel een update van een dependency als elke andere wijziging: open een merge request, lees de release notes of changelog van de nieuwe versie op breaking changes, gedragsveranderingen en verdachte wijzigingen, en controleer dat de volledige pipeline slaagt. Merge updates niet automatisch. Stel bij een major update expliciet vast welke aanpassingen aan de eigen software nodig zijn.

### Dependencies monitoren

Tenslotte spelregels om dependencies te monitoren op nieuwe risico's die ontstaan of bekend worden na de update.

10. Draai dagelijks de auditfunctie van de package manager, bijvoorbeeld `npm audit` of `pip-audit`, of analyseer dagelijks de actuele SBOM, bijvoorbeeld in Dependency-Track, om dependencies te checken op bekende kwetsbaarheden. Nieuwe kwetsbaarheden worden immers dagelijks ontdekt, ook als de eigen software niet verandert. Analyseer de ernst van de uitkomsten en neem mitigerende maatregelen (bijvoorbeeld dependencies eerder upgraden, downgraden, of vervangen) of accepteer expliciet het risico.
11. Analyseer periodiek, bijvoorbeeld éénmaal per kwartaal, of een dependency nog onderhouden wordt. Controleer dezelfde punten als bij spelregel 1. Als een dependency niet meer onderhouden lijkt, neem dan een mitigerende maatregel (bijvoorbeeld migreren, vendoren of zelf bouwen) of accepteer expliciet het risico.
