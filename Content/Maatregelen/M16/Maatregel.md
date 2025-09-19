## $M16$

#include "Content/Maatregelen/M16/Definitie.md"

ICTU adviseert en ondersteunt voor de hieronder genoemde taken specifieke tools. Projecten gebruiken deze tools, of gelijkwaardige alternatieven.

| Activiteit | Tools |
|---|---|
| [submeasure-title]Product en sprint backlog management en agile werken[/submeasure-title] | Azure DevOps of Jira |
| [submeasure-title]Inrichten en uitvoeren van een continuous delivery pipeline[/submeasure-title] | Jenkins, GitLab CI/CD (Continuous Integration, Delivery, and Deployment) of Azure DevOps |
| [submeasure-title]Monitoren van de kwaliteit van broncode[/submeasure-title] | SonarQube |
| [submeasure-title]Versiebeheer van op te leveren producten[/submeasure-title] | GitLab of Azure DevOps |
| [submeasure-title]Release van software[/submeasure-title] | Releaseserver in het ontwikkelplatform |
| [submeasure-title]Maken van testrapportages[/submeasure-title] | JUnit, Robot Framework, TestNG, of hiermee compatible tools |
| [submeasure-title]Maken van kwaliteitsrapportages[/submeasure-title] | Quality-time |
| [submeasure-title]Controleren op aanwezigheid van bekende kwetsbaarheden in externe software[/submeasure-title] | OWASP (Open Web Application Security Project) Dependency-Check en/of Dependency-Track |
| [submeasure-title]Statische controle van de software op aanwezigheid van kwetsbare constructies[/submeasure-title] | SonarQube |
| [submeasure-title]Dynamische controle van de software op aanwezigheid van kwetsbare constructies[/submeasure-title] | ZAP (Zed Attack Proxy) by Checkmarx |
| [submeasure-title]Controleren van container images op aanwezigheid van bekende kwetsbaarheden[/submeasure-title] | Trivy |
| [submeasure-title]Testen van performance en schaalbaarheid[/submeasure-title] | JMeter en Performancetestrunner |
| [submeasure-title]Testen op toegankelijkheid van de applicatie[/submeasure-title] | Axe |
| [submeasure-title]Produceren van een "software bill of materials" (SBoM)[/submeasure-title] | Tools die een SBoM in CycloneDX-formaat (zie https://cyclonedx.org) genereren |
| [submeasure-title]Opslaan van artifacten[/submeasure-title] | Nexus of Harbor |
| [submeasure-title]Registratie van incidenten bij gebruik en beheer[/submeasure-title] | Jira |
| [submeasure-title]Bij het uitvoeren van operationeel beheer; uitrollen van de software in de productieomgeving[/submeasure-title] | Ansible |

N.B. Onder het ondersteunen van "agile werken" vallen het opvoeren van eisen, het opvoeren van logische testgevallen, het koppelen van logische testgevallen aan eisen, het bijhouden van een werkvoorraad, het plannen van iteraties en het toewijzen van eisen aan iteraties. De 'eisen' worden, conform Scrumterminologie, geregistreerd als epics en/of user stories, de werkvoorraad als product backlog en de iteraties als sprints. Het toewijzen van eisen aan iteraties gebeurt via de sprint backlog.

### Rationale

Projecten hebben een redelijke vrijheid bij het kiezen en gebruiken van tools, maar voor een aantal taken is het gebruik verplicht gesteld. Deze tools zijn nodig voor een efficiënte uitvoering van de Kwaliteitsaanpak. Uniform gebruik van deze tools maakt het mogelijk koppeling tussen die tools voor alle projecten te standaardiseren; daarnaast bevordert het de uitwisselbaarheid van medewerkers en neemt het risico op het gebruik van onvolwassen tools af. Tot slot is het gebruik in een aantal gevallen, ten behoeve van informatiebeveiliging bij de overheid, verplicht.
