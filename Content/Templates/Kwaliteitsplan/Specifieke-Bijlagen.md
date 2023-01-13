## Gebruik van Jira

Gedurende de realisatiefase wordt voor de vastlegging van diverse objecten, zoals user stories en logische testgevallen, gebruik gemaakt van Jira. Scrumteams registreren specifieke informatie gedurende de gehele projectduur. Deze bijlage beschrijft welke informatie vastgelegd wordt in Jira, welke Jira-issuetypen hierbij gebruikt worden en wat de onderlinge relaties zijn. Het project richt hiervoor haar eigen Jira-project in.

### Jira-typen

De gebruikte Jira-typen ondersteunen verschillende inzichten in het project:

**Systeembeschrijving**: De te gebruiken typen geven gezamenlijk de actuele situatie weer van de te ontwikkelen of aan te passen applicatie. Informatie wordt vastgelegd over de systeemfuncties, use cases en logische testgevallen in respectievelijk de Jira-typen _Systeemfunctie_, _Use Case_ en _Logical Test Case_. Zie nadere toelichting hieronder.

**Realisatie-activiteiten**: De te gebruiken typen geven gezamenlijk inzicht in de realisatie-activiteiten: te plannen, onderhanden en/of afgeronde activiteiten. Informatie wordt vastgelegd over epics, stories en onderhanden taken in respectievelijk de Jira-typen _Epic_, _Story_ en _Technical Tasks_. Zie nadere toelichting hieronder.

**Bugs**: Bugs gevonden na oplevering in de acceptatieomgeving worden geregistreerd. Dit kunnen ook bugs zijn uit de productieomgeving die opgelost moeten worden in de applicatie. De informatie over bugs wordt vastgelegd met het Jira-type _Bug_. Zie nadere toelichting hieronder.

### Workflow

Elk Jira-type maakt gebruik van een standaard workflow. Omdat de kwaliteitsrapportage gebruik maakt van deze statussen, is het afwijken van deze stadia ongewenst. Binnen het project worden afspraken gemaakt op welke wijze deze Jira workflow in het realisatie proces wordt geïntegreerd. Mogelijke statussen zijn:

* Status Open: Deze status wordt bereikt na een _Create_- of _Stop Progress_-actie;
* Status In Progress: wordt bereikt na de actie _Start Progress_;
* Status Resolved: wordt bereikt na de actie _Resolve Issue_;
* Status Closed: wordt bereikt na het afsluiten van een issue (_Close Issue_);
* Status Reopened: wordt bereikt na de actie _Reopen Issue_.

### Systeembeschrijving

Het op te leveren systeem is beschreven in documenten zoals projectstartarchitectuur (PSA) en globaal functioneel ontwerp (GFO). De actuele situatie van het systeem kan anders zijn in situatie waarin gefaseerd het gewenste systeem wordt opgeleverd of waarin het systeem door de agile manier van werken reeds vooruitloopt op het GFO. Om de actuele situatie te beschrijven wordt gebruik gemaakt van de Jira-typen _Systeemfunctie_ en _Use Cases_. Tevens zijn de hierbij behorende logische testgevallen beschreven.

#### Systeemfunctie

Het te ontwerpen systeem wordt door het Scrumteam, meestal door een functioneel ontwerper, vastgelegd in Jira door een issue aan te maken van het type _Systeemfunctie_. Een systeemfunctie is de vastlegging van het globaal functioneel ontwerp of delen ervan. Een goedgekeurde versie van het GFO bevat de gewenste situatie van een specifiek release en zal als attachment in het issue bijgevoegd worden.

Een systeemfunctie is beschreven door één of meerdere use cases. Gezamenlijk beschrijven de use cases op elk gewenst moment de actuele situatie van de betreffende systeemfunctie.

#### Use cases

De te realiseren functionaliteit wordt met behulp van de user stories geïmplementeerd. De delen van de systeemfuncties die gerealiseerd zijn, worden met use cases door het Scrumteam vastgelegd (meestal een functioneel ontwerper) door issues aan te maken van het type _Use Case_. De verzameling use cases bevatten de functionele as-is situatie van het systeem en worden middels een Jira link van het type Relates to aan de systeemfunctie gekoppeld. Een use case kan aan slechts één systeemfunctie gekoppeld worden.

#### Logische testgevallen

Logische testgevallen worden door de Scrumteams (normaal gesproken de tester) vastgelegd in Jira door een issue te maken van het type _Logical Test Case_ (LTC). Het logisch testgeval wordt middels een Jira link van het type _Tests_ gekoppeld aan zowel de use case als de user story die hiermee getest wordt. Een LTC heeft betrekking op slechts één use case, maar kan op meerdere stories betrekking hebben.

Het logische testgeval zelf wordt beschreven volgens het Given/When/Then formaat. De Jira-issue heeft hiervoor drie velden:

* De _Given_ van een logisch testgeval beschrijft welke niet-triviale informatie aanwezig wordt verondersteld of in welke context een gebruiker zich bevindt. Bijvoorbeeld: "Gegeven een afgesloten inspectierapport" of "Gegeven een medewerker die zich net heeft geregistreerd". Context die vanzelfsprekend is, bijvoorbeeld dat een gebruiker is ingelogd, hoeft niet expliciet te worden opgeschreven.
* De _When_ van een logisch testgeval beschrijft welke actie de gebruiker doet. Bijvoorbeeld: "Als de inspecteur het afgesloten inspectierapport heropent" of "Als de medewerker zijn registratie bekijkt". Passief taalgebruik ("een rapport wordt geopend") is niet toegestaan, omdat dan niet duidelijk is wie de actie doet. Let ook op dat het testgeval logisch is, dat wil zeggen, geen user interface elementen beschrijft. Dus niet "Als de gemeentemedewerker op het dropdown menu klikt", maar "Als de gemeentemedewerker een type kinderopvang kiest".
* De _Then_ van een logisch testgeval beschrijft hoe het systeem reageert op de actie van de gebruiker, met een focus op datgene wat het testgeval beoogt te testen. Bijvoorbeeld: "Dan toont het systeem het inspectierapport met als startdatum de datum van vandaag" of "Dan toont het systeem de registratie van de gebruiker en dat aantal inlogpogingen 0 is".
Logische testgevallen worden als geautomatiseerd (Automated), handmatig (Manual) of eenmalig te testen (Will not execute) gemarkeerd. Geautomatiseerd betekent dat fysieke testgevallen worden opgenomen in de automatische regressietest (ART) van het project. Handmatig betekent dat het logische testgeval elke sprint handmatig zal worden getest door de testers. Eenmalig betekent dat de tester eenmalig handmatig het logische testgeval zal uitvoeren. In principe dienen alle logische testgevallen te worden geautomatiseerd, tenzij er goede redenen zijn om dat niet te doen, bijvoorbeeld omdat het technisch niet mogelijk is het testgeval te automatiseren. Eenmalige testen doen we bij triviale wijzigingen zoals het aanpassen van een label of de layout van een scherm.

### Realisatie-activiteiten

Gedurende de realisatie sprints worden user stories uitgevoerd. Omdat stories slechts een klein deel van gewenste functionaliteiten bevatten (om story punten niet te hoog te laten zijn), worden epics als containers gedefinieerd. Indien een story wordt opgepakt door het Scrumteam worden sub-taken gedefinieerd door middel van het Jira type Technical Task. Wanneer gedurende de ontwikkeling issues vastgelegd moeten worden, kan dit met behulp van het type _Custom Issue_.

#### Epic

Epics zijn ‘brokken’ functionaliteit die door de user stories worden geïmplementeerd. Ze worden door de Scrumteams (meestal de functioneel ontwerper) vastgelegd in Jira door een issue te maken van het type _Epic_. Een epic wordt middels een Jira link van het type _Realizes_ aan de use case gekoppeld waarvoor functionaliteiten worden geïmplementeerd. Een epic mag op slechts één use case betrekking hebben.

#### User story
User stories worden door de Scrumteams (meestal de product owner of een functioneel ontwerper) vastgelegd in Jira door een issue te maken van het type _Story_. Een story wordt middels een Jira link van het type Changes aan de use case gekoppeld waarvoor functionaliteiten worden geïmplementeerd, en middels het veld Epic link aan de epic die gerealiseerd wordt. De story mag op slechts één use case betrekking hebben.

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

## Periodieke controles

Ondanks dat het de voorkeur heeft zoveel mogelijk kwaliteitsaspecten van de software en het softwareproces geautomatiseerd te meten is dit niet altijd mogelijk of kosteneffectief. Daarom voert de kwaliteitsmanager periodiek onderstaande controles handmatig uit.

{Pas onderstaande lijst van controles aan waar relevant. Voeg indien releant kolommen toe voor frequentie, uitvoerder, datum laatste controle, status, vervolgacties, datum volgende controle, etc.}

| Onderwerp | Referentie | Controle |
|:----------|:-----------|:---------|
| Verwerking niet-functionele eisen | M01 | Actuele NFE's zijn verwerkt in SAD en kwaliteitsplan |
| Verwerking informatiebeveiligingsplan | M01 | Actuele beveiligingsmaatregelen zijn verwerkt in SAD, GFO en kwaliteitsplan |
| Traceerbaarheid functionele eisen | M03 | Functionele functionele eisen zijn traceerbaar naar logische en fysieke testgevallen |
| Traceerbaarheid niet-functionele eisen | M03 | Niet-functionele eisen zijn traceerbaar naar SAD, MTP en detailtestplannen |
| Implementatie nieuwe versie Kwaliteitsaanpak | M09 | De meest recente versie van de Kwaliteitsaanpak is geïmplementeerd in het project |
| Gebruik tools | M16 | Het project gebruikt de geadviseerde tools |
| Actualiteit tools | M16 | Het project gebruikt actuele versies van tools |
| Uitvoering self-assessment | M28 | Het project heeft recent een self-assessment uitgevoerd |
| Actualiteit self-assessment | M28 | De kwaliteitsrapportage bevat een metriek voor de actualiteit van de self-assessment |
| Versiebeheer van documenten | Kwaliteitsplan §3.2.1 | Documenten zijn met de juiste meta-informatie op de afgesproken plaats en wijze opgeslagen |
| Review van documenten | Kwaliteitsplan §3.3.2 | Documenten zijn op de afgesproken wijze gereviewd |
| Definition of Ready | Kwaliteitsplan §5.1.1 | Scrumteams hebben en gebruiken een DoR |
| Definition of Done | Kwaliteitsplan §5.1.2 | Scrumteams hebben en gebruiken een DoD |
| Vrijgaveadvies | Kwaliteitsplan §5.1.3 | Het vrijgaveadvies bevat de afgesproken onderdelen |
| Kwaliteit broncode | Kwaliteitsplan §5.3 | Onderdrukte SonarQube-waarschuwingen zijn afgestemd en (nog steeds) terecht |
| Kwaliteit broncode | Kwaliteitsplan §5.3 | De kwaliteit van de broncode voldoet bij een steekproefsgewijze, handmatige inspectie aan de eisen |
| Beveiliging broncode | Kwaliteitsplan §5.10 | Onderdrukte beveiligingsbevindingen uit de OWASP Dependency Check en Checkmarx zijn afgestemd en (nog steeds) terecht |
| Beveiligingstesten | Kwaliteitsplan §5.10 | Beveiligingsissues uit securitytesten zijn opgenomen in Jira en volgens de oplostermijnen opgelost |
| Projectspecifieke kwaliteitsmaatregelen | Kwaliteitsplan §5.16 | Projectspecifieke maatregelen zijn uitgevoerd zoals afgesproken |
| Projectafsluiting | Kwaliteitsplan §6 | Projectafsluiting is conform de afspraken uitgevoerd |
| Gebruik van Jira | Kwaliteitsplan bijlage D | Jira wordt gebruikt zoals afgesproken |
| Actualiteit kwaliteitsplan | | De kwaliteitsrapportage bevat een metriek voor de actualiteit van het kwaliteitsplan |
| Nieuwe teamleden | | Nieuwe teamleden zijn op de hoogte van de Kwaliteitsaanpak, het kwaliteitssysteem en het kwaliteitsplan |
| Vertrokken teamleden | | Alle rechten in tools (GitLab, GitHub, Trello, Sharepoint, VPN, Jira, Whatsapp, Signal, Slack, etc.) van vertrokken teamleden zijn ingetrokken |
