# Functionele geschiktheid

De mate waarin een softwareproduct of computersysteem functies levert die voldoen aan de uitgesproken en veronderstelde behoeften, bij gebruik onder gespecificeerde condities.

Opmerking: functionele geschiktheid gaat alleen over of, en in welke mate, expliciete en impliciete behoeften worden afgedekt en betreft niet de functionele eisen zelf.

## Functionele compleetheid

De mate waarin de set van functies alle gespecificeerde taken en gebruikersdoelen ondersteunen.

#include "Content/Templates/NFE/Eisentabel.md"

## Functionele correctheid

De mate waarin het systeem de juiste resultaten met de benodigde nauwkeurigheid beschikbaar stelt.

#include "Content/Templates/NFE/Eisentabel.md"

## Functionele toepasbaarheid

De mate waarin de functies bijdragen aan het behalen van specifieke taken en doelen.

#include "Content/Templates/NFE/Eisentabel.md"

# Prestatie-efficiëntie

Prestatie van het systeem in verhouding tot het aantal resources, onder bepaalde condities.

## Snelheid

De mate waarin antwoord- en verwerkingstijden en doorvoersnelheid van een product of systeem, tijdens de uitvoer van zijn functies, voldoet aan de wensen.

#include "Content/Templates/NFE/Eisentabel.md"

## Middelenbeslag

De mate waarin de hoeveelheid en type middelen die gebruikt worden door een product of systeem, tijdens de uitvoer van zijn functies, voldoet aan de wensen.

#include "Content/Templates/NFE/Eisentabel.md"

## Capaciteit

De mate waarin de maximale limieten van een product- of systeemparameter voldoet aan de wensen.

#include "Content/Templates/NFE/Eisentabel.md"

# Uitwisselbaarheid

De mate waarin een product, systeem of component informatie uit kan wisselen met andere producten, systemen of componenten, en/of het de gewenste functies kan uitvoeren terwijl het dezelfde hard- of software-omgeving deelt.

## Beïnvloedbaarheid

De mate waarin een product zijn vereiste functies kan vervullen terwijl het een omgeving en resources deelt met andere producten, zonder negatieve impact op enig product.

#include "Content/Templates/NFE/Eisentabel.md"

## Koppelbaarheid

De mate waarin twee of meer systemen, producten of componenten informatie kunnen uitwisselen en deze uitgewisselde informatie kunnen gebruiken.

#include "Content/Templates/NFE/Eisentabel.md"

# Bruikbaarheid

De mate waarin een product of systeem gebruikt kan worden door gespecificeerde gebruikers om effectief, efficiënt en naar tevredenheid gespecificeerde doelen te bereiken in een gespecificeerde gebruikscontext.

## Herkenbaarheid van geschiktheid

De mate waarin gebruikers kunnen herkennen of het product of systeem geschikt is voor hun behoeften.

#include "Content/Templates/NFE/Eisentabel.md"

## Leerbaarheid

De mate waarin het systeem gebruikt kan worden door gespecificeerde gebruikers om gespecificeerde (leer)doelen te bereiken met betrekking tot het gebruik van het systeem met effectiviteit, efficiëntie, vrijheid van risico en voldoening, in een gespecificeerde gebruikscontext.

#include "Content/Templates/NFE/Eisentabel.md"

## Bedienbaarheid

De mate waarin het systeem kenmerken heeft die het makkelijk maken om het te bedienen en beheersen.

#include "Content/Templates/NFE/Eisentabel.md"

## Voorkomen gebruikersfouten

De mate waarin het systeem gebruikers beschermt tegen het maken van fouten.

#include "Content/Templates/NFE/Eisentabel.md"

## Volmaaktheid gebruikersinterface

De mate waarin een gebruikersinterface het de gebruiker mogelijk maakt om een plezierige en voldoening gevende interactie te hebben.

#include "Content/Templates/NFE/Eisentabel.md"

## Toegankelijkheid

De mate waarin het systeem gebruikt kan worden door mensen met de meest uiteenlopende eigenschappen en mogelijkheden om een gespecificeerd doel te bereiken in een gespecificeerde gebruikscontext.

Als standaard voor toegankelijkheid hanteert de Nederlandse overheid de Web Content Accessibility Guidelines (WCAG), zie [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/). Officieel gebruikt de Nederlandse Overheid versie 2.1, maar het gebruik van versie 2.2 wordt [aangeraden](https://www.digitaleoverheid.nl/nieuws/nieuwe-aanbevolen-standaard-digitale-toegankelijkheid/).

Van WCAG versie 2.2 is op het moment nog geen Nederlandse vertaling, wel van versie 2.1, zie [https://www.w3.org/Translations/WCAG22-nl/](https://www.w3.org/Translations/WCAG21-nl/).

Conform de EN 301 549, hanteert {opdrachtgevende organisatie} de succescriteria voor niveau A en AA als eisen.

| Nr. | Eis                                                                 | Prio   | Rationale               | Realisatie in | Realisatie door | Bewijs              |
| :--- | :------------------------------------------------------------------ | :----- | :---------------------- | :------------ | :-------------- | :------------------ |
| 1   | De applicatie voldoet aan de WCAG2.2 succescriteria, niveau A en AA | {prio} | Wettelijke verplichting | {software}    | ICTU            | Axe-core rapportage |

Onderstaande tabel bevat de WCAG2.2 succescriteria. {Verwijder de AAA-succescriteria indien gewenst.} Per succescriterium is aangegeven of Axe-core, en zo ja met welke regels, het criterium geautomatiseerd kan controleren. {Geef aan of de succescriteria die Axe-core niet geautomatiseerd kan controleren wel of niet met de hand zullen worden gecontroleerd.}

Merk op dat de [Axe-core regels die als "experimenteel" zijn gemarkeerd](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md#experimental-rules) niet standaard door Axe-core worden getest. Zie de [Axe-core API-documentatie](https://www.deque.com/axe/core-documentation/api-documentation/#options-parameter) voor instructies hoe dit aan te passen.

#include "Content/Templates/NFE/WCAG-Tabel-Gegenereerd.md"

## Taal en leesbaarheid

Naast de aan NEN-ISO/IEC 25010 ontleende hoofdeigenschap bruikbaarheid zijn voor de gebruikskwaliteit van {het product} van belang:

* Taal: welke talen dienen te worden ondersteund.
* Leesbaarheid: teksten moeten makkelijk te lezen zijn. Korte zinnen hebben de voorkeur. Hoe gemakkelijker de zin en de woorden, hoe beter de leesbaarheid.

| Nr. | Eis                                            | Prio   | Rationale                                                                                                            | Realisatie in | Realisatie door | Bewijs   |
| :--- | :--------------------------------------------- | :----- | :------------------------------------------------------------------------------------------------------------------- | :------------ | :-------------- | :------- |
| 1   | De applicatie gebruikt maximaal taalniveau B1  | {prio} | [Aanbevolen richtlijn](https://www.communicatierijk.nl/vakkennis/rijkswebsites/aanbevolen-richtlijnen/taalniveau-b1) | {software}    | {partij}        | {bewijs} |
| 2   | De applicatie ondersteunt {ondersteunde talen} | {prio} | {rationale}                                                                                                          | {software}    | ICTU            | {bewijs} |

# Betrouwbaarheid

De mate waarin een systeem, product of component gespecificeerde functies uitvoert onder gespecificeerde condities gedurende een gespecificeerde hoeveelheid tijd.

## Volwassenheid

De mate waarin het systeem onder normale condities de betrouwbaarheidsnormen haalt.

#include "Content/Templates/NFE/Eisentabel.md"

## Beschikbaarheid

De mate waarin het systeem operationeel en toegankelijk is wanneer men het wil gebruiken.

#include "Content/Templates/NFE/Eisentabel.md"

## Foutbestendigheid

De mate waarin het systeem werkt zoals bedoeld ondanks de aanwezigheid van hard- of software-fouten.

#include "Content/Templates/NFE/Eisentabel.md"

## Herstelbaarheid

De mate waarin het systeem, in geval van een onderbreking of bij een fout, de direct betrokken gegevens kan herstellen en het systeem in de gewenste staat kan terug brengen.

#include "Content/Templates/NFE/Eisentabel.md"

# Beveiligbaarheid

De mate waarin een product of systeem informatie en gegevens beschermt zodat personen, andere producten of systemen de juiste mate van gegevenstoegang hebben passend bij hun soort en niveau van autorisatie.

## BIO- en SSD-eisen

De overheid is gebonden aan kaderstelling op het gebied van informatiebeveiliging, zoals de Baseline Informatiebeveiliging Overheid (BIO). Handvatten zoals Secure Software Development (SSD) van het Centrum Informatiebeveiliging en Privacybescherming dienen als leidraad voor het veilig ontwikkelen van software die het voldoen aan de BIO ondersteunt. De BIO is een toepassing van de NEN-ISO/IEC 27001:2017 en de NEN-ISO/IEC 27002:2017 op het domein van de Nederlandse overheid. Voor de Rijksoverheid zijn in die toepassing het Voorschrift Informatiebeveiliging Rijksdienst 2007 (VIR 2007) en het Besluit Voorschrift Informatiebeveiliging Rijksdienst Bijzondere Informatie 2013 (VIRBI 2013) verwerkt.

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
| 15   | (Web)applicatie voorkomen de mogelijkheid van dynamische file includes. Indien gebruik gemaakt wordt van een applicatieserver sluit de serverconfiguratie file includes uit. Mocht het niet mogelijk zijn aan hieraan te voldoen, dan wordt voor de includes gebruik gemaakt van een vertrouwde locatie en een expliciete whitelist voor de files                                                                                                                                                                                                                                                                                                                                                                                                                                                          | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 16   | Applicaties hebben geen run-time afhankelijkheid van externe codebronnen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
| 17   | Applicaties zijn gemaakt met de op het moment van uitleveren meest recente en/of door de leverancier aanbevolen versies van externe bibliotheken, raamwerken of andersoortige bouwblokken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | {prio} | {rationale}                                                                                                                                                                                                                                        | {software, hardware, combinatie} | {partij}        | {bewijs}                         |
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

## Vertrouwelijkheid

De mate waarin een product of systeem ervoor zorgt dat gegevens alleen toegankelijk zijn voor diegenen die geautoriseerd zijn.

#include "Content/Templates/NFE/Eisentabel.md"

## Integriteit

De mate waarin een systeem, product of component ongeautoriseerde toegang tot of aanpassing van computerprogramma’s of gegevens verhindert.

#include "Content/Templates/NFE/Eisentabel.md"

## Onweerlegbaarheid

De mate waarin kan worden bewezen dat acties of gebeurtenissen plaats hebben gevonden, zodat later deze acties of gebeurtenissen niet ontkend kunnen worden.

#include "Content/Templates/NFE/Eisentabel.md"

## Verantwoording

De mate waarin acties van een entiteit getraceerd kunnen worden naar die specifieke entiteit.

#include "Content/Templates/NFE/Eisentabel.md"

## Authenticiteit

De mate waarin bewezen kan worden dat de identiteit van een onderwerp of bron is zoals wordt beweerd.

#include "Content/Templates/NFE/Eisentabel.md"

# Onderhoudbaarheid

De mate waarin een product of systeem effectief en efficiënt gewijzigd kan worden door de aangewezen beheerders

## Modulariteit

De mate waarin het systeem opgebouwd is uit losstaande componenten zodat wijzigingen van een component minimale impact heeft op andere componenten.

#include "Content/Templates/NFE/Eisentabel.md"

## Herbruikbaarheid

De mate waarin een bestaand onderdeel gebruikt kan worden in meer dan één systeem of bij het bouwen van een nieuw onderdeel.

#include "Content/Templates/NFE/Eisentabel.md"

## Analyseerbaarheid

De mate waarin het mogelijk is om effectief en efficiënt de impact, van een geplande verandering van één of meer onderdelen, op een product of systeem te beoordelen, om afwijkingen en/of foutoorzaken van een product vast te stellen of om onderdelen te identificeren die gewijzigd moeten worden.

#include "Content/Templates/NFE/Eisentabel.md"

## Wijzigbaarheid

De mate waarin een product of systeem effectief en efficiënt gewijzigd kan worden zonder fouten of kwaliteitsvermindering tot gevolg.

#include "Content/Templates/NFE/Eisentabel.md"

## Testbaarheid

De mate waarin effectief en efficiënt testcriteria vastgesteld kunnen worden voor een systeem, product of component en waarin tests uitgevoerd kunnen worden om vast te stellen of aan die criteria is voldaan.

#include "Content/Templates/NFE/Eisentabel.md"

# Overdraagbaarheid

De mate waarin een systeem, product of component effectief en efficiënt overgezet kan worden van één hardware, software of andere operationele of gebruiksomgeving naar een andere.

## Aanpasbaarheid

De mate waarin een product of systeem effectief en efficiënt aangepast kan worden voor andere of zich ontwikkelende hardware, software of andere operationele of gebruiksomgevingen.

#include "Content/Templates/NFE/Eisentabel.md"

## Installeerbaarheid

De mate waarin het product of het systeem effectief en efficiënt geïnstalleerd of verwijderd kan worden in een gespecificeerde omgeving.

#include "Content/Templates/NFE/Eisentabel.md"

## Vervangbaarheid

De mate waarin een product een ander specifiek softwareproduct, met hetzelfde doel in de zelfde omgeving, kan vervangen.

#include "Content/Templates/NFE/Eisentabel.md"
