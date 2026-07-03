# Bekende problemen en oplossingen
## De SBoM wordt eenmalig gescand
### Context
Dependency-Track is tool die per project bewaakt welke externe softwarepakketten kwetsbaarheden bevatten.
### Probleem
Na het uploaden van een SBOM verschijnen er resultaten, maar een dag later lijken nieuwe kwetsbaarheden niet automatisch zichtbaar te worden. Het project lijkt daardoor alleen tijdens de eerste upload te zijn geanalyseerd.
 De bedoeling van Dependency-Track is dat een SBoM wordt gemonitord en dus op dagelijkse basis wordt gescand. 

### Waarschijnlijke oorzaken

Mogelijke oorzaken zijn:

* De geplande portfolio vulnerability analysis draait niet.
* De task scheduler is uitgeschakeld of verkeerd geconfigureerd.
* De kwetsbaarheidsbronnen zijn niet ingeschakeld of nog niet gespiegeld.
* Componenten in de SBOM missen bruikbare identifiers, zoals PURL of CPE.
* Een metrics-refresh of grafiekupdate wordt verward met een vulnerability analysis.
* De SBOM bevat wel componentnamen, maar onvoldoende metadata om betrouwbaar te matchen tegen kwetsbaarheidsbronnen.

### Oplossing

Controleer eerst of de geplande analyse actief is.

Voor Dependency-Track v5 zijn met name deze instellingen relevant:

```properties
dt.task-scheduler.enabled=true
dt.task.portfolio-analysis.cron=0 6 * * *
```

De standaardwaarde `0 6 * * *` betekent dat de portfolio vulnerability analysis dagelijks om 06:00 UTC draait.

Controleer daarna of de kwetsbaarheidsbronnen correct zijn ingericht. Ga in Dependency-Track naar:

```text
Administration > Vulnerability Sources
```

Controleer minimaal:

* NVD
* GitHub Advisories
* OSV

Na het inschakelen van een bron moet de eerste mirror uitgevoerd worden. Gebruik daarvoor, indien beschikbaar in de interface:

```text
Mirror now
```

Let daarbij op het type identifier dat per bron nodig is:

| Bron              | Belangrijke identifier |
| ----------------- | ---------------------- |
| NVD               | CPE                    |
| GitHub Advisories | PURL                   |
| OSV               | PURL                   |

Controleer vervolgens de SBOM zelf. Voor open-source dependencies is een Package URL, kortweg PURL, meestal essentieel. Voorbeelden:

```text
pkg:maven/org.apache.commons/commons-lang3@3.14.0
pkg:npm/lodash@4.17.21
pkg:pypi/requests@2.32.3
```

Als de SBOM geen PURL of CPE bevat, kan Dependency-Track de component mogelijk wel tonen, maar kwetsbaarheden minder goed of helemaal niet koppelen.

Let ook op het verschil tussen analyse en metrieken. Een grafiek of dashboardwaarde die wordt bijgewerkt, betekent niet automatisch dat de vulnerabilities opnieuw zijn geanalyseerd. Controleer daarom bij twijfel de Dependency-Track API-serverlogs en de timestamps van de analyse.

### Bronnen

* Dependency-Track v5, Task Scheduler:
  https://dependencytrack.github.io/docs/next/reference/configuration/task-scheduler/
* Dependency-Track v5, Vulnerability Sources:
  https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/
* Dependency-Track v5, Analyzers:
  https://dependencytrack.github.io/docs/next/reference/analyzers/

---



## Geen duidelijk inzicht in gebruikte licenties

### Context

Dependency-Track kan per component licentie-informatie registreren en toetsen. Die informatie komt meestal uit de SBOM. Als de SBOM geen of onvolledige licentiegegevens bevat, kan Dependency-Track deze informatie ook niet betrouwbaar tonen of beoordelen.

Licentie-inzicht bestaat uit twee verschillende vragen:

1. Welke licenties gebruiken wij?
2. Welke gebruikte licenties zijn toegestaan, ongewenst of onbekend?

De eerste vraag is inventariserend. De tweede vraag hoort thuis in beleid, bijvoorbeeld via component policies.

### Probleem

Het projectteam wil inzichtelijk maken welke licenties worden gebruikt in dependencies, maar het overzicht is onvolledig, onduidelijk of niet geschikt voor besluitvorming.

### Waarschijnlijke oorzaken

Mogelijke oorzaken zijn:

* De SBOM-generator neemt geen licentiegegevens op.
* Licenties worden niet als SPDX License Identifier vastgelegd.
* Sommige dependencies hebben geen eenduidige licentie.
* Er is geen licentiebeleid ingericht in Dependency-Track.
* Er zijn geen license groups of component policies geconfigureerd.
* Onbekende licenties worden niet apart bewaakt.

### Oplossing

Begin bij de bron: de SBOM moet licentie-informatie bevatten. Gebruik waar mogelijk SPDX License Identifiers, bijvoorbeeld:

```text
MIT
Apache-2.0
BSD-3-Clause
GPL-3.0-only
LGPL-2.1-or-later
```

Gebruik bij samengestelde of alternatieve licenties een SPDX expression, bijvoorbeeld:

```text
MIT OR Apache-2.0
```

Richt daarna licentiebeleid in Dependency-Track in.

Ga naar:

```text
Policy Management > License Groups
```

Maak bijvoorbeeld deze groepen aan:

| License group        | Doel                                                          |
| -------------------- | ------------------------------------------------------------- |
| Toegestane licenties | Licenties die binnen de organisatie standaard zijn toegestaan |
| Verboden licenties   | Licenties die niet gebruikt mogen worden                      |
| Review vereist       | Licenties die handmatige beoordeling vereisen                 |

Maak vervolgens component policies aan via:

```text
Policy Management > Policies
```

Voorbeelden van bruikbare policies:

### Policy: verboden licenties blokkeren

```text
Subject: LICENSE_GROUP
Operator: IS
Value: Verboden licenties
Violation state: FAIL
```

Gebruik deze policy om componenten te signaleren waarvan de licentie expliciet verboden is.

### Policy: onbekende licenties signaleren

```text
Subject: LICENSE
Operator: IS
Value: unresolved
Violation state: WARN
```

Gebruik deze policy om componenten te signaleren waarvoor Dependency-Track geen licentie heeft kunnen bepalen.

### Policy: alleen toegestane licenties accepteren

```text
Subject: LICENSE_GROUP
Operator: IS_NOT
Value: Toegestane licenties
Violation state: WARN of FAIL
```

Gebruik deze policy wanneer de organisatie werkt met een allowlist. Let op: deze aanpak is strenger dan een denylist. Alles wat niet expliciet is toegestaan, wordt dan gemarkeerd.

Koppel de policies vervolgens aan projecten of projecttags. Gebruik projecttags wanneer hetzelfde beleid voor meerdere projecten geldt.

### Praktisch advies

Gebruik minimaal deze drie categorieën:

1. Toegestaan
2. Verboden
3. Review vereist of onbekend

Zonder categorie voor onbekende licenties ontstaat een blinde vlek. Een dependency zonder licentie-informatie is niet automatisch veilig of toegestaan.

### Bronnen

* Dependency-Track v5, Managing Component Policies:
  https://dependencytrack.github.io/docs/next/guides/user/managing-component-policies/
* Dependency-Track v5, Component Policies Reference:
  https://dependencytrack.github.io/docs/next/reference/policies/component-policies/
* SPDX License List:
  https://spdx.org/licenses/

---

## Het SBOM-formaat wordt niet geaccepteerd

### Context

Dependency-Track v5 ondersteunt CycloneDX als uploadformaat voor SBOM’s. De ondersteunde serialisaties zijn:

| Formaat        | Content type                     |
| -------------- | -------------------------------- |
| CycloneDX JSON | `application/vnd.cyclonedx+json` |
| CycloneDX XML  | `application/vnd.cyclonedx+xml`  |

Dependency-Track v5 ondersteunt alle CycloneDX BOM specification versions voor upload.

### Probleem

Een SBOM wordt niet geaccepteerd door Dependency-Track, of de upload lukt wel maar de inhoud wordt niet goed verwerkt.

### Waarschijnlijke oorzaken

Mogelijke oorzaken zijn:

* De SBOM is geen CycloneDX-document.
* De SBOM is SPDX, Syft JSON, npm audit JSON of een ander formaat.
* De SBOM is CycloneDX, maar ongeldig volgens het CycloneDX-schema.
* De SBOM bevat syntactische fouten.
* De SBOM is geconverteerd, maar tijdens de conversie is informatie verloren gegaan.
* De SBOM bevat onvoldoende metadata, zoals PURL’s of licentiegegevens.

### Oplossing

Genereer bij voorkeur direct een CycloneDX-SBOM vanuit de build of dependency manager van het project. Gebruik dus liever een native CycloneDX-generator dan een conversiestap achteraf.

Voorbeelden van ecosystemen waarvoor CycloneDX-tools bestaan:

| Ecosysteem    | Aanpak                                       |
| ------------- | -------------------------------------------- |
| Maven         | CycloneDX Maven-plugin                       |
| Gradle        | CycloneDX Gradle-plugin                      |
| npm / Node.js | CycloneDX Node.js tooling                    |
| Python        | CycloneDX Python tooling                     |
| .NET          | CycloneDX .NET tooling                       |
| Containers    | Tooling die CycloneDX als output ondersteunt |

Valideer de SBOM voordat deze naar Dependency-Track wordt gestuurd.

Voor CycloneDX JSON:

```bash
cyclonedx validate \
  --input-file bom.json \
  --input-format json \
  --fail-on-errors
```

Voor CycloneDX XML:

```bash
cyclonedx validate \
  --input-file bom.xml \
  --input-format xml \
  --fail-on-errors
```

Gebruik conversie alleen als tijdelijke oplossing. Bijvoorbeeld wanneer een leverancier alleen SPDX JSON aanlevert.

Voorbeeld:

```bash
cyclonedx convert \
  --input-file sbom.spdx.json \
  --input-format spdxjson \
  --output-file bom.json \
  --output-format json \
  --output-version v1_6
```

Valideer daarna altijd het resultaat:

```bash
cyclonedx validate \
  --input-file bom.json \
  --input-format json \
  --fail-on-errors
```

Let op: conversie tussen SBOM-formaten is niet altijd verliesvrij. Controleer na conversie minimaal:

* componentnaam
* versie
* package URL
* licentie
* supplier
* hashes
* dependency-relaties

### Praktisch advies

Gebruik voor Dependency-Track-projecten deze voorkeursvolgorde:

1. Genereer direct CycloneDX vanuit de build.
2. Valideer de CycloneDX-SBOM.
3. Upload de gevalideerde SBOM naar Dependency-Track.
4. Gebruik conversie alleen als fallback.
5. Controleer na conversie of kritieke metadata niet verloren is gegaan.

### Bronnen

* Dependency-Track v5, File Formats:
  https://dependencytrack.github.io/docs/next/reference/file-formats/
* CycloneDX Tool Center:
  https://cyclonedx.org/tool-center/
* CycloneDX CLI:
  https://github.com/CycloneDX/cyclonedx-cli

---

## VDR- en VEX-export uit Dependency-Track

### Context

Dependency-Track kan naast SBOM’s ook CycloneDX-documenten genereren met kwetsbaarheidsinformatie.

Belangrijke termen:

| Term | Betekenis                                 |
| ---- | ----------------------------------------- |
| BOM  | Bill of Materials, de componentinventaris |
| VEX  | Vulnerability Exploitability Exchange     |
| VDR  | Vulnerability Disclosure Report           |

### Toelichting

Een VEX-document beschrijft analysebeslissingen over kwetsbaarheden. Het geeft bijvoorbeeld context over de vraag of een kwetsbaarheid exploiteerbaar is in een specifieke toepassing.

Een VDR-document bevat kwetsbaarheidsinformatie over componenten in een product of project.

Noem een VDR daarom niet simpelweg een “annotated SBOM”. Dat is te onnauwkeurig. Een betere formulering is:

> Een Dependency-Track VDR-export is een CycloneDX Vulnerability Disclosure Report met kwetsbaarheidsinformatie over componenten in het project.

### Bronnen

* Dependency-Track v5, File Formats:
  https://dependencytrack.github.io/docs/next/reference/file-formats/
* CycloneDX, Vulnerability Disclosure Report:
  https://cyclonedx.org/use-cases/vulnerability-disclosure/
* CycloneDX, Vulnerability Exploitability Exchange:
  https://cyclonedx.org/capabilities/vex/

---

## “Refresh requested” bij grafieken of projectmetingen

### Context

Dependency-Track toont projectmetingen en grafieken, maar deze zijn niet hetzelfde als een vulnerability analysis.

### Probleem

Bij een project of grafiek staat dat een refresh is aangevraagd, maar het is niet duidelijk of dit betekent dat kwetsbaarheden opnieuw worden geanalyseerd.

### Uitleg

Behandel een metrics-refresh en een vulnerability analysis als twee verschillende processen.

Een metrics-refresh werkt projectmetingen of grafieken bij. Een vulnerability analysis beoordeelt componenten tegen kwetsbaarheidsbronnen.

Als nieuwe kwetsbaarheden niet zichtbaar worden, controleer dan niet alleen de grafiek of metrics, maar ook:

* of de portfolio vulnerability analysis draait;
* of de vulnerability sources recent zijn gespiegeld;
* of de SBOM bruikbare identifiers bevat;
* of de API-serverlogs analyseactiviteit tonen.

### Bronnen

* Dependency-Track v5, Task Scheduler:
  https://dependencytrack.github.io/docs/next/reference/configuration/task-scheduler/
