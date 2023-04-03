## $M16$

#include "Content/Maatregelen/M16/Definitie.md"

Onder het ondersteunen van "agile werken" vallen het opvoeren van eisen, het opvoeren van logische testgevallen, het koppelen van logische testgevallen aan eisen, het bijhouden van een werkvoorraad, het plannen van iteraties en het toewijzen van eisen aan iteraties. De 'eisen' worden, conform Scrumterminologie, geregistreerd als epics en/of user stories, de werkvoorraad als backlog en de iteraties als sprints.

ICTU adviseert en ondersteunt voor de genoemde taken onderstaande tools. Projecten gebruiken deze tools:

1. Backlogmanagement en agile werken: Azure DevOps of Jira,
2. Continuous delivery pipeline: Jenkins, GitLab CI/CD (Continuous Integration, Delivery, and Deployment) of Azure DevOps,
3. Kwaliteit van broncode: SonarQube,
4. Versiebeheer: GitLab of Azure DevOps,
5. Release van software: Releaseserver in het ontwikkelplatform,
6. Testrapportages: JUnit, Robot Framework, TestNG, of hiermee compatible tools,
7. Kwaliteitsrapportages: Quality-time,
8. Kwetsbaarheden in configuratie: OpenVAS (Vulnerability Assessment System),
9. Kwetsbaarheden in externe software: OWASP (Open Web Application Security Project) Dependency Checker,
10. Kwetsbaarheden in software: GitLab SAST (Static Application Security Testing), SonarQube en/of OWASP ZAP (Zed Attack Proxy),
11. Kwetsbaarheden in container images: Trivy,
12. Performancetesten en performancetestrapportages: JMeter en Performancetestrunner,
13. Toegankelijkheid: Axe,
14. Software bill of materials: tools die een SBoM in CycloneDX-formaat (zie https://cyclonedx.org) genereren,
15. Artifact repository: Nexus of Harbor,
16. Registratie van incidenten bij gebruik en beheer: Jira,
17. Bij een DevOps werkwijze; uitrollen in de productieomgeving: Ansible.

### Rationale

Projecten hebben een redelijke vrijheid bij het kiezen en gebruiken van tools, maar voor een aantal taken is het gebruik verplicht gesteld. Deze tools zijn nodig voor een efficiënte uitvoering van de Kwaliteitsaanpak. Uniform gebruik van deze tools maakt het mogelijk koppeling tussen die tools voor alle projecten te standaardiseren; daarnaast bevordert het de uitwisselbaarheid van medewerkers en neemt het risico op het gebruik van onvolwassen tools af. Tot slot is het gebruik in een aantal gevallen, ten behoeve van informatiebeveiliging bij de overheid, verplicht.
