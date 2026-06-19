# ZAP Verdieping en Begrippen
## ZAP algemeen

ZAP is een open source tool die fungeert als een kleine, geautomatiseerde penetratietest in de pipeline. Het is een tool die, net als bij testautomatiseringsscripts, een serie acties uitvoert op de system-onder-test (SUT) om te onderzoeken of deze applicatie beveiligingskwetsbaarheden heeft. Het is niet representatief voor een echte penetratietest, maar dit kan wel een goede voorbereiding zijn. 
ZAP is bedoeld voor zowel mensen die geen specialist zijn op het gebied van applicatiebeveiliging, die een beveiligingsscan aan de pipeline willen toevoegen, als professionele penetratietesters die ter plekke een eerste analyse willen doen. 
ZAP staat voor Zed Attack Proxy en werkt dus als een proxy, een tussenlaag. Het opereert, net als een man-in-the-middel-aanval (MITM), tussen de browser en het testobject (SUT). 

ZAP kan geconfigureerd worden om een stappenplan (in ZAP heet dit een [Automation plan](#Automation-plan)) uit te voeren vanuit de CI/CD-pijplijn. Dit plan kan onderstaande acties uitvoeren.
- Vooraf gedefinieerde acties uit met behulp van een Zest-script.
- De API van de applicatie scannen met behulp van de OpenAPI-specificaties.
- Een spiderscan uitvoeren om alle blootgestelde bronnen te ontdekken.
- Actieve en passieve beveiligingsscans uitvoeren op de API en de bronnen die zijn ontdekt tijdens de spiderscan.
- Rapporten genereren in zowel computer leesbare (XML) als menselijk leesbare (HTML) formaten, zodat deze toegankelijk zijn in Quality-time.
### Geschiedenis en achtergrond
ZAP is ontstaan als een fork van Paros Proxy en is sinds 2010 uitgegroeid tot een van de meest gebruikte open source webapplicatie securityscanners. Het is vooral populair onder QA-engineers, ethical hackers en DevOps-teams vanwege de combinatie van open source en uitgebreide functionaliteit.
Meer info: [zie de Wikipedia-pagina van ZAP](https://en.wikipedia.org/wiki/ZAP_(software))

### Belangrijkste kenmerken
- Ondersteuning voor zowel handmatige als geautomatiseerde security tests
- Passieve en actieve scans op webapplicaties
- Integratie met CI/CD (bijv. Jenkins, GitHub Actions)
- REST API voor scripting en externe aansturing
- Plug-in-architectuur met uitbreidingen voor o.a. Selenium, HUD, Docker
## ZAP-client
De ZAP-client wordt gebruikt voor ad hoc onderzoeken en het maken van testautomatisering (automation plan) die later gebruikt kan worden in een pipeline. Deze standalone applicatie heeft een zeer steile leercurve en werkt niet intuïtief. Dit is de aanleiding om deze wiki op te zetten. 
Meer info $LINK.ZAP.INSTALLATIE$
## Automation plan

❌ hier noemen dat Automation plan een grote ontwikkeling is geweest en dat ICTU projecten moeten wijzigen

Het automatiseren van ZAP kan het best gedaan worden met een zogenaamd automation plan. Dit is een **.yaml-script** dat je kan uitvoeren in je pipeline. Door het gebruiken van een automation plan kun je ook rapportages genereren.

Een automation plan bevat omgevingsvariabelen (`env`) en taken (`jobs`). De jobs zijn de afzonderlijke stappen die uitgevoerd worden. Een script job importeert een scriptbestand, bijvoorbeeld om een locatie of configuratiebestand in te laden.

Onderstaande onderdelen zitten doorgaans in een automation plan.
- De application context (URL's, authentication, session management)
- Verschillende scan jobs (passive scan, script execution, OpenAPI scanning, spider scanning, etc.)
- Instellingen voor report generation

Voor meer info, zie:[Gids Automation Plan]

## Acties / jobs
ZAP kent meerdere acties (vaak scans genoemd), de belangrijkste zijn: passive scan en active scan. Waarbij de eerste een onderzoek is om te kijken welke URL's en links er te vinden zijn en de tweede is meer een aanval op die URL's. Active scan is dus een verwarrende naamgeving.

- OpenAPI - scant OpenAPI-specificaties (net zoals Swagger dit doet)
- spider
- [AJAX](https://nl.wikipedia.org/wiki/Asynchronous_JavaScript_and_XML) spider
- sequence. active scan = uitvoer van het ZEST script ❌ dit moet beter worden verwoord, hoe staat een sequence in relatie met een active scan?
## Omgevingsvariabelen in ZAP

Binnen het **ZAP Automation Framework** kun je gebruikmaken van omgevingsvariabelen om je automation plannen flexibeler en herbruikbaar te maken. Deze variabelen worden gedefinieerd in het `env:`-gedeelte van je YAML-configuratie.
#### Gebruik

Omgevingsvariabelen worden ingesteld in het `parameters`-veld van de `env`-sectie, bijvoorbeeld:

```yaml
env:
  parameters:
    release_name: "v1.2.3"
    base_url: "https://test.example.org"


# Zest - ZAP's eigen automation
## Wat is ZEST?

**Zest** is een scripttaal ontwikkeld door Mozilla, specifiek voor security testing. Het is ontworpen om eenvoudig leesbare en herbruikbare scripts te maken die het gedrag van een gebruiker of aanvaller simuleren binnen ZAP.

Zest-scripts zijn:
- **Menselijk leesbaar** en gebaseerd op JSON-structuur
- **Herhaalbaar** en dus goed inzetbaar voor regressietests
- **Geïntegreerd** met ZAP: je kunt ze opnemen in automation plans, aanpassen via de ZAP-GUI en uitvoeren als onderdeel van scans

Zest wordt vaak gebruikt voor:
- Het automatisch uitvoeren van testscenario’s
- Het aanroepen van specifieke URL's met aangepaste headers of cookies
- Het controleren van verwachte responses en statuscodes
- Het vastleggen van testlogica op een declaratieve manier

Zest ondersteunt conditionele logica (zoals if-statements), logging, loops, en integratie met andere ZAP-functies zoals scan rules en contexten.

Meer informatie: [Officiële bronnen](ZAP%20-%20Referentiemateriaal-(Informatie).md#Officiële%20bronnen)
```

Deze variabelen kun je vervolgens gebruiken in andere delen van het plan via `${variabelenaam}`:

```yaml
jobs:
  - type: passiveScan-config
  - type: requestor
    parameters:
      requests:
        - url: "${base_url}/login"

```

#### Belangrijk om te weten

- Variabelen worden **alleen vervangen** op plekken waar ZAP dit expliciet ondersteunt, zoals bij `url`, `name`, `includedPaths` en andere parameterwaarden.
    
- In velden waar variabelen niet automatisch worden geïnterpreteerd (zoals binnen bepaalde scripts), moet je dit handmatig oplossen.
    
- De interpolatie gebeurt **eenmalig** bij het laden van het automation-plan; dynamische aanpassing tijdens runtime is niet mogelijk.

Meer informatie: [Officiële bronnen]

## Zest - ZAP's eigen automation
### Wat is ZEST?

**Zest** is een scripttaal ontwikkeld door Mozilla, specifiek voor security testing. Het is ontworpen om eenvoudig leesbare en herbruikbare scripts te maken die het gedrag van een gebruiker of aanvaller simuleren binnen ZAP. De doorontwikkeling van Zest wordt momenteel gedaan in de ZAP-repo en inmiddels niet meer in de repo van Mozilla.

Zest-scripts zijn:
- **Menselijk leesbaar** en gebaseerd op JSON-structuur
- **Herhaalbaar** en dus goed inzetbaar voor regressietests
- **Geïntegreerd** met ZAP: je kunt ze opnemen in automation plans, aanpassen via de ZAP-GUI en uitvoeren als onderdeel van scans

Zest wordt vaak gebruikt voor:
- Het automatisch uitvoeren van testscenario’s
- Het aanroepen van specifieke URL's met aangepaste headers of cookies
- Het controleren van verwachte responses en statuscodes
- Het vastleggen van testlogica op een declaratieve manier

Zest ondersteunt conditionele logica (zoals if-statements), logging, loops, en integratie met andere ZAP-functies zoals scan rules en contexten.

Meer informatie: [Officiële bronnen]


### Reference — Syntax, jobs en begrippen

#### Belangrijke jobs
- **OpenAPI**: laadt de API-specificatie  
- **spider / ajaxSpider**: verken endpoints  
- **activeScan / activeScan-config**: actieve aanvalsscan  
- **script (Zest)**: sequences of custom logic  
- **report**: output in html/xml/sarif  
- **exitStatus**: quality gate  

#### Variabelen
```yaml
env:
  parameters:
    base_url: "https://test.example.org"
    release_name: "v1.2.3"
```
Gebruik als `${variabelenaam}` in jobs.

#### Context-management
- Context in GUI ≠ Context in Automation Plan (kopie!).  
- Synchroniseer handmatig of genereer plan opnieuw na wijzigingen.  

---

### Explanation — Concepten & best practices

- **ZAP is geen vervanging van een pentest (penetratietest)**, maar biedt een **shift-left security check op een draaiende (runtime) applicatie.**.  
- **Proxy-model**: inzicht in al het verkeer; History is fantastisch voor het bouwen van flows.  
- **Passive vs Active scan**: passief = observeren, actief = muteren en aanvallen.  
- **Sequences**: onmisbaar voor flows met login of state.  
- **Authenticatie**: integreer altijd in context; voorkom false negatives.  
- **Exit-criteria**: altijd tijds- en regellimieten instellen; zo blijft CI voorspelbaar.  
- **Rapportage**: HTML voor menselijk lezen, XML/SARIF voor dashboards en quality tooling.  

---


#### C. Authenticatie
- **Form-based**: configureer context (login URL, users, logged-in regex).  
- **Tokens (header/bearer)**: gebruik **Replacer** of **HTTP Sender** script.  
- **OIDC/JWT**: vaak herbruikbaar, maar hou rekening met expiratie en refresh.  
- **SAML**: tokens zijn niet herbruikbaar → elke run opnieuw ophalen (via sequence of regex **Moet nog uitgewerkt worden in tutorial**). ❌  

---

#### D. Referentie-YAML-bestand

```yaml annotate
env:
  contexts:
    - name: "ICTU-Test"
      urls:
        - "http://testphp.vulnweb.com"
      includePaths:
        - "http://testphp.vulnweb.com.*"
      authentication:
        method: "form"
        parameters:
          loginUrl: "http://testphp.vulnweb.com/login.php"
          loginRequestBody: "uname={%username%}&pass={%password%}&login=login"
        verification:
          loggedInRegex: "Logout"
          loggedOutRegex: "Login"
      sessionManagement:
        method: "cookie"
      users:
        - name: "demo-user"
          credentials:
            username: "test"
            password: "test"

jobs:
  - type: passiveScan-config
    parameters:
      maxAlertsPerRule: 0

  - type: spider
    parameters:
      context: "ICTU-Test"
      user: "demo-user"
      maxDuration: 2

  - type: ajaxSpider
    parameters:
      context: "ICTU-Test"
      user: "demo-user"
      maxDuration: 2

  - type: activeScan
    parameters:
      context: "ICTU-Test"
      user: "demo-user"
      policy: "Default Policy"
      maxRuleDurationInMins: 2

  - type: report
    parameters:
      template: "traditional-html"
      reportDir: "./zap-reports"
      reportFile: "ictu-zap-report.html"

   - type: exitStatus
    parameters:
      warnLevel: Low
      errorLevel: Medium
```
