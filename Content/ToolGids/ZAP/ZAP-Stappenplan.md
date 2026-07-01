# ZAP Stappenplan ZAP-script maken

## Samengevat
- ZAP kun je gebruiken voor een actieve aanval (ad hoc) of geautomatiseerd middels een automation plan (zie [Gids Automation Plan]). Dit is verder uitgelegd in [[ZAP - Verdieping en begrippen]].
- In dit stappenplan wordt eerst en context gemaakt. Dit is een verzameling URL's die later wordt kan gebruikt worden voor beide typen gebruikswijzen (ad hoc of geautomatiseerd).
- We voegen deze context toe aan een automation plan zodat dit later in een CI/CD-pipeline kan worden uitgevoerd.
- Als laatste stap kan er een ZEST script worden toegevoegd aan het automation plan om daadwerkelijk stappen te doorlopen die later ook in die volgorde worden uitgevoerd.

In dit stappenplan wordt de Desktop-applicatie gebruikt. 
Volg deze instructies om ZAP te downloaden en te installeren: [Download ZAP en installeer ZAP](#download-en-installatie-voor-desktop)

## Stap 1 — Een opname maken
Om het verkeer op te nemen wordt geadviseerd om de geïntegreerde browser van ZAP (zie screenshot) te gebruiken omdat die vooringesteld is. 

> ⚠️ **Let op:** Dit is geen opname waarbij de stappen op volgorde kunnen worden afgespeeld. Dit registreert alleen alle calls/endpoints.

Als doelwit/testobject kun je gebruik maken van onderstaande testwebsites.
- https://juice-shop.herokuapp.com/#/
- https://demo.owasp-juice.shop/
- https://demo.weblock.ru
- http://testphp.vulnweb.com/
- of kies hier een site: https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/

Wanneer je dit ziet is het goed
![Screenshot van Browser](ToolGids/Images/Pasted image 20251003105810.png " ")

Als je dan naar de pagina gaat moeten er in de zijbalk van ZAP Sites te voorschijn komen. Dit is de opname.
![Screenshot van ZAP met zijbalk](ToolGids/Images/Pasted image 20251003105944.png " ")

- Gebruik de geïntegreerde browser van de ZAP GUI of;
- Zet je browser (Firefox/Chromium) op `http://localhost:8090`. 
- Bezoek de webapplicatie of webpagina → requests verschijnen in **History**.  
- ZAP functioneert als **MITM-proxy**: alle verkeer wordt zichtbaar en kan later opnieuw worden afgespeeld.  
![Geïntegreerde ZAP-Browser](ToolGids/Images/ZAP_Browser.png "De browser die geïntegreerde is in ZAP en standaard via de proxy loopt")
*De browser die geïntegreerde is in ZAP en standaard via de proxy loopt.*

> [!WARNING]
> Wanneer je de melding krijgt: bla bla
> ⚠️ Wanneer je de melding krijgt: `PR_CONNECT_RESET_ERROR` of `Kan geen verbinding maken`  

## Stap 2 — Een context maken

Een context wordt gebruikt om de scope te bepalen van een scan/test. Het is het beste om dit te doen per webapplicatie die je wil scannen/testen/aanvallen. Een context zorgt ervoor dat ZAP de *niet* relevante endpoints *niet* meeneemt in een scan/test/aanval. De meeste webpagina's maken namelijk ook allerlei aanroepen naar websites die niet getest/aangevallen moeten worden met ZAP, zoals bv een aanroep naar Google o.i.d.).

Deze stap (een context maken) kun je ook voorafgaand aan de opname doen (dan werkt het als een include/exclude). Toch adviseren wij om dit als tweede stap te doen omdat je niet altijd weet welke calls je webapplicatie maakt en welke calls je daarvan wil behouden. Er is dan eerst een (grote) lijst met URL's van de endpoints als resultaat van de opname. Hierna kan een selectie worden gemaakt tussen wat *wel* moet worden behouden en wat *niet*.

> Meer info hierover is te lezen op.
> https://www.zaproxy.org/docs/desktop/start/features/contexts/

- Rechtsklik op de site in **Sites** → *Include in Context → New Context*.  
- Definieer:
  - **IncludePaths / ExcludePaths** (regex ondersteund)  
  - (Optioneel) **Authentication** + **Users** + **Session Management**  
- Test je instellingen met de **Authentication Tester**.  
![Context_Aanmaken](ToolGids/Images/Context_aanmaken.png "Hier maak je de context aan, dit is de centrale configuratie die ZAP vertelt wat er bij een applicatie hoort en hoe deze werkt.")
*Hier maak je de context aan, dit is de centrale configuratie die ZAP vertelt wat er bij een applicatie hoort en hoe deze werkt.*



## Stap 4 — Verkennen (passive scan)
ZAP kent verschillende soorten *'scans'* als stappen. De 'passive scans' zijn stappen waarin ZAP fungeert als crawler/spider. De tool gaat op de pagina op zoek naar hyperlinks en calls en verzamelt deze en volgt de links ook. Op de gevonden andere pagina's doet hij hetzelfde, enzovoorts.

Het voordeel van deze passive scan is dat er een lijst wordt opgebouwd van endpoints buiten het opgenomen klikpad die later weer kunnen worden gescand/getest/aangevallen. 

je kunt 
ad hoc scannen
- ter orientatie
- en/of resultaten verwerken in een context

passive scan kan ook onderdeel zijn van een automation plan, maar dan moet je eerst een plan maken en daarna de passive scan toevoegen


- **Spider**: ontdekt links op basis van HTML-structuur.  
- **Ajax Spider**: gebruikt een echte browser en is geschikt voor SPA’s (React/Angular/Vue).  
- **OpenAPI import**: laad je API-spec om endpoints in scope te krijgen.

WAAROM
zodat je ook andere links (buiten je opname klikpad) kunt ontdekken, die later kunnen worden aangevallen
alle endpoints in kaart brengen
- context uitbreiden om later aan te vallen

HOE

## Stap 5 — Actieve scan

Je kunt nu een actieve scan doen ingeval je een ad hoc test zou willen doen.
Voor deze 

- Rechtsklik op een context of node → *Attack → Active Scan*.  
- Kies **scan-policy** en stel **limieten** in:  
  - `maxScanDurationInMins`  
  - `maxRuleDurationInMins`  
  - `threadsPerHost`  

## Stap 6 — Rapportage
- *Report → Generate Report* → kies `traditional-html` en/of `traditional-xml`.  


## Stap 7 — Automation Plan genereren
- Open het tabblad **Automation** → *Generate Plan* → exporteer als `af-plan.yaml`.  
- Headless uitvoeren:
```bash
zap.sh -cmd -autorun /zap/wd/af-plan.yaml
```
![Automation Panel](ToolGids/Images/Automation_Panel.png "Het Automation Panel waar je gemaakte automation plans kan inzien en exporteren")
*Het Automation Panel waar je gemaakte automation plans kan inzien en exporteren.*



⚠️ **Belangrijk**: stel **exit-criteria** in (via `exitStatus` job) om te voorkomen dat scans onbeperkt draaien of CI/CD altijd slaagt.
