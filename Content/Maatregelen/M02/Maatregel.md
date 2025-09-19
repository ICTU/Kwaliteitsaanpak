## $M02$

#include "Content/Maatregelen/M02/Definitie.md"

De kwaliteitsnormen voor het product zijn beschreven in de niet-functionele eisen, het informatiebeveiligingsplan, het kwaliteitsplan en deze Kwaliteitsaanpak, zie [$M01$](#m01).

Om continu te bewaken dat het product aan de kwaliteitsnormen voldoet, voert het project de volgende activiteiten uit:

1. [submeasure-title]Tijdens de voorfase: het project reviewt de deliverables periodiek[/submeasure-title],
1. [submeasure-title]Tijdens de realisatiefase: het project bewaakt op dagelijkse basis en geautomatiseerd de kwaliteit van de software[/submeasure-title],
1. [submeasure-title]Als operationeel beheer onderdeel is van de dienstverlening tijdens de realisatiefase: het project bewaakt op dagelijkse basis en geautomatiseerd het gedrag van de software in gebruik en beheer[/submeasure-title],
1. [submeasure-title]Tijdens de realisatiefase: het project evalueert periodiek en handmatig de kwaliteitseigenschappen van de software die niet geautomatiseerd kunnen worden gemeten[/submeasure-title],
1. [submeasure-title]Tijdens de realisatiefase: het project actualiseert en reviewt periodiek de documentatie[/submeasure-title],
1. [submeasure-title]Indien nodig: de kwaliteitsmanager escaleert het langdurig niet halen van de kwaliteitsnormen[/submeasure-title].

Daarnaast voert het project periodiek een self-assessment uit tegen de actuele versie van de Kwaliteitsaanpak, zie [$M28$](#m28).

### Voorfase: review documenten

Tijdens de voorfase wordt het voldoen aan de kwaliteitsnormen met behulp van reviews gecontroleerd, normaal gesproken elke sprint. Als onderdeel van het op te stellen kwaliteitsplan wordt tijdens de voorfase bepaald hoe het project de kwaliteit tijdens realisatie gaat controleren; voor producten die niet geautomatiseerd kunnen worden gecontroleerd, beschrijft het kwaliteitsplan een alternatieve aanpak. Als bijvoorbeeld door de gekozen technologie geen ondersteuning van het kwaliteitssysteem mogelijk is, kunnen periodieke, handmatige controles als alternatief ingezet worden.

### Realisatiefase: geautomatiseerde kwaliteitsmeting

Tijdens de realisatiefase wordt de kwaliteit diverse malen per uur gemeten door Quality-time, een door ICTU ontwikkeld, open source, geautomatiseerd kwaliteitssysteem. De kwaliteitsmanager configureert de kwaliteitsrapportage in Quality-time en past waar nodig de normen aan, op basis van de projectspecifieke kwaliteitseisen.

Het Scrumteam kijkt dagelijks of er afwijkingen van de normen zijn en onderneemt actie, indien nodig. Ook de kwaliteitsmanager signaleert afwijkingen en meldt deze bij het Scrumteam tijdens de daily scrum en/of tijdens het projectoverleg.

### Realisatiefase operationeel beheer: geautomatiseerde monitoring

Als operationeel beheer onderdeel is van de dienstverlening tijdens de realisatiefase monitort en test het project continue het gedrag van de software in gebruik en beheer. Hiertoe gebruikt het project operationele monitoringsoftware, bijvoorbeeld Nagios en/of Zabbix.

### Realisatiefase: handmatige evaluatie

Kwaliteitseigenschappen van de software die niet (volledig) geautomatiseerd kunnen worden gemeten, worden tijdens de realisatiefase periodiek handmatig geëvalueerd. Minimaal betreft dit de beveiliging van de software, zie [$M26$](#m26). Voor kwaliteitsaspecten als toegankelijkheid en gebruikskwaliteit organiseert het project handmatige testen en/of evaluaties in een vorm en met een frequentie die aansluit bij de aard van de applicatie en de door de opdrachtgevende organisatie gestelde eisen. De kwaliteitsmanager houdt in Quality-time bij wanneer de laatste test of evaluatie is uitgevoerd en wanneer het tijd is voor de volgende.

### Realisatiefase: actualisering en review documentatie

Documenten, die onderdeel uitmaken van het op te leveren projectresultaat, zijn zo veel mogelijk geactualiseerd; eventuele achterstand wordt planmatig weggewerkt. De kwaliteitscontrole van documenten gebeurt op basis van reviews. De auteur van een document en de software delivery manager zorgen dat de juiste reviewers benoemd zijn; hiertoe behoort in ieder geval de kwaliteitsmanager. De auteur van het document zorgt voor een correct versiebeheer van het document. De auteur koppelt aan de reviewers terug of en hoe het ontvangen commentaar is verwerkt in de volgende versie van het betreffende document.

### Escalatie

Als de kwaliteitsnormen langdurig niet worden behaald heeft de kwaliteitsmanager de volgende escalatielijn:

* De kwaliteitsmanager bespreekt de situatie met de software delivery manager.
* Indien dat niet tot resultaat leidt, escaleert de kwaliteitsmanager de situatie naar de projectleider.
* Indien dat ook niet tot resultaat leidt, escaleert de kwaliteitsmanager de situatie naar het hoofd van de afdeling ICTU Software Expertise (ISE).

### Rationale

Vaak de kwaliteitsnormen bewaken maakt een actueel inzicht mogelijk. Projectleden kunnen snel reageren op afwijkingen, die in de regel ook pas recent zijn ontstaan en dus meestal gerelateerd zijn aan huidige activiteiten. Met name afwijkingen van de normen op het vlak van informatiebeveiliging en onderhoudbaarheid komen zo snel aan het licht en kunnen dan ook snel worden beoordeeld en - indien nodig en mogelijk - opgelost.
