# Functionele eisen

Voor {het product} gelden de volgende functionele eisen, geformuleerd in de vorm van epics. Eisen voor het MVP zijn vetgedrukt.

## Hoofdfunctie 1 - {naam hoofdfunctie, bijvoorbeeld: Softwareproducten registreren}

{Introductie op hoofdfunctie 1, bijvoorbeeld: Beheerders kunnen softwareproducten registreren, inclusief de versies die beschikbaar zijn bij de leverancier.}

1. **{Titel epic 1, bijvoorbeeld: Registratie van softwareproducten}**: Als {rol} wil ik {actie} zodat {doel}. {Bijvoorbeeld: Als beheerder wil ik registreren welke softwareproducten ISD beheert zodat ik installaties van het softwareproduct kan registreren.}
1. **{Titel epic 2, bijvoorbeeld: Link naar beschikbare versies vastleggen}**: Als {rol} wil ik {actie} zodat {doel}. {Bijvoorbeeld: Als beheerder wil ik vastleggen via welke URL ik kan vinden wat de beschikbare versies van een softwareproduct zijn zodat ik kan registreren welke versies van het softwareproduct beschikbaar zijn.}
1. **{Titel epic 3, bijvoorbeeld: Beschikbare versies registreren}**: Als {rol} wil ik {actie} zodat {doel}. {Bijvoorbeeld: Als beheerder wil ik registreren welke versies van welke softwareproducten bij de leverancier beschikbaar zijn zodat ik kan zien welke software-installaties bijgewerkt kunnen worden.}
1. {Titel epic 4, bijvoorbeeld: Notificatie over nieuwe versies}: {Bijvoorbeeld: Als beheerder wil ik een notificatie ontvangen als er een nieuwe beschikbare versie van een softwareproduct geregistreerd wordt door een collega zodat ik niet zelf regelmatig hoef te kijken of er nieuwe versies beschikbaar zijn. }

## Hoofdfunctie 2 - {naam hoofdfunctie, bijvoorbeeld: Softwareinstallaties registreren}

{Introductie op hoofdfunctie 2, bijvoorbeeld: Bij installatie van een softwareproduct registreren beheerders welke versie van het softwareproduct op welke apparaat wordt geïnstalleerd. Dat maakt het mogelijk te zien wat waar is geïnstalleerd en de geïnstalleerde versies te vergelijken met de beschikbare versies.}

1. **{Titel epic 1, bijvoorbeeld: Registratie van software-installaties}**: Als {rol} wil ik {actie} zodat {doel}. {Bijvoorbeeld: Als beheerder wil ik registreren dat een versie van een softwareproduct op een apparaat is geïnstalleerd zodat ik kan zien welke versies van welke softwareproducten op welke apparaten zijn geïnstalleerd.}
1. **{Titel epic 2, bijvoorbeeld: Overzicht van software-installaties}**: Als {rol} wil ik {actie} zodat {doel}. {Bijvoorbeeld: Als beheerder wil ik bekijken welke versies van welke softwareproducten op welke apparaten zijn geïnstalleerd zodat ik in het geval van nieuwe bekende beveiligingskwetsbaarheden in bepaalde versies van een softwareproduct kan zien op welke apparaten deze versies van het softwareproduct zijn geïnstalleerd.}
1. **{Titel epic 3, bijvoorbeeld: Geïnstalleerde versies vergelijken met beschikbare versies}**: Als {rol} wil ik {actie} zodat {doel}. {Bijvoorbeeld: Als beheerder wil ik de versies van software-installaties vergelijken met de beschikbare versies van de softwareproducten zodat ik kan bepalen of ik een software-installatie kan bijwerken.}

## Hoofdfunctie 3 - {naam hoofdfunctie}

{Vul aan}

# Niet-functionele eisen

Onderstaande niet-functionele eisen zijn van toepassing op {het product}:

1. De oplossing is in het Nederlands omdat {rationale}.
1. De oplossing is compatible met {andere software}.
1. De oplossing wordt open source ter beschikking gesteld via {bijvoorbeeld: GitHub en PyPI (Python Package Index)}.
1. De oplossing voldoet aan de A- en AA-eisen uit WCAG 2.2.
5. De oplossing ondersteunt {...}.

{Vul aan.}

# Softwarearchitectuur

## Applicatiecontext

{Beschrijf in deze paragraaf de technische context waarbinnen de applicatie zal opereren. Denk aan omliggende systemen, authenticatie, logging en backup. Als deze informatie al in een ander document beschreven staat kan daarnaar verwezen worden uiteraard.}

## Datamodel

Het datamodel voor {het product} moet de hieronder beschreven entiteiten ondersteunen.

### Entiteit 1 - {naam entiteit, bijvoorbeeld: Softwareproduct}

{Omschrijving van de entiteit, attributen en relaties. Bijvoorbeeld: Een softwareproduct is een applicatie, firmware of besturingssysteem dat geïnstalleerd kan worden op een apparaat. Softwareproducten hebben een naam, een omschrijving en een lijst van tags. Softwareproducten hebben (net als device types) een manufacturer. Softwareproducten hebben een link naar een pagina op een website van de manufacturer met beschikbare versienummers. Softwareproducten hebben nul of meer versies.}

### Entiteit 2 - {naam entitieit, bijvoorbeeld: Softwareinstallatie}

{Omschrijving van de entiteit, attributen en relaties. Bijvoorbeeld: Een software-installatie is een softwareproduct dat geïnstalleerd is op één specifiek apparaat. Software-installaties hebben een versie, een installatiedatum, een commentaarveld en een lijst van tags. In NetBox kunnen devices services bevatten (services zijn combinaties van protocol en poortnummers en optioneel IP-adressen). Voor softwareproducten ondersteunen we geen services. Gebruikers kunnen bij installatie alleen versienummers invoeren die bij het softwareproduct voorkomen als beschikbaar versienummer.}

### Entiteit 3 - {naam entiteit}

{Vul aan}

## Componenten

{Beschrijf de belangrijkste componenten van het product. Denk aan database, webserver/services, models en views.}

## Koppelingen

{Beschrijf met welke systemen het product communiceert, welke informatie wordt uitgewisseld en welke protocollen en standaarden daarbij van toepassing zijn.}

## Deployment

{Beschijf hoe en waar het product zal worden gedeployed. Besteed eventueel ook aandacht aan migratie.}

## Implementatie

{Beschrijf programmeertaal en technologiestack voor de implementatie.}

# Testaanpak

{Beschrijf de testaanpak in termen van testsoorten, testtools, testomgevingen en betrokkenen.}

# Plan van aanpak

{Beschrijf beoogde resultaten, scope, werkwijze, planning, doorlooptijd en samenstelling van het team.}

De volgende activiteiten zijn nodig voor het ontwikkelen van de MVP van {het product}:

| Nr.  | Activiteit                                           | Dagen |
|:-----|:-----------------------------------------------------|------:|
| A01  | {Activiteit 1, bijvoorbeeld: Voorbereiding}          |   {X} |
| A02  | {Activiteit 2, bijvoorbeeld: Realisatie}             |   {X} |
| A03  | {Activiteit 3, bijvoorbeeld: Toegankelijkheidstoets} |   {X} |
| A{X} | {Activiteit X}                                       |   {X} |
|      | Totaal                                               |   {X} |

Uitgangspunt is dat alle activiteiten door {X} ontwikkelaar(s) worden uitgevoerd en dat {activiteiten X en Y, bijvoorbeeld de daadwerkelijke uitrol naar de productieomgeving} buiten scope van dit plan van aanpak zijn.

Er zijn {X} eisen geïdentificeerd die buiten de scope van het MVP vallen (eisen {Y en Z}). De schatting nu is dat het realiseren van deze eisen {X} dagen extra zal kosten, maar uiteraard is een veel betere schatting mogelijk na realisatie van het MVP.
