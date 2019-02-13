#### ICTU

ICTU hanteert de volgende documenten, templates en documentstandaarden voor softwarerealisatieprojecten:

- De beschrijving van niet-functionele eisen is gebaseerd op ISO (International Organization for Standardization)-25010, de Wbni (Wet beveiliging netwerk- en informatiesystemen), de BIR (Baseline Informatiebeveiliging Rijksdienst), de methode Grip op SSD (Secure software development) van het CIP (Centrum Informatiebeveiliging en Privacybescherming), en de Web Content Accessibility Guideliens (WCAG) versie 2.1, niveau A en AA. De beschrijving bevat een prioritering van de niet-functionele eisen. De beschrijving van niet-functionele eisen is gebaseerd op het ICTU NFE (Niet-functionele eisen)-template. De beschrijving bevat in ieder geval eisen aan toegangsbeveiliging, aan beheerfuncties, aan logging en aan het gewenste gedrag van de software bij uitval van infrastructurele diensten, zoals een log-server;

- Overheidsorganisaties moeten een toegankelijkheidsverklaring op hun websites plaatsen. Indien gewenst ondersteunt ICTU bij het opstellen van de toegankelijkheidsverklaring;

- De beschrijving van functionele eisen bestaat uit een geprioriteerde backlog met epics en/of user stories. De beschrijving bevat in ieder geval eisen voor (ondersteuning van) beheerfuncties die door de beoogd beheerder gesteld worden en voor logging, inclusief de (globale) inhoud van te loggen business events (gebeurtenissen op procesniveau) en de daarvoor geldende bewaartermijnen;

- De ontwerp- en architectuurdocumentatie bestaat uit een PSA (Projectstartarchitectuur), een SAD (Softwarearchitectuurdocument), een IA (Infrastructuurarchitectuur), een GFO (Globaal functioneel ontwerp) bijvoorbeeld in de vorm van use cases, en een prototype en/of interactieontwerp. De architectuurdocumenten moeten expliciet inzichtelijk maken hoe aan de niet-functionele eisen wordt voldaan door uit te werken welke oplossingen en mechanieken gekozen zijn, bijvoorbeeld voor identificatie, authenticatie, autorisatie, concurrency, transactionele verwerking of logging;

- De testdocumentatie bestaat uit een mastertestplan, gemaakt op basis van een PRA (Productrisicoanalyse). Beveiligingstesten zijn een integraal onderdeel van het mastertestplan en worden als zodanig afgestemd met de opdrachtgever;

- Het informatiebeveiligingsplan is gebaseerd op een dreigingen- en kwetsbaarhedenanalyse (TVA (Threat and vulnerability assessment)) en bevat een maatregelenselectie informatiebeveiliging. De TVA wordt tijdens de voorfase opgesteld op basis van de resultaten van de BIA, de eventuele PIA en inhoud van de ontwerp- en architectuurdocumentatie. Een TVA levert een deel van een traceerbare onderbouwing voor de te treffen beveiligingsmaatregelen;

- Het vrijgaveadvies bevat ten minste alle nog openstaande testbevindingen en geconstateerde beveiligingsbevindingen. Zie ook [M26: Periodieke beoordeling informatiebeveiliging](#periodieke-beoordeling-informatiebeveiliging-m26-) en [M16: Verplichte tools](#verplichte-tools-m16-). Indien er beveiligingsissues zijn, zijn deze voorzien van een beschreven voorziene impact.

- De deploymentdocumentatie bevat informatie over de eisen die een applicatie stelt aan een omgeving en de stappen die nodig zijn om de applicatie in die omgeving veilig te installeren en configureren. De documentatie bevat daartoe onder meer aanwijzingen voor de HTTP-header en -request-configuratie van de webserver en voor het verwijderen van overbodige header-informatie zoals de 'Server'-header. Ook zijn er aanwijzingen voor veilige configuratie(s) van (externe) toegang tot de beheerinterface. De documentatie bevat daarnaast in ieder geval een beschrijving van de protocollen en services die de applicatie aanbiedt, de protocollen, services en accounts die het product gebruikt en de protocollen, services en accounts die de applicatie gebruikt voor beheer;

Zie de bijlage [Documenten voor M01: Op te leveren producten](#documenten-voor-m01-op-te-leveren-producten) voor een uitgebreider overzicht van de documenten en documentstandaarden die ICTU hanteert voor softwarerealisatieprojecten.

Het genoemde onderzoek voert ICTU uit als onderdeel van een "due diligence". Een due diligence wordt uitgevoerd in samenwerking met een potentiële opdrachtgever en biedt, naast het genoemde onderzoek, ook de opdrachtgever de kans zich een oordeel te vormen over de werkwijze van ICTU en de verwachte samenwerking.
