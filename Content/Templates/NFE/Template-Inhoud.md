# Functional suitability

Capability of a product to provide functions that meet stated and implied needs of intended users when it is used under specified conditions.

Opmerking: functional suitability gaat alleen over of, en in welke mate, expliciete en impliciete behoeften worden afgedekt en betreft niet de functionele eisen zelf.

## Functional completeness

Capability of a product to provide a set of functions that covers all the specified tasks and intended users’ objectives.

#include "Content/Templates/NFE/Eisentabel.md"

## Functional correctness

Capability of a product to provide accurate results when used by intended users.

#include "Content/Templates/NFE/Eisentabel.md"

## Functional appropriateness

Capability of a product to provide functions that facilitate the accomplishment of specified tasks and objectives.

#include "Content/Templates/NFE/Eisentabel.md"

# Performance-efficiency

Capability of a product to perform its functions within specified time and throughput parameters and be efficient in the use of resources under specified conditions.

## Time behavior

Capability of a product to perform its specified function under specified conditions so that the response time and throughput rates meet the requirements.

#include "Content/Templates/NFE/Eisentabel.md"

## Resource utilization

Capability of a product to use no more than the specified amount of resources to perform its function under specified conditions.

#include "Content/Templates/NFE/Eisentabel.md"

## Capacity

Capability of a product to meet requirements for the maximum limits of a product parameter.

#include "Content/Templates/NFE/Eisentabel.md"

# Compatibility

Capability of a product to exchange information with other products, and/or to perform its required functions while sharing the same common environment and resources.

## Co-existence

Capability of a product to perform its required functions efficiently while sharing a common environment and resources with other products, without detrimental impact on any other product.

#include "Content/Templates/NFE/Eisentabel.md"

## Interoperability

Capability of a product to exchange information with other products and mutually use the information that has been exchanged.

#include "Content/Templates/NFE/Eisentabel.md"

# Interaction capability

Capability of a product to be interacted with by specified users to exchange information between a user and a system via the user interface to complete the intended task.

## Appropriateness recognizability

Capability of a product to be recognized by users as appropriate for their needs.

#include "Content/Templates/NFE/Eisentabel.md"

## Learnability

Capability of a product to have specified users learn to use specified product functions within a specified amount of time.

#include "Content/Templates/NFE/Eisentabel.md"

## Operability

Capability of a product to have functions and attributes that it easy to operate and control.

#include "Content/Templates/NFE/Eisentabel.md"

## User error protection

Capability of a product to prevent operation errors.

#include "Content/Templates/NFE/Eisentabel.md"

## User engagement

Capability of a product to present functions and information in an inviting and motivating manner encouraging continued interaction.

#include "Content/Templates/NFE/Eisentabel.md"

## Inclusivity

Capability of a product to be utilised by people of various backgrounds.

Als standaard voor toegankelijkheid hanteert de Nederlandse overheid de Web Content Accessibility Guidelines (WCAG), zie [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/). Officieel gebruikt de Nederlandse Overheid versie 2.1, maar het gebruik van versie 2.2 wordt [aangeraden](https://www.digitaleoverheid.nl/nieuws/nieuwe-aanbevolen-standaard-digitale-toegankelijkheid/).

Van WCAG versie 2.2 is op het moment nog geen Nederlandse vertaling, wel van versie 2.1, zie [https://www.w3.org/Translations/WCAG22-nl/](https://www.w3.org/Translations/WCAG21-nl/).

Conform de EN 301 549, hanteert {opdrachtgevende organisatie} de succescriteria voor niveau A en AA als eisen.

| Nr. | Eis                                                                 | Prio   | Rationale               | Realisatie in | Realisatie door | Bewijs              |
| :--- | :------------------------------------------------------------------ | :----- | :---------------------- | :------------ | :-------------- | :------------------ |
| 1   | De applicatie voldoet aan de WCAG2.2 succescriteria, niveau A en AA | {prio} | Wettelijke verplichting | {software}    | ICTU            | Axe-core rapportage |

Onderstaande tabel bevat de WCAG2.2 succescriteria. {Verwijder de AAA-succescriteria indien gewenst.} Per succescriterium is aangegeven of Axe-core, en zo ja met welke regels, het criterium geautomatiseerd kan controleren. {Geef aan of de succescriteria die Axe-core niet geautomatiseerd kan controleren wel of niet met de hand zullen worden gecontroleerd.}

Merk op dat de [Axe-core regels die als "experimenteel" zijn gemarkeerd](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md#experimental-rules) niet standaard door Axe-core worden getest. Zie de [Axe-core API-documentatie](https://www.deque.com/axe/core-documentation/api-documentation/#options-parameter) voor instructies hoe dit aan te passen.

#include "Content/Templates/NFE/WCAG-Tabel-Gegenereerd.md"

## User assistance

Capability of a product to be used by people with the widest range of characteristics and capabilities to achieve specified goals in a specified context of use.

#include "Content/Templates/NFE/Eisentabel.md"

## Self-descriptiveness

Capability of a product to present appropriate information, where needed by the user, to make its capabilities and use immediately obvious to the user without excessive interactions with a product or other resources.

#include "Content/Templates/NFE/Eisentabel.md"

## Taal en leesbaarheid

Naast de aan NEN-ISO/IEC 25010:2023 ontleende hoofdeigenschap bruikbaarheid zijn voor de gebruikskwaliteit van {het product} van belang:

* Taal: welke talen dienen te worden ondersteund.
* Leesbaarheid: teksten moeten makkelijk te lezen zijn. Korte zinnen hebben de voorkeur. Hoe gemakkelijker de zin en de woorden, hoe beter de leesbaarheid.

| Nr. | Eis                                            | Prio   | Rationale                                                                                                            | Realisatie in | Realisatie door | Bewijs   |
| :--- | :--------------------------------------------- | :----- | :------------------------------------------------------------------------------------------------------------------- | :------------ | :-------------- | :------- |
| 1   | De applicatie gebruikt maximaal taalniveau B1  | {prio} | [Aanbevolen richtlijn](https://www.communicatierijk.nl/vakkennis/rijkswebsites/aanbevolen-richtlijnen/taalniveau-b1) | {software}    | {partij}        | {bewijs} |
| 2   | De applicatie ondersteunt {ondersteunde talen} | {prio} | {rationale}                                                                                                          | {software}    | ICTU            | {bewijs} |

# Reliability

Capability of a product to perform specified functions under specified conditions for a specified period of time without interruptions and failures.

## Faultlessness

Capability of a product to perform specified functions without fault under normal operation.

#include "Content/Templates/NFE/Eisentabel.md"

## Availability

Capability of a product to be operational and accessible when required for use.

#include "Content/Templates/NFE/Eisentabel.md"

## Fault tolerance

Capability of a product to operate as intended despite the presence of hardware or software faults.

#include "Content/Templates/NFE/Eisentabel.md"

## Recoverability

Capability of a product in the event of an interruption or a failure to recover the data directly affected and re-establish the desired state of the system.

#include "Content/Templates/NFE/Eisentabel.md"

# Security

Capability of a product to protect information and data so that persons or other products have the degree of data access appropriate to their types and levels of authorization, and to defend against attack patterns by malicious actors.

## BIO- en SSD-eisen

De overheid is gebonden aan kaderstelling op het gebied van informatiebeveiliging, zoals de Baseline Informatiebeveiliging Overheid (BIO). Handvatten zoals Secure Software Development (SSD) van het Centrum Informatiebeveiliging en Privacybescherming dienen als leidraad voor het veilig ontwikkelen van software die het voldoen aan de BIO ondersteunt. De BIO is een toepassing van de NEN-ISO/IEC 27001 en de NEN-ISO/IEC 27002 op het domein van de Nederlandse overheid. Voor de Rijksoverheid zijn in die toepassing het Voorschrift Informatiebeveiliging Rijksdienst 2007 (VIR 2007) en het Besluit Voorschrift Informatiebeveiliging Rijksdienst Bijzondere Informatie 2013 (VIRBI 2013) verwerkt.

BIO en SSD bevatten ook een aantal maatregelen ten aanzien van software en/of de infrastructurele componenten waar deze software gebruik van maakt. Deze maatregelen zijn hieronder als eisen opgenomen.

| Nr.  | Eis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Prio   | Rationale                                                                                                                                                                                                                                          | Realisatie in                    | Realisatie door | Bewijs                           |
| :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- | :-------------- | :------------------------------- | -------- | -------- |
| 1    | Applicaties zijn gebaseerd op een formele, met de beheerorganisatie afgestemde standaard stack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | {prio} | Dit maakt integrale beveiliging mogelijk en beperkt het risico op nieuwe en onbekende zwakheden door het gebruik van onbekende componenten of services                                                                                             | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 2    | De architectuur van een (web)applicatie is gebaseerd op een gelaagde structuur door de presentatielaag, de applicatielaag en de gegevens te scheiden                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | {prio} | Hierdoor kunnen de lagen beschermd worden binnen de netwerkzones                                                                                                                                                                                   | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 3    | (Web)applicaties stellen de identiteit van externe gebruikers vast op basis van een mechanisme voor identificatie en authenticatie, waarbij de authenticatiegegevens in een geconsolideerde authenticatievoorziening worden beheerd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 4    | (Web)applicaties stellen de identiteit van interne gebruikers vast op basis van een mechanisme voor identificatie en authenticatie, waarbij de authenticatie- en autorisatiegegevens in een geconsolideerde authenticatie- en autorisatievoorziening worden beheerd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 5    | Inrichting van de autorisaties van gebruikers (inclusief beheerders) binnen een (web)applicatie:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | {prio} | Autorisaties kunnen worden toegewezen aan organisatorische functies en scheiding van niet te verenigen autorisaties is mogelijk                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 5a   | In de applicatie zijn de autorisaties op een beheersbare wijze geordend. De applicatie maakt daartoe gebruik van autorisatiegroepen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 5b   | Op basis van taken, verantwoordelijkheden en bevoegdheden zijn de niet te verenigen taken en autorisaties geïdentificeerd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 5c   | Verantwoordelijkheden voor beheer en wijziging van gegevens en bijbehorende informatiesysteemfuncties moeten eenduidig toegewezen zijn aan één specifieke (beheerders)rol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 5d   | Er is een scheiding tussen beheertaken en overige gebruikstaken. Beheerswerkzaamheden worden alleen uitgevoerd wanneer ingelogd als beheerder, normale gebruikstaken alleen wanneer ingelogd als gebruiker                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 6    | Applicaties hebben een beheerinterface dat gescheiden is van de standaard gebruikersinterface. Deze scheiding komt zowel in de operationele interfaces (dat wil zeggen de deployment van de onderdelen) als in de autorisaties die toegang geven tot de interfaces tot uitdrukking. Het uiterlijk van de beheerinterface onderscheidt zich eveneens van de gebruikersinterface                                                                                                                                                                                                                                                                                                                                                                                                                             | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 7    | Activiteiten van gebruikers, uitzonderingen en informatiebeveiligingsgebeurtenissen behoren te worden vastgelegd in audit-logbestanden. Deze logbestanden behoren gedurende een overeengekomen periode te worden bewaard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {prio} | Mogelijk maken van toekomstig onderzoek en toegangscontrole                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 8    | Applicaties normaliseren de invoer, valideren de invoer op syntax en semantiek en normaliseren uitvoer waar dit toepasbaar is                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | {prio} | Normaliseren en valideren van de invoer beschermt een applicatie tegen manipulatie (cross-site scripting, cross-site request forgery SQL-injectie, buffer overflow, et cetera). Normaliseren van uitvoer beschermt de ontvanger tegen manipulatie. | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 9    | Wanneer de invoervalidatie faalt, stopt de verwerking van de betreffende invoer in zijn geheel en hervat de applicatie zijn normale functies alsof de invoer nooit ontvangen was. Het falen wordt wel gelogd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {prio} | Onbeschikbaarheid van de applicatie voorkomen en tegelijkertijd analyse van de opgetreden situatie mogelijk maken                                                                                                                                  | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 10   | Applicaties maken gebruik van statisch geconfigureerde queries en/of commando’s, waarbij parameters/variabelen zodanig worden ingevoegd dat zij de beoogde werking niet kunnen beïnvloeden. Voor databases is dit bekend als een ‘prepared query’. Voor commando’s is een constructie gekozen die interpretatie van een parameter/variabele door een commando interpreter/shell uitsluit. Mocht het niet mogelijk zijn hieraan te voldoen, dan wordt de waarde van elke parameter/variabele voor gebruik zodanig behandeld dat dezelfde zekerheid wordt verkregen. Te allen tijde wordt voorkomen dat vrije toegang tot het commando- of query-interface gegeven wordt. Dit geldt zowel voor waarden die door een gebruiker (in)direct worden aangeleverd, als voor waarden uit configuraties of databases | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 11   | Een (web)applicatie is voorzien van Concurrent Session Control, die slechts één sessie per gebruiker toestaat, tenzij onderbouwd is dat meer noodzakelijk is                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 12   | Een applicatie heeft een instelbare maximale sessieduur en een maximale duur van inactiviteit. Na deze periode wordt een sessie automatisch afgesloten, alsof de gebruiker zelf de sessie beëindigd heeft                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 13   | De maximale sessieduur en maximale inactiviteit zijn door (of namens) de opdrachtgevende organisatie in te stellen. De instelbare waarden zijn per default begrenst op 10 uur (sessieduur) en 15 minuten (inactiviteit). Alleen op expliciet aangeven van de opdrachtgevede organisatie kan hiervan worden afgeweken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 14   | Applicaties maken gebruik van gangbare protocollen en cryptografische technieken, versleutelen informatie volgens de maatregelenselectie in het IB-plan en borgen de onweerlegbaarheid van daartoe aangewezen transacties via cryptografische technieken. De gebruikte cryptografische algoritmen voor versleuteling zijn als open standaard gedocumenteerd en zijn door onafhankelijke betrouwbare deskundigen getoetst. De cryptografische beveiligingsvoorzieningen en componenten voldoen aan algemeen gangbare beveiligingscriteria (zoals FIPS 140-2 en waar mogelijk NBV)                                                                                                                                                                                                                           | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 15   | (Web)applicaties voorkomen de mogelijkheid van dynamische file includes. Indien gebruik gemaakt wordt van een applicatieserver sluit de serverconfiguratie file includes uit. Mocht het niet mogelijk zijn aan hieraan te voldoen, dan wordt voor de includes gebruik gemaakt van een vertrouwde locatie en een expliciete whitelist voor de files                                                                                                                                                                                                                                                                                                                                                                                                                                                         | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 16   | Applicaties hebben geen run-time afhankelijkheid van externe codebronnen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 17   | Applicaties zijn gemaakt met de op het moment van uitleveren meest recente en/of door de leverancier (lees in het geval van open source: de community) aanbevolen versies van externe bibliotheken, raamwerken of andersoortige bouwblokken. Applicaties gebruiken alleen externe bibliotheken, raamwerken of andersoortige bouwblokken waarvoor de leverancier beveiligingsupdates uitbrengt. Applicaties ondersteunen alleen besturingssystemen of browsers waarvoor de leverancier beveiligingsupdates uitbrengt                                                                                                                                                                                                                                                                                                                          | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 18   | Een applicatie vangt interne fouten (excepties) af op hoofdniveau, zonder ongecontroleerd te falen (crash). Afgevangen fouten worden vastgelegd (log) en aan gebruikers wordt een melding getoond die geen inhoudelijke details bevat. Een betekenisloze referentie (code) van de fout ten behoeve van communicatie over de fout mag wel getoond worden                                                                                                                                                                                                                                                                                                                                                                                                                                                    | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 19   | Een applicatie heeft een uniforme en veilige wijze van applicatie-logging. De logging bevat geen inloggegevens (credentials) of vertrouwelijke gegevens over personen. Referenties (bv identifiers) zijn wel toegestaan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | {prio} | De logging zorgt voor traceerbaarheid van gebeurtenissen en activiteiten in relatie tot ten minste personen, systemen, applicaties en tijd                                                                                                         | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 20   | Een applicatie beperkt de gebruikte protocollen, parameters (headers) en functionaliteit tot wat nodig is. Hieronder vallen ook HTTP-headers en HTTP-methoden (liefst niet meer dan GET en POST):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 20a  | De webserver stuurt bij een antwoord aan een gebruiker alleen die informatie in de HTTP-headers mee die van belang is voor het functioneren van HTTP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 20b  | De webapplicatie toont alleen noodzakelijke informatie in HTTP-headers die van belang is voor het functioneren van HTTP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 20c  | De webserver gebruikt alleen de HTTP-functionaliteiten die nodig zijn voor het functioneren van de webapplicatie                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | {prio} |                                                                                                                                                                                                                                                    | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 21   | De aan de gebruiker aangeboden scripts / code bevat geen commentaar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | {prio} | Voorkomt misbruik van het commentaar                                                                                                                                                                                                               | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 22   | De aan de gebruiker getoonde informatie bevat geen directory listings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | {prio} | Voorkomt misbruik van de directory listing                                                                                                                                                                                                         | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 23   | Wanneer toegang tot (de inhoud van) het filesysteem nodig is, gebeurt dit altijd onder expliciete autorisatie en controle door de applicatie                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 24   | In de (web)applicatieomgeving zijn signaleringsfuncties (registratie en detectie) actief en efficiënt, effectief en beveiligd ingericht                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | {prio} | {rationale}{software, hardware, combinatie}                                                                                                                                                                                                        | {partij}                         |                 | {bewijs}                         |
| {nr} | {eis}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {software, hardware, combinatie} | {partij} | {bewijs} |

## Confidentiality

Capability of a product to ensure that data are accessible only to those authorized to have access.

#include "Content/Templates/NFE/Eisentabel.md"

## Integrity

Capability of a product to ensure that the state of its system and data are protected from unauthorized modification or deletion either by malicious action or computer error.

#include "Content/Templates/NFE/Eisentabel.md"

## Non-repudiation

Capability of a product to prove that actions or events have taken place, so that the events or actions cannot be repudiated later.

#include "Content/Templates/NFE/Eisentabel.md"

## Accountability

Capability of a product to enable actions of an entity to be traced uniquely to the entity.

#include "Content/Templates/NFE/Eisentabel.md"

## Authenticity

Capability of a product to prove that the identity of a subject or resource is the one claimed.

#include "Content/Templates/NFE/Eisentabel.md"

## Resistance

Capability of a product to sustain operations while under attack from a malicious actor.

#include "Content/Templates/NFE/Eisentabel.md"

# Maintainability

Capability of a product to be modified by the intended maintainers with effectiveness and efficiency.

## Modularity

Capability of a product to limit changes to one component from affecting other components.

#include "Content/Templates/NFE/Eisentabel.md"

## Reusability

Capability of a product to be used as assets in more than one system, or in building other assets.

#include "Content/Templates/NFE/Eisentabel.md"

## Analysability

Capability of a product to be effectively and efficiently assessed regarding the impact of an intended change to one or more of its parts, to diagnose it for deficiencies or causes of failures, or to identify parts to be modified.

#include "Content/Templates/NFE/Eisentabel.md"

## Modifiability

Capability of a product to be effectively and efficiently modified without introducing defects or degrading existing product quality.

#include "Content/Templates/NFE/Eisentabel.md"

## Testability

Capability of a product to enable an objective and feasible test to be designed and performed to determine whether a requirement is met.

#include "Content/Templates/NFE/Eisentabel.md"

# Flexibility

Capability of a product to be adapted to changes in its requirements, contexts of use, or system environment.

## Adaptability

Capability of a product to be effectively and efficiently adapted for or transferred to different hardware, software or other operational or usage environments.

#include "Content/Templates/NFE/Eisentabel.md"

## Scalability

Capability of a product to handle growing or shrinking workloads or to adapt its capacity to handle variability.

#include "Content/Templates/NFE/Eisentabel.md"

## Installability

Capability of a product to be effectively and efficiently installed successfully and/or uninstalled in a specified environment.

#include "Content/Templates/NFE/Eisentabel.md"

## Replaceability

Capability of a product to replace another specified product for the same purpose in the same environment.

#include "Content/Templates/NFE/Eisentabel.md"

# Safety

Capability of a product under defined conditions to avoid a state in which human life, health, property, or the environment is endangered.

## Operational constraint

Capability of a product to constrain its operation to within safe parameters or states when encountering operational hazard.

#include "Content/Templates/NFE/Eisentabel.md"

## Risk identification

Capability of a product to identify a course of events or operations that can expose life, property or environment to unacceptable risk.

#include "Content/Templates/NFE/Eisentabel.md"

## Fail safe

Capability of a product to automatically place itself in a safe operating mode, or to revert to a safe condition in the event of a failure.

#include "Content/Templates/NFE/Eisentabel.md"

## Hazard warning

Capability of a product to provide warnings of unacceptable risks to operations or internal controls so that they can react in sufficient time to sustain safe operations.

#include "Content/Templates/NFE/Eisentabel.md"

## Safe integration

Capability of a product to maintain safety during and after integration with one or more components.

#include "Content/Templates/NFE/Eisentabel.md"
