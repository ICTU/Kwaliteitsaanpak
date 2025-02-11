## $M16$

#include "Content/Maatregelen/M16/Definitie.md"

Onder het ondersteunen van "agile werken" vallen het opvoeren van eisen, het opvoeren van logische testgevallen, het koppelen van logische testgevallen aan eisen, het bijhouden van een werkvoorraad, het plannen van iteraties en het toewijzen van eisen aan iteraties. De 'eisen' worden, conform Scrumterminologie, geregistreerd als epics en/of user stories, de werkvoorraad als backlog en de iteraties als sprints.

ICTU adviseert en ondersteunt voor de genoemde taken onderstaande tools. Projecten gebruiken deze tools, of gelijkwaardige alternatieven:

1. backlog management en agile werken: Azure DevOps of Jira,
2. inrichten en uitvoeren van een continuous delivery pipeline: Jenkins, GitLab CI/CD (Continuous Integration, Delivery, and Deployment) of Azure DevOps,
3. monitoren van de kwaliteit van broncode: SonarQube,
4. versiebeheer van op te leveren producten: GitLab of Azure DevOps,
5. release van software: Releaseserver in het ontwikkelplatform,
6. maken van testrapportages: JUnit, Robot Framework, TestNG, of hiermee compatible tools,
7. maken van kwaliteitsrapportages: Quality-time,
8. controleren op aanwezigheid van bekende kwetsbaarheden in externe software: OWASP (Open Web Application Security Project) Dependency-Check en/of Dependency-Track,
9. statische controle van de software op aanwezigheid van kwetsbare constructies: SonarQube,
10. dynamische controle van de software op aanwezigheid van kwetsbare constructies: ZAP (Zed Attack Proxy) by Checkmarx,
11. controleren van container images op aanwezigheid van bekende kwetsbaarheden: Trivy,
12. testen van performance en schaalbaarheid: JMeter en Performancetestrunner,
13. testen op toegankelijkheid van de applicatie: Axe,
14. produceren van een "software bill of materials" (SBoM): tools die een SBoM in CycloneDX-formaat (zie https://cyclonedx.org) genereren,
15. opslaan van artifacten: Nexus of Harbor,
16. registratie van incidenten bij gebruik en beheer: Jira, en
17. bij het uitvoeren van operationeel beheer; uitrollen van de software in de productieomgeving: Ansible.

### Rationale

Projecten hebben een redelijke vrijheid bij het kiezen en gebruiken van tools, maar voor een aantal taken is het gebruik verplicht gesteld. Deze tools zijn nodig voor een efficiënte uitvoering van de Kwaliteitsaanpak. Uniform gebruik van deze tools maakt het mogelijk koppeling tussen die tools voor alle projecten te standaardiseren; daarnaast bevordert het de uitwisselbaarheid van medewerkers en neemt het risico op het gebruik van onvolwassen tools af. Tot slot is het gebruik in een aantal gevallen, ten behoeve van informatiebeveiliging bij de overheid, verplicht.
