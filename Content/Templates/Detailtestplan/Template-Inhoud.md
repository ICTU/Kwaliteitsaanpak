# Testaanpak

Dit hoofdstuk beschrijft hoe de testen conform de teststrategie, beschreven in het Mastertestplan, concreet worden aangepakt.

{De Kwaliteitsaanpak schrijft voor dat er in de voorfase een Mastertestplan (door de opdrachtgever) is opgesteld. Mocht deze niet zijn opgesteld, dan zal dit detailtestplan minimaal aan de door ICTU gestelde kwaliteitseisen moeten voldoen.}

## Soorten testen

{Geef hieronder alleen de testsoorten weer die door het project worden uitgevoerd. Zie het kwaliteitsplan voor normen wat betreft de dekking van de verschillende testsoorten.}

Binnen het project worden door ICTU de volgende testsoorten onderscheiden en toegepast:

* Unit testen: De unit testen (op code) worden uitgevoerd door de ontwikkelaars.

* Functionele testen:
    + **Smoke test:** Dit is een snelle geautomatiseerde test met weinig diepgang. Deze test wordt uitgevoerd om een build te valideren. Fouten tijdens deze test worden aangemerkt als bouwfouten.
    + **Geautomatiseerde regressietest (ART):** Dit is een uitputtende geautomatiseerde test die aantoont dat de bestaande, niet aangepaste functionaliteit nog steeds juist werkt.
    + **Handmatig testen van nieuwe functionaliteit:** Het handmatig uitvoeren van fysieke testgevallen om de werking van de nieuwgebouwde functionaliteit te testen.
    + **Handmatig regressietesten:** Het handmatig uitvoeren van fysieke testgevallen om de werking van de bestaande functionaliteit te controleren. Deze testgevallen zijn veelal te complex om te automatiseren.

* Niet-functionele testen:
    + **Performancetesten:** Het testen van de snelheid van afhandeling van bepaalde functies van het systeem onder een vooraf gedefinieerde belasting. Performancetesten vinden bij voorkeur plaats in een productie-like omgeving, maar kunnen ook in een niet-productie-like omgeving plaatsvinden ten behoeve van het volgen van de relatieve performance van verschillende versies van de software. Er vinden zowel een loadtest (normale en piekbelasting), als een duurtest (normale belasting voor langere tijd), als een stresstest (verhogen van de belasting totdat het systeem het begeeft) plaats. De Kwaliteitsaanpak schrijft voor dat er tijdens de realisatiefase performancetesten worden uitgevoerd. Deze worden bij voorkeur automatisch gegenereerd. Belangrijk is dat de performancetest die op de testomgeving wordt uitgevoerd, niet vanzelfsprekend representatief is voor de productieomgeving. Dit betekent dat een opdrachtgever op de eigen productieomgeving een performancetest moet uitvoeren om te controleren dat er aan de gestelde performance-eisen is voldaan.
    + **Securitytesten:** Security- en penetratietesten uitgevoerd door een externe partij. Normaliter worden deze minimaal twee maal per jaar of met elke grote release uitgevoerd en niet elke sprint. Securitytesten vinden bij voorkeur plaats in een productie-like omgeving, maar kunnen ook in een niet-productie-like omgeving plaatsvinden ten behoeve van het testen van de beveiliging van de software zelf. De securitytest is inclusief een review van de broncode. Tijdens de realisatie draaien standaard al de volgende securitytesttools mee in de geautomatiseerde pijplijn: Checkmarx, OWASP dependency checker, OWASP ZAP en OpenVAS; de bevindingen die uit deze tools komen worden meteen tijdens de realisatie van het systeem opgepakt.

* **Integratietesten:** Tijdens deze test wordt de onderlinge verwerkingswijze tussen de verschillende applicaties getest. Denk hierbij aan gewijzigde applicaties die samen werken met ongewijzigde applicaties. Indien van toepassing zullen hier ook externe systemen bij betrokken worden, in de vorm van stubs. Integratietesten zijn normaal gesproken geautomatiseerde tests. Als onderdeel van de integratietesten wordt getest of de software kan omgaan met fouten in andere applicaties en na een herstart goed blijft functioneren.

* **Gebruikersacceptatietest (GAT):** In tegenstelling tot de ‘traditionele’ watervalmethode biedt agile ontwikkelen meer ruimte voor de gebruiker om te participeren in het ontwikkeltraject. Tijdens elke sprint wordt nieuwe functionaliteit gedemonstreerd op de GAT-testomgeving waar gebruikers kunnen werken met de nieuwe applicaties. Bevindingen worden tijdens workshops verzameld om in de backlogs verwerkt te worden. De product owner prioriteert vervolgens deze bevindingen.

* **Usabilitytesten:** Het doel van deze test is om te bepalen hoe gemakkelijk / toegankelijk het systeem is in het gebruik ervan. Onderdeel van deze test is de toegankelijkheidstest; hiermee wordt bepaald in welke mate de software voldoet aan de wettelijke vereisten van de Web Content Accessibility Guidelines (WCAG2.1) en eventuele aanvullende toegankelijkheidseisen. Deze toegankelijkheidstesten worden waar mogelijk geautomatiseerd uitgevoerd. De toegankelijkheidseisen die niet geautomatiseerd getest kunnen worden, worden periodiek handmatig getest.

## Agile werkwijze

Het team zal volgens de Scrummethode werken. Dat betekent dat de expertise van de diverse componenten in het landschap bij elkaar in één team zit en dat het testen van de gerealiseerde oplossing in principe tijdens de sprint plaatsvindt.

{Mogelijke uitzonderingen hierop zijn de securitytest, Migratietest (MT), performancetest en Product Acceptatie Test (PAT). Deze behoren niet vanzelfsprekend tot de vaste sprintactiviteiten.}

## Testactiviteiten tijdens sprints

Deze paragraaf beschrijft de testactiviteiten die plaatsvinden binnen de grenzen van een sprint. De testengineers nemen actief deel aan de sprintplanning. De stappen voor het testen van een user story zijn als volgt:

1. Ontwikkelen testgevallen in Jira, gebaseerd op user story
    a. Logische testgevallen laten reviewen door teamgenoot;
    b. Reviewcommentaar verwerken.
2. Logische testgevallen uitwerken in fysieke testgevallen
    a. Handmatig uitvoeren op de testomgeving;
    b. Alle voorkomende issues direct oplossen.
3. ART uitvoeren
    a. Alle voorkomende regressie direct oplossen.
4. Na uitvoer fysieke testgevallen en oplossen issues de testgevallen opnemen in de ART.
5. Vaststellen van ART
    a. De laatste nieuwe versie van de ART uitvoeren op de regressie- en de integratietestomgeving;
    b. Eventuele bevindingen en issues dienen direct te worden opgelost en te worden gevolgd door het opnieuw uitvoeren van de ART.

## Entry- en exitcriteria

Dit hoofdstuk beschrijft wat nodig is om te kunnen testen en wanneer er voldoende getest is.

### Entry-criteria

{Benoem hier de criteria waaraan voldaan moet worden voordat het testen kan starten. Voorbeelden: "De testomgeving(en) zijn beschikbaar en ingericht conform de gestelde eisen van de tester" en "Het systeem met omgeving is met goed gevolg door de intake gekomen".}

### Exitcriteria

Aan het eind van de sprint zal er alleen functionaliteit overgedragen worden die voldoet aan de Definition of Done (zie Kwaliteitsplan).

{Benoem hier eventuele specifieke zaken die gerelateerd zijn aan het testen en niet al onderdeel uitmaken van de Definition of Done.}

# Infrastructuur

## Testomgevingen

{Neem hieronder alleen testomgevingen op die voor het project van toepassing zijn.}

Conform BIO-12.1.4 zijn productieomgevingen gescheiden van testomgevingen en wordt er niet getest in productieomgevingen. De onderstaande testomgevingen zijn inzetbaar voor het project:

* **Ontwikkelomgeving:** Op deze omgeving wordt de smoketest uitgevoerd;
* **Testomgeving:** Handmatig testen van nieuwe functionaliteit en het automatiseren van handmatig uitgevoerde testen om op te nemen in de ART;
* **Regressietestomgeving:** ART uitvoeren op omgeving met functionaliteit, zoals meest recent vrijgegeven;
* **Integratietestomgeving:** Alle laatste versies zijn hier uitgerold op een omgeving waar gebruik wordt gemaakt van productie-like data;
* **Performancetestomgeving:** Omgeving gebruikt voor performancetesten;
* **Securitytestomgeving:** Gebruikt voor security- en penetratietesten;
* **Middleware-omgevingen:** Deze testomgevingen worden gebruikt om besturingssystemen, databases, patches en andere 3rd party componenten te testen voor uitrol naar productie;
* **GAT-omgeving:** Op deze omgeving worden de gebruikersacceptatietesten uitgevoerd, inclusief usabilitytestsen.

ICTU beschikt over een private cloud waarin deze omgevingen allemaal kunnen worden ingericht. In welke mate dit productie-like kan, is afhankelijk van de karakteristieken van de productie-omgeving en het beschikbare budget.

## Testtools

{Geef alleen de tools weer die voor het project van toepassing zijn en vul aan waar nodig.}

Tijdens het testen worden de onderstaande tools gebruikt:

* **Axe:** Axe is een testtool voor de Web Content Accessibility Guidelines.
* **Selenium:** Web UI driver library, wordt gebruikt om de browser aan te sturen vanuit de ART.
* **Jenkins:** Jenkins is een Continuous Integration (CI) server die wordt gebruikt om de ART uit te voeren.
* **BIRT:** Een rapportagetool waarmee kwaliteits- en managementrapportages gegenereerd worden.
* {Andere tools}

## Testdata

Conform BIO-14.3 wordt er niet met productiedata getest. In de ontwikkel-, test- en regressietestomgevingen wordt nagemaakte testdata gebruikt. In de integratie- en performanceomgevingen wordt gegenereerde testdata of eventueel geanonimiseerde productiedata gebruikt. Deze richtlijnen zijn bedoeld om privacy te waarborgen.

Er worden drie soorten data onderscheiden:

* **Statische data:** Dit is data die noodzakelijk is voor het correct functioneren van de applicatie. Denk hierbij aan systeemlocaties, certificaten, etc.;
* **Dynamische data:** Dit is data die voortkomt uit de interactie tussen gebruiker en systemen (applicaties);
* **Testgegevens:** Deze data wordt gebruikt om de test correct uit te kunnen voeren en wordt gecreëerd aan het begin van een testscript. Na het uitvoeren van de test wordt deze data weer verwijderd.

{Neem hier eventuele bijzonderheden op over testdata in het project.}

# Rapportages en testartifacten

Dit hoofdstuk beschrijft de testrapportages en andere testartifaction die het project oplevert.

## Interne testrapportages

{Benoem hier de interne testrapportages die voor het project van toepassing zijn.}

De resultaten van de testuitvoer worden gedeeld met de projectleider in de vorm van de volgende interne testrapportages:

* **ART-resultaten:** Zichtbaar in Jenkins als resultaat van de Jenkins job. BIRT-resultaten worden automatisch gegenereerd, hierin is een gedetailleerd overzicht van de testruns, logische testgevallen, testklassen en testmethodes zichtbaar.
* **Performancetestrapport:** Op wekelijkse basis, met hierin een overzicht van de testresultaten van de performancetest, de performancetrend, een analyse en eventueel advies.
* **Securitytestrapport:** De securitytesten worden uitgevoerd door een gespecialiseerde organisatie. Deze organisatie stelt ook het securityeindrapport op. Hierin staat een overzicht van de kwetsbaarheden die zijn ontdekt tijdens het testen, en een advies hoe deze te aan te pakken.
* **Toegankelijkheidstestrapport:** In dit rapport is vastgelegd in welke mate de software aan de toegankelijkheidseisen voldoet, waaronder de wettelijk verplichte Web Content Accessibility Guidelines.

## Externe testrapportages

{Benoem hier de externe testrapportages die voor het project van toepassing zijn.}

De volgende externe testrapportages zijn onderdeel van elke release:

* **Eindrapport functionele testen:**
  + Opsomming van de user stories per product,
  + Gerelateerde logische testgevallen,
  + Reviewstatus van de logische testgevallen,
  + Of de testgevallen zijn geautomatiseerd,
  + Wat het resultaat van de test was (geslaagd/gefaald/overgeslagen).
* **Performancetestrapport:** Een overzicht van de testresultaten van de performancetest, de performancetrend, een analyse en eventueel advies.
* **Securitytestrapport:** De securitytesten worden uitgevoerd door een gespecialiseerde organisatie. Deze organisatie stelt ook het securityeindrapport op. Hierin staat een overzicht van de kwetsbaarheden die zijn ontdekt tijdens het testen, en een advies hoe deze te aan te pakken.
* **Toegankelijkheidstestrapport:** In dit rapport is vastgelegd in welke mate de software aan de toegankelijkheidseisen voldoet, waaronder de wettelijk verplichte Web Content Accessibility Guidelines.

## Bevindingenprocedure

{Beschrijf de bevindingenprocedure, zoals die voor het project geldt.}

## Testartifacten

{Benoem hier de testartifacten die voor het project van toepassing zijn.}

De volgende testartifacten worden bij een release opgeleverd:

* Broncode van de ART,
* Performance testrapportage,
* Security testrapportage,
* Toegankelijkheidstestrapport,
* Eind(test)rapport,
* Kwaliteitsrapport,
* Vrijgaveadvies.
