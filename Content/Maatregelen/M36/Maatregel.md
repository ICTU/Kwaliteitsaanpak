## $M36$

#include "Content/Maatregelen/M36/Definitie.md"

De aanbevelingen gelden voor alle dependencies in de software en de CI-pipeline: directe en indirecte dependencies, inclusief images gebruikt in Dockerfiles, Helm charts, pre-commit hooks en CI-pipeline definities.

### Dependencies toevoegen

Het beheren en bijwerken van een dependency is alleen nodig als die dependency er überhaupt is. De eerste aanbeveling gaat dan ook over het toevoegen van dependencies.

1. [submeasure-title]Controleer voor het toevoegen van een nieuwe dependency of deze wordt onderhouden.[/submeasure-title] Kijk naar licentie, supportopties, community chatter, aantal actieve maintainers, recente releases en releasebeleid (zijn er LTS-releases, hebben major releases een geplande EOL), commitactiviteit, open security issues, open pull requests en eventuele projectarchivering. Als een dependency niet onderhouden lijkt, kies dan een andere dependency, bouw de functionaliteit zelf of kopieer de broncode van de dependency naar een eigen repository ("fork") of in de repository van de eigen software ("vendoring") en onderhoud deze zelf.

### Dependencies specificeren

Doel van de aanbevelingen voor het specificeren van dependencies is om te voorkomen dat er onbedoeld en ongemerkt andere versies van dependencies worden geïnstalleerd dan gedacht. Dit vermindert de kwetsbaarheid voor supply chain attacks en is ook beter voor de herhaalbaarheid van builds.

2. [submeasure-title]Gebruik geen unpinned tags: dus geen `latest` of andere tags die niet naar één versie wijzen, zoals `trixie` of `windows`.[/submeasure-title] Gebruik in plaats daarvan versietags, bijvoorbeeld `13.6.0`, of snapshottags, bijvoorbeeld `trixie-20260713`.
3. [submeasure-title]Pin dependencies met de grootste precisie die mogelijk is: dus `3.14.5` in plaats van `3.14` of `3`.[/submeasure-title] Gebruik dus ook geen versierange, zoals `requests>=2.34`, tenzij de software een library is.
4. [submeasure-title]Pin dependencies met hashes (digests, commit SHA, integrity hashes) waar mogelijk.[/submeasure-title] Package managers doen dit veelal zelf met een lockfile. Plaats in dat geval de lockfile onder versiebeheer en gebruik deze om dependencies te installeren zonder ook te updaten (bijvoorbeeld `npm ci` of `uv sync --locked` in build pipelines). Gebruik voor dependencies zonder package manager een tool als Renovate, Dependabot of Update-time. Het registeren van zowel een versie als een hash (`actions/checkout@3d3c42...ba90b1 # v7.0.1`) lijkt wellicht dubbele administratie, maar aan de hash pin is niet eenvoudig te zien welke versie gebruikt wordt en tools kunnen veelal beiden tegelijk bijwerken.
5. [submeasure-title]Haal dependencies binnen via de interne registry of proxy van het project, bijvoorbeeld Nexus Repository of Harbor, en niet rechtstreeks van publieke registries.[/submeasure-title] Controleer de herkomst van een dependency waar dat mogelijk is, bijvoorbeeld via ondertekende releases, provenance-attestaties of ondertekende images.

### Dependencies bijwerken

Doel van de aanbevelingen voor het bijwerken van dependencies is om de risico's die nieuwe versies met zich meebrengen te beperken.

6. [submeasure-title]Gebruik een cooldown van minstens 7 dagen voor het toepassen van een nieuwe versie.[/submeasure-title] Weeg bij het kiezen van een langere cooldownperiode bewust het lagere risico op supply chain attacks af tegen het hogere beveiligingsrisico door het later ontvangen van security fixes. Sla bij een kritische security fix de cooldown eventueel (incidenteel) over. Configureer de voor updates gebruikte tools om de cooldown te hanteren, bijvoorbeeld `min-release-age` in `.npmrc` of uv's `exclude-newer` in `pyproject.toml`.
7. [submeasure-title]Beoordeel voor het updaten naar een major release van een dependency het risico van de nieuwe release.[/submeasure-title] Kijk of de nieuwe release veranderingen bevat die het risico op regressies vergroten, zoals veel nieuwe functionaliteit, backwards-incompatible changes of een grote refactoring. Wacht in dat geval op de eerste of tweede patchrelease voor het bijwerken van de versie.
8. [submeasure-title]Gebruik tooling om dependencies periodiek (bijvoorbeeld eenmaal per sprint) te updaten, bijvoorbeeld met de package manager, Renovate, Dependabot of Update-time.[/submeasure-title]
9. [submeasure-title]Behandel een update van een dependency als elke andere wijziging: open een merge request, lees de release notes of changelog van de nieuwe versie op breaking changes, gedragsveranderingen en verdachte wijzigingen, en controleer of de volledige pipeline slaagt.[/submeasure-title] Review de wijzigingen in transitieve dependencies (zichtbaar in lockfiles en/of SBoM) risicogestuurd: nieuwe runtime- en builddependencies, nieuwe herkomsten, dependency-downgrades, licentiewijzigingen en nieuwe bekende kwetsbaarheden vereisen expliciete aandacht. Merge updates niet automatisch. Stel bij een major update expliciet vast welke aanpassingen aan de eigen software nodig zijn.

### Dependencies monitoren

Tenslotte aanbevelingen om dependencies te monitoren op nieuwe risico's die ontstaan of bekend worden na de update.

10. [submeasure-title]Draai dagelijks de auditfunctie van de package manager, bijvoorbeeld `npm audit` of `pip-audit`, of analyseer dagelijks de SBoM, bijvoorbeeld in Dependency-Track, om dependencies te checken op bekende kwetsbaarheden.[/submeasure-title] Doe dit niet alleen voor de actuele dependencies, maar ook voor de dependencies van releases van de eigen software, bijvoorbeeld door de SBoM van releases te analyseren in Dependency-Track. Nieuwe kwetsbaarheden worden immers dagelijks ontdekt, ook als de eigen software niet verandert. Analyseer de ernst van de uitkomsten en neem mitigerende maatregelen (bijvoorbeeld dependencies eerder upgraden, downgraden, of vervangen, patch release van de eigen software uitbrengen, beheerpartij informeren) of accepteer expliciet het risico.
11. [submeasure-title]Analyseer periodiek, bijvoorbeeld eenmaal per kwartaal, of een dependency nog onderhouden wordt.[/submeasure-title] Controleer dezelfde punten als bij aanbeveling 1.1. Als een dependency niet meer onderhouden lijkt, neem dan een mitigerende maatregel (bijvoorbeeld migreren, vendoren of zelf bouwen) of accepteer expliciet het risico.

### Rationale
Dependencies vormen een belangrijk onderdeel van de software. Nieuwe versies leveren noodzakelijke security fixes, maar brengen ook risico's mee zoals nieuwe fouten en het risico op supply chain attacks. Het zorgvuldig selecteren, precies specificeren, regelmatig bijwerken en doorlopend monitoren houden de risico's beheersbaar.
