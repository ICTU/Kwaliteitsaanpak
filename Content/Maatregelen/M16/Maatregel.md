## $M16$

#include "Content/Maatregelen/M16/Definitie.md"

ICTU adviseert en ondersteunt voor de hieronder genoemde taken specifieke tools. Projecten gebruiken deze tools, of gelijkwaardige alternatieven.

| Activiteit | Tools |
|---|---|
| Product en sprint backlog management en agile werken | Azure DevOps of Jira |
| Inrichten en uitvoeren van een continuous delivery pipeline | Jenkins, GitLab CI/CD (Continuous Integration, Delivery, and Deployment) of Azure DevOps |
| Monitoren van de kwaliteit van broncode | SonarQube |
| Versiebeheer van op te leveren producten | GitLab of Azure DevOps |
| Release van software | Releaseserver in het ontwikkelplatform |
| Maken van testrapportages | JUnit, Robot Framework, TestNG, of hiermee compatible tools |
| Maken van kwaliteitsrapportages | Quality-time |
| Actueel houden van externe software | RenovateBot |
| Controleren op aanwezigheid van bekende kwetsbaarheden in externe software | OWASP (Open Web Application Security Project) Dependency-Check en/of Dependency-Track |
| Statische controle van de software op aanwezigheid van kwetsbare constructies | SonarQube |
| Dynamische controle van de software op aanwezigheid van kwetsbare constructies | ZAP (Zed Attack Proxy) by Checkmarx |
| Controleren van container images op aanwezigheid van bekende kwetsbaarheden | Trivy |
| Testen van performance en schaalbaarheid | JMeter en Performancetestrunner |
| Testen op toegankelijkheid van de applicatie | Axe |
| Produceren van een "software bill of materials" (SBoM) | Tools die een SBoM in CycloneDX-formaat (zie https://cyclonedx.org) genereren |
| Opslaan van artifacten | Nexus of Harbor |
| Registratie van incidenten bij gebruik en beheer | Jira |
| Bij het uitvoeren van operationeel beheer; uitrollen van de software in de productieomgeving | Ansible |

N.B. Onder het ondersteunen van "agile werken" vallen het opvoeren van eisen, het opvoeren van logische testgevallen, het koppelen van logische testgevallen aan eisen, het bijhouden van een werkvoorraad, het plannen van iteraties en het toewijzen van eisen aan iteraties. De 'eisen' worden, conform Scrumterminologie, geregistreerd als epics en/of user stories, de werkvoorraad als product backlog en de iteraties als sprints. Het toewijzen van eisen aan iteraties gebeurt via de sprint backlog.

### Rationale

Projecten hebben een redelijke vrijheid bij het kiezen en gebruiken van tools, maar voor een aantal taken is het gebruik verplicht gesteld. Deze tools zijn nodig voor een efficiënte uitvoering van de Kwaliteitsaanpak. Uniform gebruik van deze tools maakt het mogelijk koppeling tussen die tools voor alle projecten te standaardiseren; daarnaast bevordert het de uitwisselbaarheid van medewerkers en neemt het risico op het gebruik van onvolwassen tools af. Tot slot is het gebruik in een aantal gevallen, ten behoeve van informatiebeveiliging bij de overheid, verplicht.
