## Gebruik van Jira

Gedurende de realisatiefase wordt voor de vastlegging van diverse objecten, zoals user stories en logische testgevallen, gebruik gemaakt van Jira. Teams registreren specifieke informatie gedurende de gehele projectduur. Deze bijlage beschrijft welke informatie vastgelegd wordt in Jira, welke Jira-issuetypen hierbij gebruikt worden en wat de onderlinge relaties zijn. Het project richt hiervoor haar eigen Jira-project in. 

### Jira-typen

De gebruikte Jira-typen ondersteunen verschillende inzichten in het project:

**Systeembeschrijving**: De te gebruiken typen geven gezamenlijk de actuele situatie weer van de te ontwikkelen of aan te passen applicatie. Informatie wordt vastgelegd over de systeemfuncties, use cases en logische testgevallen in respectievelijk de Jira-typen _Systeemfunctie_, _Use Case_ en _Logical Test Case_. Zie nadere toelichting hieronder.

**Realisatie-activiteiten**: De te gebruiken typen geven gezamenlijk inzicht in de realisatie-activiteiten: te plannen, onderhanden en/of afgeronde activiteiten. Informatie wordt vastgelegd over epics, stories, onderhanden taken, sprint-bugs en sprint-issues in respectievelijk de Jira-typen _Epic_, _Story_, _Technical Tasks_, _Sprint Bug_ en _Custom Issue_. Zie nadere toelichting hieronder.

**Gedetecteerde bugs**: De gevonden bugs na oplevering in de acceptatieomgeving worden geregistreerd. Dit kunnen ook bugs zijn uit de productieomgeving die opgelost moeten worden in de applicatie. Deinformatie over bugs wordt vastgelegd met het Jira-type _Bug_. Zie nadere toelichting hieronder.

### Workflow

Elk Jira-type maakt gebruik van een standaard workflow. Omdat de kwaliteitsrapportage gebruik maakt van deze statussen, is het afwijken van deze stadia ongewenst. Binnen het project worden afspraken gemaakt op welke wijze deze Jira workflow in het realisatie proces wordt geïntegreerd. Mogelijke statussen zijn:

* Status Open: Deze status wordt bereikt na een _Create_- of _Stop Progress_-actie;
* Status In Progress: wordt bereikt na de actie _Start Progress_;
* Status Resolved: wordt bereikt na de actie _Resolve Issue_;
* Status Closed: wordt bereikt na het afsluiten van een issue (_Close Issue_);
* Status Reopened: wordt bereikt na de actie _Reopen Issue_.

### Systeembeschrijving

Het op te leveren systeem is beschreven in documenten zoals projectstartarchitectuur (PSA) en globaal functioneel ontwerp (GFO). De actuele situatie van het systeem kan anders zijn in situatie waarin gefaseerd het gewenste systeem wordt opgeleverd of waarin het systeem door de agile-manier van werken reeds vooruit loopt op het GFO. Om de actuele situatie te beschrijven wordt gebruik gemaakt van de Jira-typen _Systeemfunctie_ en _Use Cases_. Tevens zijn de hierbij behorende logische testgevallen beschreven.

**Systeemfunctie**
Het te ontworpen systeem wordt door het team, meestal door een functioneel ontwerper, vastgelegd in Jira door een issue aan te maken van het type _Systeemfunctie_. Een systeemfunctie is de vastlegging van het globaal functioneel ontwerp of delen ervan. Een goedgekeurde versie van het GFO bevat de gewenste situatie van een specifiek release en zal als attachment in het issue bijgevoegd worden.

Een systeemfunctie is beschreven door één of meerdere use cases. Gezamenlijk beschrijven de use cases op elk gewenst moment de actuele situatie van de betreffende systeemfunctie.

**Use cases**
De te realiseren functionaliteit wordt met behulp van de user stories geïmplementeerd. De delen van de systeemfuncties die gerealiseerd zijn, worden met use cases door het team vastgelegd (meestal een functioneel ontwerper) door issues aan te maken van het type _Use Case_. De verzameling use cases bevatten de functionele as-is situatie van het systeem en worden middels een Jira link van het type Relates to aan de systeemfunctie gekoppeld. Een use case kan aan slechts één systeemfunctie gekoppeld worden.

**Logische testgevallen**
Logische testgevallen worden door de teams (normaal gesproken de tester) vastgelegd in Jira door een issue te maken van het type _Logical Test Case_ (LTC). Het logisch testgeval wordt middels een Jira link van het type _Tests_ gekoppeld aan zowel de use case als de user story die hiermee getest wordt. Een LTC heeft betrekking op slechts één use case, maar kan op meerdere stories betrekking hebben.

Het logische testgeval zelf wordt beschreven volgens het Given/When/Then formaat. De Jira-issue heeft hiervoor drie velden:

* De _Given_ van een logisch testgeval beschrijft welke niet-triviale informatie aanwezig wordt verondersteld of in welke context een gebruiker zich bevindt. Bijvoorbeeld: "Gegeven een afgesloten inspectierapport" of "Gegeven een medewerker die zich net heeft geregistreerd". Context die vanzelfsprekend is, bijvoorbeeld dat een gebruiker is ingelogd, hoeft niet expliciet te worden opgeschreven.
* De _When_ van een logisch testgeval beschrijft welke actie de gebruiker doet. Bijvoorbeeld: "Als de inspecteur het afgesloten inspectierapport heropent" of "Als de medewerker zijn registratie bekijkt". Passief taalgebruik ("een rapport wordt geopend") is niet toegestaan, omdat dan niet duidelijk is wie de actie doet. Let ook op dat het testgeval logisch is, dat wil zeggen, geen user interface elementen beschrijft. Dus niet "Als de gemeentemedewerker op het dropdown menu klikt", maar "Als de gemeentemedewerker een type kinderopvang kiest".
* De _Then_ van een logisch testgeval beschrijft hoe het systeem reageert op de actie van de gebruiker, met een focus op datgene wat het testgeval beoogt te testen. Bijvoorbeeld: "Dan toont het systeem het inspectierapport met als startdatum de datum van vandaag" of "Dan toont het systeem de registratie van de gebruiker en dat aantal inlogpogingen 0 is". 
Logische testgevallen worden als geautomatiseerd (Automated), handmatig (Manual) of eenmalig te testen (Will not execute) gemarkeerd. Geautomatiseerd betekent dat fysieke testgevallen worden opgenomen in de automatische regressietest (ART) van het project. Handmatig betekent dat het logische testgeval elke sprint handmatig zal worden getest door de testers. Eenmalig betekent dat de tester eenmalig handmatig het logische testgeval zal uitvoeren. In principe dienen alle logische testgevallen te worden geautomatiseerd, tenzij er goede redenen zijn om dat niet te doen, bijvoorbeeld omdat het technisch niet mogelijk is het testgeval te automatiseren. Eenmalige testen doen we bij triviale wijzigingen zoals het aanpassen van een label of de layout van een scherm.

### Realisatie-activiteiten

Gedurende de realisatie sprints worden user stories uitgevoerd. Omdat stories slechts een klein deel van gewenste functionaliteiten bevatten (om story punten niet te hoog te laten zijn), worden epics als containers gedefinieerd. Indien een story wordt opgepakt door het team worden sub-taken gedefinieerd door middel van het Jira type Technical Task en bij het unit testen en/of systeemtesten worden gevonden fouten middels sprint-bugs vastgelegd. Wanneer gedurende de ontwikkeling issues vastgelegd moeten worden, kan dit met behulp van het type _Custom Issue_.

**Epic**
Epics zijn ‘brokken’ functionaliteit die door de user stories worden geïmplementeerd. Ze worden door de teams (meestal de functioneel ontwerper) vastgelegd in Jira door een issue te maken van het type _Epic_. Een epic wordt middels een Jira link van het type _Realizes_ aan de use case gekoppeld waarvoor functionaliteiten worden geïmplementeerd. Een epic mag op slechts één use case betrekking hebben.

**User story**
User stories worden door de teams (meestal de product owner of een functioneel ontwerper) vastgelegd in Jira door een issue te maken van het type _Story_. Een story wordt middels een Jira link van het type Changes aan de use case gekoppeld waarvoor functionaliteiten worden geïmplementeerd, en middels het veld Epic link aan de epic die gerealiseerd wordt. De story mag op slechts één use case betrekking hebben.

De user story zelf wordt beschreven in het formaat: "Als <rol> wil ik <actie> zodat <rationale die duidelijk maakt wat de business waarde is>". Voorbeelden zijn: "Als medewerker van ICTU wil ik een parkeerplaats voor een bezoeker kunnen reserveren zodat deze niet op zoek hoeft naar een parkeerplaats" of "Als aankomend medewerker in de kinderopvang wil ik mijn VOG registreren in het register voor medewerkers in de kinderopvang omdat ik anders niet mag werken in de kinderopvang". De tekst van de user story dienst in het description veld van het issue te worden vastgelegd zodat de user story tekst goed in de rapportages komt.

**Technical tasks**
Gedurende de realisatie van een user story worden door het team diverse activiteiten uitgevoerd. Om de sprint voortgang eenvoudiger te kunnen monitoren, wordt gebruik gemaakt van sub-taken binnen een user story. Deze kunnen automatisch aangemaakt worden (aanvragen via Jira team), of handmatig door het team vastgelegd worden (meestal door de scrum master) door _Create Sub-task_ type _Technical Task_. Een technical task heeft het formaat <werkwoord> <onderwerp>. Voorbeelden zijn: Opstellen logische testgevallen, Review testgevallen, Ontwikkelen <module>, Uitvoeren handmatige testen, Ontwikkelen ART, Controleren kwaliteitsrapportages, Bijwerken use cases, Check code kwaliteit en testcoverage, etc.

**Sprint bugs**
De afwijkingen tussen verwacht gedrag en actuele situatie die gedurende de sprint worden gedetecteerd, kunnen worden vastgelegd door het team, veelal de tester. Dit kan met het type _Bug_ of door _Create Sub-task_ type _Sprint Bug_ in de user story. Het project maakt afspraken of deze afwijkingen worden vastgelegd en van welk type er gebruik gemaakt zal gaan worden.

De sprint bug beschrijft de geconstateerde afwijking op een duidelijke en eenduidige wijze, het gebruikte testgeval en omgeving, en de prioriteit (=impact x urgency).

* Blocker: sprint release demo zal niet uitgevoerd kunnen worden;
* Critical: sprint release demo kan wel uitgevoerd worden, maar belangrijke functionaliteiten ontbreken of zijn onjuist;
* Major: als critical, maar workaround mogelijk;
* Minor: functionaliteit is niet geheel correct, maar dit heeft niet of nauwelijks invloed op de demo;
* Trivial: issues zijn cosmetisch en hebben niet of nauwelijks invloed op de demo.

In de kwaliteitsrapportage wordt gerapporteerd over het aantal non-closed (sprint) bugs. 

**Custom issues**
Gedurende de realisatie van de epics kunnen er issues zijn die van belang zijn om formeel vast te leggen en de voortgang te bewaken. Dit kunnen bijvoorbeeld onduidelijkheden zijn die niet specifiek betrekking hebben op een user story of openstaande activiteiten die user story overstijgend zijn.
Deze issues kunnen vastgelegd worden door het team door Jira issues aan te maken van het type Custom issue, en gekoppeld worden aan de gerelateerde epic middels een Jira link van het type Relates to. Een custom issue heeft slechts betrekking op één epic.

Het gebruik van custom issues is optioneel.

**Gedetecteerde bugs**
Bugs zijn afwijkingen tussen verwacht gedrag en actuele situatie die is gedetecteerd. Het kunnen bugs betreffen gedurende de sprints (zie ook type _Sprint Bug_), gedurende acceptatietesten of productieverstoringen. De bugs worden vastgelegd door Jira issues aan te maken van het type _Bug_.

De bug moet bij registreren alle informatie bevatten die nodig is om de geconstateerde afwijking, gebruikte omgeving en situatie te beschrijven, de prioriteit i.r.t. impact en urgentie, specifieke labels die gebruikt worden in de kwaliteitsrapportage om type bugs te kunnen onderkennen (bijvoorbeeld Security, Performance), en de referentie naar het gebruikte testgeval i.g.v. testen.

* Blocker: applicatie of bedrijfskritische functies/processen kunnen niet gebruikt worden;
* Critical: bedrijfskritische functies/processen worden negatief beïnvloed en er is geen workaround mogelijk;
* Major: critical, maar workaround mogelijk;
* Minor/Trivial: raakt geen bedrijfskritische functies/processen.

Indien de bug opgelost gaat worden, zal er een Jira link van het type _Is realized by_ gelegd worden naar die betreffende user story waarin de bug wordt opgepakt; middels comments wordt informatie toegevoegd over de analyse, de alternatieven en de uiteindelijk gekozen oplossing.

### Velden in JIra

Het ICTU-kwaliteitssysteem voert verschillende controles uit op user stories (US) en logische testgevallen (LTC). Hieronder is in een overzicht gegeven welke controle er wordt uitgevoerd, welke metriekbron hiervoor wordt geraadpleegd en een korte beschrijving op welke plek in Jira deze administratie bijgehouden dient te worden:

| Controle  | Metriekbron | Beschrijving |
|:-----|:----|:----|
| Ready user story zonder security risk beoordeling | Jira filter | Betreffende US bevat een tab “Risks”, hier wordt de zwaarte van het Security Risk beoordeeld |
| Ready user story zonder performance risk beoordeling | Jira filter | Betreffende US bevat een tab “Risks”, hier wordt de zwaarte van het Performance Risk beoordeeld |
| Uitvoeringstijd handmatig logisch testgeval | Jira filter | Betreffende LTC bevat een tab “Main Tab”, hier wordt in het geval van een handmatig logisch testgeval de uitvoeringstijd ingevuld |
| Niet gereviewde user story, Niet goedgekeurde user story | Birt report | Betreffende US bevat een tab “Review”, hier wordt de US Approved na review |
| Niet gereviewd logisch testgeval, Niet goedgekeurd logisch testgeval | Birt report | Betreffende LTC bevat een tab “Review”, hier wordt de LTC Approved na review |
| User story met een onvoldoende aantal logische testgevallen | Birt report | Betreffende US bevat een tab “Review”, hier wordt het aantal Expected number of LTC’s geconfigureerd |
| Nog te automatiseren logisch testgeval | Birt report | Betreffende LTC bevat een tab “Main Tab”, hier wordt Test execution Automated geconfigureerd |
| Uitvoerdatum logisch testgeval | Birt report | Betreffende LTC bevat een tab “Comment” hier wordt iedere Sprint onderstaande als comment toegevoegd: Versie: <versie> Geslaagd: <YYYYMMDD> |
| Handmatig logisch testgeval | Birt report | Betreffende LTC bevat een tab “Main Tab”, hier wordt Test execution Manual geconfigureerd |
