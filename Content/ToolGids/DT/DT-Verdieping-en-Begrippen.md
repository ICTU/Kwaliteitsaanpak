# Dependency-Track Verdieping en Begrippen
## Dependency-Track algemeen
Dependency-Track is een open-source tool die de softwarecompositie analyseert van softwareontwikkelprojecten. Het inventariseert projecten en scant de componenten periodiek op kwetsbaarheden.
Dependency-Track is een applicatie die los staat van je pipeline en SBoM ontvangt en de securitydatabase periodiek bevraagd om te bepalen of de softwarecomponenten in uit de SBoM kwetsbaarheden bevat. In een SBoM kunnen zowel container images als softwarebibliotheken worden opgenomen. Ook al lijken de namen sterk op elkaar, deze tool moet niet verward worden met de onderstaande. Ze hebben overlap maar ook verschillen.

## Geschiedenis en achtergrond
Dependency-Track is een OWASP-project bedacht door Steve Springett. Volgens de OWASP-projectpagina bestaat Dependency-Track sinds 2013 en is het ontwikkeld om Bill of Materials te analyseren voor cybersecurity-risico’s.

Dependency-Track is een OWASP Flagship Project en wordt ontwikkeld door een internationale groep vrijwilligers. De software valt onder de Apache 2.0-licentie.

Dependency-Track is nauw verbonden met CycloneDX. CycloneDX is een standaard voor Bills of Materials en wordt eveneens binnen de OWASP-context gebruikt. Dependency-Track consumeert en produceert CycloneDX SBOM’s en CycloneDX VEX-documenten.

Bronnen:

https://www.owasp.community/projects/dependency-track
https://owasp.org/www-project-dependency-track/
https://cyclonedx.org/
https://docs.dependencytrack.org/


## Waarvoor gebruik je Dependency-Track?

Dependency-Track wordt vooral gebruikt voor continue software supply chain monitoring.

- inzicht krijgen in gebruikte softwarecomponenten;
- kwetsbare componenten vinden;
- bepalen welke projecten geraakt worden door een specifieke kwetsbaarheid;
- licentierisico’s zichtbaar maken;
- policies afdwingen op security, licenties en operationele risico’s;
- auditbeslissingen vastleggen over kwetsbaarheden;
- SBOM’s en VEX-informatie gebruiken in beheer, releaseprocessen en leveranciersmanagement.

Dependency-Track is vooral nuttig wanneer meerdere applicaties, teams of leveranciers centraal bewaakt moeten worden. Voor één losse build kan een pipeline-scanner voldoende lijken, maar voor portfoliobreed inzicht is een centrale SBOM-gebaseerde applicatie geschikter.

## Wat doet Dependency-Track niet?

Dependency-Track is geen vervanging voor alle securitytesting.

Dependency-Track doet niet automatisch het volgende:

broncode analyseren zoals een SAST-tool;
draaiende applicaties testen zoals een DAST-tool;
containers of images zelf bouwen;
dependencies automatisch updaten;
beoordelen of een kwetsbaarheid daadwerkelijk exploiteerbaar is in de specifieke applicatiecontext;
bepalen of een licentie juridisch acceptabel is voor jouw organisatie.

Dependency-Track levert signalen, bevindingen en beleidsondersteuning. De beoordeling en opvolging blijven onderdeel van het ontwikkel-, beheer- en securityproces.

## Verschil met vergelijkbare tools

Dependency-Track wordt regelmatig verward met andere tools. De namen lijken soms op elkaar, maar het doel verschilt.

Tool of standaard	Wat is het?	Belangrijk verschil
Dependency-Track	Platform voor SBOM-analyse en continue monitoring	Bewaart SBOM’s en monitort projecten centraal over tijd
OWASP Dependency-Check	SCA-tool die projectdependencies onderzoekt op bekende kwetsbaarheden	Draait meestal als CLI, build-plugin of pipeline-stap
CycloneDX	Standaard voor Bills of Materials	Is geen dashboard of vulnerability management platform, maar een formaat en ecosysteem
SBOM-generator	Tool die een SBOM maakt	Genereert input voor Dependency-Track, maar bewaakt de portfolio niet zelf

OWASP Dependency-Check probeert kwetsbaarheden in projectdependencies te detecteren en koppelt dependencies onder meer aan CPE’s en CVE’s. Dependency-Track werkt anders: het gebruikt SBOM’s als centrale input en bewaakt componentgebruik over projecten en versies heen.

Bronnen:

https://owasp.org/www-project-dependency-check/
https://docs.dependencytrack.org/odt-odc-comparison/
https://cyclonedx.org/
Belangrijkste kenmerken

## Dependency-Track heeft onder meer de volgende kenmerken:

open-source;
OWASP Flagship Project;
standalone platform met webinterface en API;
geschikt voor integratie met CI/CD;
gebruikt SBOM’s als centrale bron;
ondersteunt CycloneDX SBOM en CycloneDX VEX;
bewaakt componentgebruik over projecten en versies heen;
ondersteunt componenten zoals libraries, containers, operating systems, firmware, hardware en services;
analyseert bekende kwetsbaarheden;
ondersteunt licentiebeleid;
ondersteunt security-, operational- en license policies;
kan kwetsbaarheidsbronnen zoals NVD, GitHub Advisories en OSV gebruiken;
ondersteunt prioritering met EPSS;
biedt mogelijkheden voor audit, triage en rapportage.

Bronnen:

https://dependencytrack.org/
https://docs.dependencytrack.org/
https://owasp.org/www-project-dependency-track/
https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/

# Begrippen
## SBoM 
SBoM staat voor Software Bill of Materials en is te vergelijken met aan pakbon uit de logistiek. Een SBoM is een overzicht van componenten, bibliotheken en andere softwareonderdelen die in een applicatie of systeem worden gebruikt.

Een goede SBoM bevat bij voorkeur minimaal:

componentnaam;
versie;
leverancier of auteur;
dependency-relaties;
package URL of andere identifier;
licentie-informatie;
hashes;
metadata over de applicatie of het product waarvoor de SBOM is gemaakt.

In de [Kwaliteitsaanpak]($BASE_URL$/$LATEST$/ICTU-Kwaliteitsaanpak.html#m16) is het gebruik van tools en het genereren van een SBoM een maatregel.

⚠️ Let op
Dependency-Track hanteert de naam project voor de verzameling van dezelfde SBoM's die alleen verschillen in versie. 
Dit kan tot verwarring leiden. Je kunt bijvoorbeeld voor iedere release een SBoM genereren van de front-end en de back-end van je project. Dependency-Track ziet dit dan als twee losse 'projects'.

## Project

In Dependency-Track is een project de administratieve eenheid waaronder componenten, versies, bevindingen, policies en metrics worden geregistreerd.

Een project in Dependency-Track is dus niet altijd hetzelfde als een Jira-project, Git-repository of softwareontwikkelproject. In de praktijk komt een Dependency-Track-project vaak overeen met een applicatie, service, component of releasebaar product.

Let op: zeg niet dat Dependency-Track “een SBoM een project noemt”. Nauwkeuriger is:

> Dependency-Track beheert projecten en projectversies. Een SBOM wordt geüpload naar een project of projectversie en beschrijft de componenten daarvan.

Dit onderscheid voorkomt verwarring. Een project kan meerdere versies hebben, en per versie kan een nieuwe SBOM worden aangeleverd.

Bronnen:

https://dependencytrack.org/
https://docs.dependencytrack.org/


## Dependency
Softwareontwikkelprojecten gebruiken extern softwarepakketten (ook wel bibliotheken of libraries) om bepaalde generieke functionaliteit niet zelf te hoeven bouwen, denk bijvoorbeeld aan een log-functionaliteit.
Omdat de software afhankelijk is van deze software worden het, in de context van een softwareontwikkelproject, dependencies genoemd. In Dependency-Track wordt de term component hiervoor gebruikt.

## Directe en transitieve dependencies

Een directe dependency is een dependency die het project zelf expliciet declareert.

Een transitieve dependency is een dependency die indirect wordt binnengehaald door een andere dependency.

Voorbeeld:

```text
Applicatie
└── Library A
    └── Library B
```

In dit voorbeeld gebruikt de applicatie `Library A` direct. `Library B` is transitief, omdat deze via `Library A` wordt meegenomen.

Transitieve dependencies zijn belangrijk, omdat kwetsbaarheden vaak niet in de expliciet gekozen library zitten, maar dieper in de dependency-boom.

---
---

## Component

Een component is een software- of systeemonderdeel dat in een SBOM voorkomt en door Dependency-Track wordt geanalyseerd.

Een component kan bijvoorbeeld zijn:

* een library;
* een framework;
* een container-image;
* een operating system package;
* firmware;
* een bestand;
* een service;
* hardware.

De term component is breder dan dependency. Elke dependency is meestal een component, maar niet elk component hoeft in de klassieke zin een library-dependency te zijn.

Bron:

* https://docs.dependencytrack.org/

---

## CycloneDX

CycloneDX is een Bill of Materials-standaard. Dependency-Track gebruikt CycloneDX als belangrijk formaat voor SBOM’s en VEX-documenten.

CycloneDX ondersteunt meer dan alleen softwarebibliotheken. Het kan ook informatie bevatten over onder meer services, hardware, cryptografie, vulnerabilities en licenties.

Voor Dependency-Track-projecten is CycloneDX het voorkeursformaat voor SBOM’s.

Bronnen:

* https://cyclonedx.org/
* https://dependencytrack.github.io/docs/next/reference/file-formats/
* https://docs.dependencytrack.org/

---

## CVE
Openbare softwarepakketten worden continue onderzocht op kwetsbaarheden in de beveiliging. Deze kwestbaarheden worden [CVE's](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) genoemd. Dit staat voor Common Vulnerabilities and Exposures.
Deze ontdekte kwetsbaarheden worden opgeslagen in databases die kunnen worden geraadpleegd. Zo kunnen softwareontwikkelprojecten weten of de dependencies die gebruikt worden, veilig zijn.

Een CVE krijgt een unieke identifier, bijvoorbeeld:

```text
CVE-2021-44228
```

Dit voorbeeld verwijst naar de bekende Log4Shell-kwetsbaarheid in Apache Log4j.

Een CVE is vooral een gestandaardiseerde verwijzing. De CVE zelf bevat meestal beperkte informatie. Extra details, zoals ernstscore, getroffen versies en verrijkte metadata, komen vaak uit andere bronnen zoals NVD, GitHub Advisories of OSV.

Bronnen:

* https://www.cve.org/
* https://nvd.nist.gov/

---


## NVD

NVD staat voor National Vulnerability Database. Dit is de Amerikaanse overheidsdatabase van NIST voor kwetsbaarheidsmanagementdata.

NVD gebruikt CVE’s als basis en verrijkt die met aanvullende informatie, zoals:

* CVSS-scores;
* CPE-koppelingen;
* impactinformatie;
* referenties;
* metadata over getroffen producten.

Voor Dependency-Track is NVD een belangrijke bron, maar niet de enige bron. Let op dat NVD vooral goed werkt wanneer componenten correct gekoppeld kunnen worden aan CPE’s.

Bronnen:

* https://nvd.nist.gov/
* https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/

---

## GitHub Advisories

GitHub Advisories is een database met security advisories voor open-source dependencies. Deze bron is vooral relevant voor package-ecosystemen zoals Maven, npm, NuGet, PyPI en vergelijkbare repositories.

Dependency-Track kan GitHub Advisories gebruiken als vulnerability source. Voor Dependency-Track v5 is hiervoor een GitHub personal access token nodig. Volgens de officiële documentatie zijn geen scopes nodig, maar de GitHub GraphQL API accepteert geen unauthenticated requests.

Bron:

* https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/

---

## OSV

OSV staat voor Open Source Vulnerabilities. OSV is een kwetsbaarheidsdatabase die zich richt op open-source ecosystemen en package-identifiers zoals PURL.

Dependency-Track kan OSV gebruiken als vulnerability source. In Dependency-Track v5 kan per ecosysteem worden gekozen welke OSV-data gemirrord wordt.

Bronnen:

* https://osv.dev/
* https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/

---

## Vulnerability source

Een vulnerability source is een bron waaruit Dependency-Track kwetsbaarheidsinformatie haalt. Dependency-Track gebruikt die informatie om componenten uit SBOM’s te koppelen aan bekende kwetsbaarheden.

Voor Dependency-Track v5 beschrijft de officiële configuratiedocumentatie drie publieke bronnen die gemirrord kunnen worden:

* NVD;
* GitHub Advisories;
* OSV.

Let op: algemene of oudere Dependency-Track-documentatie noemt soms ook bronnen zoals Sonatype OSS Index, Snyk, Trivy of VulnDB. Controleer altijd de documentatie van de gebruikte Dependency-Track-versie en de actuele configuratie van de eigen omgeving.

Bronnen:

* https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/
* https://docs.dependencytrack.org/

---

## CVSS

CVSS staat voor Common Vulnerability Scoring System. CVSS geeft een numerieke score aan de technische ernst van een kwetsbaarheid. De score loopt van 0,0 tot 10,0 en wordt vaak vertaald naar categorieën zoals low, medium, high en critical.

Belangrijk: CVSS is een maat voor ernst, niet automatisch voor risico. Een kwetsbaarheid met een hoge CVSS-score is technisch ernstig, maar dat betekent niet altijd dat deze in jouw context direct exploiteerbaar is. Omgekeerd kan een kwetsbaarheid met een lagere score toch belangrijk zijn als deze actief wordt misbruikt.

Bronnen:

* https://www.first.org/cvss/
* https://nvd.nist.gov/vuln-metrics/cvss

---

## PURL

PURL staat voor Package-URL. Een PURL is een gestandaardiseerde manier om softwarepackages te identificeren over package-ecosystemen heen.

Voorbeelden:

```text
pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1
pkg:npm/lodash@4.17.21
pkg:pypi/requests@2.32.3
pkg:nuget/Newtonsoft.Json@13.0.3
```

Voor SBOM-gebaseerde analyse is PURL belangrijk, omdat tools zoals Dependency-Track componenten daarmee beter kunnen koppelen aan package-ecosystemen en kwetsbaarheidsbronnen zoals GitHub Advisories en OSV.

Bronnen:

* https://www.packageurl.org/
* https://github.com/package-url/purl-spec
* https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/

---

## Licentie

Een licentie bepaalt onder welke voorwaarden een softwarecomponent gebruikt, verspreid of aangepast mag worden.

Voorbeelden van bekende open-sourcelicenties:

* MIT;
* Apache-2.0;
* BSD-3-Clause;
* GPL-3.0-only;
* LGPL-2.1-or-later.

Dependency-Track kan licentie-informatie uit componenten gebruiken voor licentiebeleid. Het is verstandig om licenties zo veel mogelijk vast te leggen met SPDX License Identifiers.

Bronnen:

* https://spdx.org/licenses/
* https://dependencytrack.github.io/docs/next/guides/user/managing-component-policies/

---

## Policy

Een policy is een regel waarmee Dependency-Track kan bepalen of een component, vulnerability of licentie voldoet aan de afspraken van de organisatie.

Voorbeelden:

* geen componenten met kritieke kwetsbaarheden;
* geen dependencies met verboden licenties;
* onbekende licenties moeten handmatig beoordeeld worden;
* componenten zonder recente release moeten worden onderzocht;
* bepaalde projecten moeten voldoen aan strengere regels.

Policies helpen om afspraken expliciet en toetsbaar te maken. Zonder policies blijft Dependency-Track vooral een signaleringstool. Met policies wordt het ook een governance-instrument.

Bronnen:

* https://dependencytrack.github.io/docs/next/guides/user/managing-component-policies/
* https://dependencytrack.github.io/docs/next/reference/policies/component-policies/

---

## VEX

VEX staat voor Vulnerability Exploitability Exchange. Een VEX-document legt vast of een bekende kwetsbaarheid daadwerkelijk relevant of exploiteerbaar is in een specifieke productcontext.

Een component kan bijvoorbeeld technisch kwetsbaar zijn, maar de kwetsbare functionaliteit wordt niet aangeroepen. In dat geval kan een VEX-status helpen om het verschil vast te leggen tussen:

* kwetsbaar component aanwezig;
* kwetsbaarheid werkelijk exploiteerbaar;
* kwetsbaarheid niet relevant;
* analyse nog niet afgerond.

Bronnen:

* https://cyclonedx.org/capabilities/vex/
* https://docs.dependencytrack.org/

---

## VDR

VDR staat voor Vulnerability Disclosure Report. Een VDR bevat kwetsbaarheidsinformatie over componenten in een product of project.

Noem een VDR niet simpelweg een “annotated SBOM”. Dat is te onnauwkeurig. Een betere formulering is:

> Een VDR is een CycloneDX-document met kwetsbaarheidsinformatie over componenten in een product of project.

Bron:

* https://cyclonedx.org/use-cases/vulnerability-disclosure/
