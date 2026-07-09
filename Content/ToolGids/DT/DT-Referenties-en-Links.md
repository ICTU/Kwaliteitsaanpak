# Referenties en Links

Deze pagina bevat een overzicht van nuttige bronnen voor wie zich verder wil verdiepen in Dependency-Track. De focus ligt op officiële documentatie, aanvullende standaarden, community-bronnen en verdiepende uitleg over SBoM’s, CycloneDX, kwetsbaarheden en licentiebeleid.

⚠️ Let op: Dependency-Track heeft documentatie voor meerdere versies. Gebruik voor nieuwe installaties en actuele informatie bij voorkeur de v5-documentatie. Gebruik de oudere documentatie alleen wanneer de gebruikte omgeving nog op Dependency-Track v4 draait.

## Officiële bronnen

* **Dependency-Track website**
  De officiële website van Dependency-Track met een algemene uitleg over het platform, de belangrijkste kenmerken en verwijzingen naar documentatie en downloads:
  https://dependencytrack.org/

* **Dependency-Track v5-documentatie**
  De actuele documentatie voor Dependency-Track v5. Deze documentatie bevat tutorials, gebruikershandleidingen, conceptuele uitleg en technische referentie-informatie:
  https://dependencytrack.github.io/docs/next/

* **Dependency-Track v4-documentatie**
  De oudere documentatie voor Dependency-Track v4. Gebruik deze alleen wanneer de gebruikte omgeving nog op v4 draait:
  https://docs.dependencytrack.org/

* **OWASP-projectpagina**
  De officiële OWASP-pagina van Dependency-Track. Hier staat onder meer de OWASP-context, projectinformatie en een overzicht van de belangrijkste kenmerken:
  https://owasp.org/www-project-dependency-track/

* **GitHub-repository Dependency-Track**
  De hoofdrepository met de broncode, releases, issues en projectinformatie:
  https://github.com/DependencyTrack/dependency-track

* **Dependency-Track GitHub-organisatie**
  Overzicht van de officiële Dependency-Track repositories, waaronder de frontend, documentatie, community-resources, Helm charts en client libraries:
  https://github.com/DependencyTrack

* **Quick start**
  Officiële tutorial om Dependency-Track lokaal te starten met Docker Compose:
  https://dependencytrack.github.io/docs/next/tutorials/quickstart/

* **File formats**
  Officiële referentiepagina over ondersteunde bestandsformaten. Belangrijk: Dependency-Track v5 ondersteunt CycloneDX als uploadformaat voor SBoM’s:
  https://dependencytrack.github.io/docs/next/reference/file-formats/

* **Configuratie van vulnerability sources**
  Officiële uitleg over het configureren van kwetsbaarheidsbronnen zoals NVD, GitHub Advisories en OSV:
  https://dependencytrack.github.io/docs/next/guides/administration/configuring-vulnerability-sources/

* **Task scheduler**
  Technische referentie voor geplande taken, zoals het synchroniseren (mirror) van kwetsbaarheidsbronnen, metrics-updates en portfolio vulnerability analysis:
  https://dependencytrack.github.io/docs/next/reference/configuration/task-scheduler/

* **Component policies**
  Uitleg over het aanmaken en beheren van component policies, bijvoorbeeld voor licenties, kwetsbaarheden en operationele risico’s:
  https://dependencytrack.github.io/docs/next/guides/user/managing-component-policies/

* **Component policies referentie**
  Technische referentie voor policy-onderwerpen, operators, violation states en voorwaarden:
  https://dependencytrack.github.io/docs/next/reference/policies/component-policies/

* **REST API v1**
  Referentie voor de Dependency-Track REST API v1. Nuttig voor integraties vanuit CI/CD-pipelines, scripts en rapportagetools:
  https://dependencytrack.github.io/docs/next/reference/api/v1/

* **REST API v2**
  Referentie voor de Dependency-Track REST API v2:
  https://dependencytrack.github.io/docs/next/reference/api/v2/

* **Migratie van v4 naar v5**
  Officiële migratie-informatie voor organisaties die van Dependency-Track v4 naar v5 willen overstappen:
  https://dependencytrack.github.io/docs/next/guides/administration/migrating-from-v4-to-v5/

## SBoM en CycloneDX

* **CycloneDX**
  De officiële website van CycloneDX. CycloneDX is de Bill of Materials-standaard die Dependency-Track gebruikt voor SBoM’s, VEX en VDR:
  https://cyclonedx.org/

* **CycloneDX specificaties**
  Overzicht van de CycloneDX-specificaties en ondersteunde versies:
  https://cyclonedx.org/specification/overview/

* **CycloneDX Tool Center**
  Overzicht van tools die CycloneDX kunnen genereren, verwerken of valideren. Nuttig bij het kiezen van een SBoM-generator voor Maven, Gradle, npm, Python, .NET, containers en andere ecosystemen:
  https://cyclonedx.org/tool-center/

* **CycloneDX CLI**
  Command-line tool voor het valideren, converteren en verwerken van CycloneDX-documenten:
  https://github.com/CycloneDX/cyclonedx-cli

* **CycloneDX Maven-plugin**
  Plugin voor het genereren van CycloneDX-SBoM’s voor Maven-projecten:
  https://github.com/CycloneDX/cyclonedx-maven-plugin

* **CycloneDX Gradle-plugin**
  Plugin voor het genereren van CycloneDX-SBoM’s voor Gradle-projecten:
  https://github.com/CycloneDX/cyclonedx-gradle-plugin

* **CycloneDX Node.js tooling**
  Tooling voor het genereren van CycloneDX-SBoM’s voor Node.js- en npm-projecten:
  https://github.com/CycloneDX/cyclonedx-node-npm

* **CycloneDX Python tooling**
  Tooling voor het genereren van CycloneDX-SBoM’s voor Python-projecten:
  https://github.com/CycloneDX/cyclonedx-python

* **CycloneDX .NET tooling**
  Tooling voor het genereren van CycloneDX-SBoM’s voor .NET-projecten:
  https://github.com/CycloneDX/cyclonedx-dotnet

## VEX en VDR

* **CycloneDX VEX**
  Uitleg over Vulnerability Exploitability Exchange. VEX helpt om vast te leggen of een kwetsbaarheid daadwerkelijk exploiteerbaar is in een specifieke productcontext:
  https://cyclonedx.org/capabilities/vex/

* **CycloneDX VDR**
  Uitleg over Vulnerability Disclosure Reports. Een VDR bevat kwetsbaarheidsinformatie over componenten in een product of project:
  https://cyclonedx.org/use-cases/vulnerability-disclosure/

## Kwetsbaarheidsbronnen en identifiers

* **NVD - National Vulnerability Database**
  Amerikaanse kwetsbaarheidsdatabase van NIST. NVD verrijkt CVE’s onder meer met CVSS-scores, CPE-koppelingen en referenties:
  https://nvd.nist.gov/

* **CVE**
  Officiële website van het CVE-programma. CVE staat voor Common Vulnerabilities and Exposures en biedt unieke identifiers voor publiek bekende kwetsbaarheden:
  https://www.cve.org/

* **GitHub Advisory Database**
  Database met security advisories voor open-source packages in ecosystemen zoals Maven, npm, NuGet, PyPI en RubyGems:
  https://github.com/advisories

* **OSV - Open Source Vulnerabilities**
  Kwetsbaarheidsdatabase gericht op open-source ecosystemen en package-identifiers:
  https://osv.dev/

* **Sonatype OSS Index**
  Kwetsbaarheidsdatabase van Sonatype voor open-source componenten. Let op: controleer altijd of en hoe deze bron in de eigen Dependency-Track-versie of -omgeving gebruikt wordt:
  https://ossindex.sonatype.org/

* **Package URL - PURL**
  Standaard voor het eenduidig identificeren van softwarepackages over verschillende package-ecosystemen heen:
  https://www.packageurl.org/

* **PURL-specificatie**
  Specificatie van Package URL op GitHub:
  https://github.com/package-url/purl-spec

* **CPE - Common Platform Enumeration**
  Gestandaardiseerde naamgeving voor IT-producten, platformen en software. CPE wordt onder meer gebruikt door NVD:
  https://nvd.nist.gov/products/cpe

## Scores en prioritering

* **CVSS - Common Vulnerability Scoring System**
  Standaard voor het bepalen van de technische ernst van kwetsbaarheden:
  https://www.first.org/cvss/

* **NVD CVSS uitleg**
  Uitleg van NVD over het gebruik van CVSS-scores:
  https://nvd.nist.gov/vuln-metrics/cvss

* **EPSS - Exploit Prediction Scoring System**
  Model van FIRST dat inschat hoe waarschijnlijk het is dat een CVE binnen de komende 30 dagen actief wordt misbruikt:
  https://www.first.org/epss/

## Licenties

* **SPDX License List**
  Officiële lijst met SPDX License Identifiers. Deze identifiers zijn nuttig voor consistente licentievermelding in SBoM’s:
  https://spdx.org/licenses/

* **SPDX Specification**
  Specificatie van SPDX. SPDX is breder dan alleen licenties en wordt ook gebruikt voor software supply chain metadata:
  https://spdx.dev/specifications/

## Integraties en deployment

* **Community integrations**
  Overzicht van community-integraties met Dependency-Track, zoals Jenkins, Azure DevOps, Backstage, DefectDojo en verschillende API-clients:
  https://docs.dependencytrack.org/integrations/community-integrations/

* **Dependency-Track Jenkins-plugin**
  Jenkins-plugin voor het publiceren van CycloneDX-SBoM’s naar Dependency-Track:
  https://plugins.jenkins.io/dependency-track/

* **Dependency-Track GitHub Action voor SBoM-upload**
  GitHub Action voor het uploaden van SBoM’s naar Dependency-Track:
  https://github.com/DependencyTrack/gh-upload-sbom

* **Helm charts**
  Officiële Helm charts voor Dependency-Track deployments op Kubernetes:
  https://github.com/DependencyTrack/helm-charts

* **Docker Hub**
  Container-images van Dependency-Track op Docker Hub:
  https://hub.docker.com/u/dependencytrack

## Community en ondersteuning

* **Dependency-Track community repository**
  Community-informatie, waaronder informatie over community meetings en presentatiemateriaal:
  https://github.com/DependencyTrack/community

* **Dependency-Track Slack**
  Officiële Slack-community voor vragen, discussies en contact met gebruikers en maintainers:
  https://dependencytrack.org/slack

* **Dependency-Track groups.io**
  Mailinglist en archief met discussies over Dependency-Track:
  https://groups.io/g/dependency-track

* **YouTube-kanaal**
  Video’s, community meeting recordings en presentaties over Dependency-Track:
  https://www.youtube.com/@DependencyTrack

* **LinkedIn**
  LinkedIn-pagina van OWASP Dependency-Track:
  https://www.linkedin.com/company/owasp-dependency-track

* **Mastodon**
  Mastodon-account van Dependency-Track:
  https://infosec.exchange/@DependencyTrack

## Aanvullende artikelen

* **A practical approach to SBoM in CI/CD - Part III: Tracking SBoMs with Dependency-Track**
  Praktijkartikel over het gebruik van Dependency-Track in een CI/CD-context:
  https://devsec-blog.com/2024/03/a-practical-approach-to-sbom-in-ci-cd-part-iii-tracking-sboms-with-dependency-track/

⚠️ Let op: veel informatie over Dependency-Track is verspreid over meerdere bronnen: de nieuwe v5-documentatie, de oudere v4-documentatie, GitHub, community-discussies en CycloneDX-documentatie. Controleer daarom altijd of een bron past bij de gebruikte Dependency-Track-versie en bij de gekozen SBoM-standaard.
