## Wijzigingsgeschiedenis

### Versie 2.5.0, nog te releasen

#### Kwaliteitsaanpak

* HTML-versie van de Kwaliteitsaanpak toegevoegd als toegankelijk alternatief voor de PDF-versie.
* Op meerdere plekken in de Kwaliteitsaanpak de gebruikte rollen aangescherpt of verbeterd door bijvoorbeeld ICTU te vervangen door project, team door Scrumteam en projectleider door software delivery manager.
* Bij maatregel "Het project levert in elke fase vastgestelde producten en informatie op" (M01): software bill of materials toegevoegd als op te leveren informatie.
* Bij maatregel "Het project gebruikt tools voor vastgestelde taken" (M16): de lijst van verplichte tools en ondersteunde tools gelijk getrokken, de genoemde tools bijgewerkt en software bill of materials toegevoegd als taak.
* Bij maatregel "Het project voert periodiek een self-assessment uit ten aanzien van de Kwaliteitsaanpak" (M28): de rol van de kwaliteitsmanager bij het uitvoeren van de self-assessment toegevoegd.
* Nieuwe maatregel "ICTU organiseert periodiek een gezamenlijke self-assessment ten aanzien van de Kwaliteitsaanpak" (M33) toegevoegd.
* Nieuwe maatregel "Het project draagt software beheerst over" (M34) toegevoegd.
* De term 'standup' vervangen door de officiële term 'Daily Scrum'.
* Kruisverwijzingen tussen maatregelen verwijderd om de onderhoudbaarheid van de tekst te vergroten.

#### Template Niet-Functionele Eisen

* Axe-core bijgewerkt naar versie 4.6 in de tabel met de WCAG 2.1 succescriteria.

### Versie 2.4.0, 12 januari 2022

#### Kwaliteitsaanpak

* De titel van maatregel "Het project levert in elke fase vastgestelde informatie over het product op" (M01) veranderd in "Het project levert in elke fase vastgestelde producten en informatie op" zodat de titel beter past bij de scope van de maatregel.
* Bij maatregel "Het project levert in elke fase vastgestelde producten en informatie op" (M01): de tabel uitgebreid met product backlog, en de lopende tekst aangevuld en aangepast opdat deze consistent is met de tabel.
* Bij maatregel "Het project zorgt dat het product continu aan de kwaliteitsnormen voldoet" (M02): "Ook zorgt het project dat de performance van de software regelmatig wordt getest." toegevoegd.

#### Template Kwaliteitsplan

* Bijlage met periodieke (kwaliteits)controles toegevoegd.
* Beschrijvingen van release notes en performancetest toegevoegd.

#### Template Niet-Functionele Eisen

* Axe-core bijgewerkt naar versie 4.3 in de tabel met de WCAG 2.1 succescriteria.

#### Template Plan van Aanpak Realisatiefase

* UX: aanpassing producten uit de voorfase; verantwoordelijkheden van rol UX-designer aangevuld.
* Toelichting op te maken afspraken voor: release notes, vrijgaveadvies, beveiligingstest, performancetest.
* In hoofdstuk Verwachte inzet ICTU een tabel toegevoegd met te verwachten kosten voor door ICTU te benutten diensten.

#### Template Plan van Aanpak Voorfase

* UX: te realiseren producten toegevoegd: interactie-ontwerp (UX), wireframe, mockup, prototype, animatie.

#### Template Generiek

* Definities toegevoegd: release notes en vrijgaveadvies.

#### Self-assessment checklist

* Invulinstructie uitgebreid.
* Duidelijk gemaakt dat als maatregelen submaatregelen hebben alleen de status van submaatregelen hoeft te worden ingevuld.

#### Inwerkplan Kwaliteitsmanager

* Inwerkplan voor de rol van kwaliteitsmanager toegevoegd.

### Versie 2.3.0, 14 mei 2021

#### Kwaliteitsaanpak

* Verwijzingen naar BIRT en de Releasemanager verwijderd uit de maatregel "Het project gebruikt tools voor vastgestelde taken" (M16) omdat deze tools niet meer ondersteund worden.
* Manifest verwijderd omdat de inhoud grotendeels terugkomt op andere plekken in de Kwaliteitsaanpak.

#### Samenvatting Kwaliteitsaanpak

* Een samenvatting van de Kwaliteitsaanpak als los document toegevoegd.

#### Presentatie Kwaliteitsaanpak

* Een presentatie van de Kwaliteitsaanpak als los document toegevoegd.

#### Alle templates

* Lijst van reviewers toegevoegd aan colofon.
* Leeswijzer uitgebreid met een beschrijving van de (standaard) bijlagen van de templates.
* Hoofdstuk "Managementsamenvatting" toegevoegd.

#### Template Detailtestplan

* Verwijzingen naar BIRT en de Releasemanager verwijderd.

#### Template Globaal Functioneel Ontwerp

* Template aangepast naar het gebruik van use cases om de functionaliteit te beschrijven.
* Kaders die niet relevant waren voor een GFO verwijderd.

#### Template Niet-Functionele Eisen

* Tabel met de WCAG 2.1 succescriteria toegevoegd. Per succescriterium geeft de tabel aan of Axe-core, en zo ja met welke regels, het succescriterium geautomatiseerd kan controleren.

#### Template Kwaliteitsplan

* Het kwaliteitsplantemplate sprak van een verantwoordingsparagraaf in alle documenten, maar deze paragraaf zat niet in de andere templates. Deze verantwoordingsparagrafen waren bedoeld om de eisen traceerbaar te maken. Omdat niet alle projecten dit nodig hebben, en er andere manieren in gebruik zijn om eisen traceerbaar te maken (bijvoorbeeld een losse administratie in Confluence) is de tekst over verantwoordingsparagrafen vervangen door een optionele paragraaf over tracering van eisen die nader kan worden ingevuld.
* Uit de bijlage "Gebruik van Jira" is de paragraaf "Velden in Jira" verwijderd omdat deze out-of-date en incompleet was en bovendien niet ging over velden in Jira, maar over metrieken die met behulp van de informatie in Jira gemeten kunnen worden. In plaats van deze paragraaf verwijst het kwaliteitsplantemplate naar de lijst op GitHub van metrieken die Quality-time kan meten.
* Uit de bijlage "Gebruik van Jira" is het issue type "Sprint bug" verwijderd omdat bugs die tijdens sprints worden gevonden normaal gesproken niet worden vastgelegd in Jira.
* Uit de bijlage "Gebruik van Jira" is het issue type "Custom issue" verwijderd omdat custom issues optioneel zijn en in de praktijk te weinig worden toegepast om apart te beschrijven.
* Het hoofdstuk "Kwaliteitsmaatregelen projectafsluiting" bevatte een lijst van activiteiten voor de software delivery manager. Die activiteiten zijn verplaatst naar het template plan van aanpak realisatiefase. De kwaliteitsmaatregelen bij projectafsluiting zijn beperkt tot een controle door de kwaliteitsmanager van de uitvoering van die activiteiten.

#### Template Plan van Aanpak Voorfase

* Paragraaf over projectafsluiting toegevoegd.

#### Template Plan van Aanpak Realisatiefase

* Paragraaf over projectafsluiting en bijlage met activiteiten voor projectafsluiting toegevoegd.

#### Alle documenten

* Vervang 'privacy impact analyse' door 'privacy impact assessment' en 'business impact analyse' door 'business impact analysis' zodat beide termen consequent op dezelfde manier geschreven worden.

### Versie 2.2.0, 27 januari 2021

#### Kwaliteitsaanpak

* Afdeling ICTU Software Realisatie vervangen door de afdelingen ICTU Software Diensten en/of ICTU Software Expertise.
* ICTU ondersteunt alleen nog Quality-time als kwaliteitssysteem; HQ verwijderd.
* Leeswijzer uitgebreid met uitleg over beschrijvend en voorschrijvend karakter van de Kwaliteitsaanpak.
* Nieuwe maatregel "Het project beschikt over vastgestelde informatie" (M31) toegevoegd die beschrijft welke informatie de opdrachtgever aan een project beschikbaar stelt.
* Bij maatregel "Het project levert in elke fase vastgestelde informatie over het product op" (M01) met een plaatje de relaties tussen de voorfase producten toegelicht.
* De maatregel "Het project is gesplitst in een voorfase en een realisatiefase" (M14) hernoemd naar "Het project bereidt samen met opdrachtgever en belanghebbenden de realisatie voor".
* De maatregel "ICTU geeft de voorkeur aan open source tools" (M15) is verwijderd. De inhoud van M15 is verplaatst naar "ICTU biedt ondersteuning voor verplicht gestelde tools" (M18). Reden is dat de voorkeur voor open source geen apart uitvoerbare maatregel is, maar deel uitmaakt van de ondersteuning van projecten met tools.
* Bij maatregel "Het project gebruikt tools voor vastgestelde taken" (M16) performancetesttools toegevoegd.
* Maatregel "ICTU zorgt dat een aantal vastgestelde tools snel beschikbaar is voor een project" (M17) verwijderd omdat projecten deze tools ofwel via de kantoorautomatisering van ICTU kunnen gebruiken of zelf kunnen draaien in de afgeschermde digitale omgeving zoals beschreven bij M19.
* Bij maatregel "Het project laat de beveiliging van het ontwikkelde product periodiek beoordelen" (M26) beter toegelicht onder welke voorwaarden de beveiligingstesten alleen door de opdrachtgever kunnen worden uitgevoerd.
* Bijlage "Risico's van softwareontwikkeling" verwijderd vanwege de overlap met de bijlage "Relatie met NEN NPR 5326".

#### Template Projectvoorstel Voorfase

* Template veranderd in een template voor een plan van aanpak voor de voorfase. Gebruik voor projectvoorstellen het ICTU-brede template.

#### Template Projectvoorstel Realisatiefase

* Template veranderd in een template voor een plan van aanpak voor de realisatiefase. Gebruik voor projectvoorstellen het ICTU-brede template.

#### Template Kwaliteitsplan

* Toegevoegd bij projectafsluiting dat VPN-keys, LDAP-accounts, Jira-accounts en werkstations moeten worden opgeschoond.
* Bij projectafsluiting de verantwoordelijke rol aangepast naar software delivery manager, conform Maatregel 27 in de Kwaliteitsaanpak.
* Het hanteren van codeerstandaarden toegevoegd aan de kwaliteitsmaatregelen tijdens de realisatiefase.

### Versie 2.1.0, 2 september 2020

#### Kwaliteitsaanpak

* M30 ontbrak in de bijlage met het overzicht van alle maatregelen.
* Link naar Kwaliteitsaanpak op ICTU-website toegevoegd.

#### Alle templates

* Rubriceringsmogelijkheid conform Besluit Voorschrift Informatiebeveiliging Rijksdienst Bijzondere Informatie 2013 (VIRBI 2013) toegevoegd.
* Rubriceringsniveau, rubriceringsduur en totaal aantal bladzijden conform VIRBI 2014, bijlage 1, eis 6J toegevoegd.
* Link naar Kwaliteitsaanpak op ICTU-website toegevoegd in de bijlage over de Kwaliteitsaanpak.

#### Template Projectvoorstel Realisatiefase

* Projectvoorstel Realisatiefase template toegevoegd dat als basis kan dienen voor een projectvoorstel voor het uitvoeren van een realisatiefase aansluitend aan een voorfase.

#### Generiek template

* Generiek template toegevoegd dat als basis kan dienen voor documenten waarvoor nog geen specifiek template is.

#### Template Kwaliteitsplan

* Paragrafen 1.2, 1.5 en 1.6 uitgebreid met standaard teksten.
* Stakeholder management vervangen door het bescheidener identificeren van belanghebbenden en belangen.

#### Template Niet-Functionele Eisen

* Link naar Nederlandse vertaling van WCAG 2.1 toegevoegd aan het NFE-template.

### Versie 2.0.0, 29 april 2020

* Naam van de Kwaliteitsaanpak veranderd van "Kwaliteitsaanpak ICTU Software Realisatie" naar "ICTU Kwaliteitsaanpak Softwareontwikkeling". Waar relevant "softwarerealisatie" veranderd in "softwareontwikkeling".
* Maatregelen, waar mogelijk, compacter geformuleerd.
* Maatregelen herverdeeld over de drie maatregelhoofdstukken.
* De maatregel "Het project levert in elke fase vastgestelde informatie over het product op" (M01) beknopter geformuleerd en toelichting op documenten uitgebreid.
* Bij de maatregelen "Het project zorgt dat het product continue aan de kwaliteitsnormen voldoet" (M02), "Het project maakt technische schuld inzichtelijk en lost deze planmatig op" (M08) en "Het project gebruikt tools voor vastgestelde taken" (M16) naast HQ ook Quality-time vermeld.
* Bij de maatregel "Het project maakt technische schuld inzichtelijk en lost deze planmatig op" (M08) toegevoegd dat projecten regelmatig en voldoende tijd besteden aan het voorkomen en oplossen van technische schuld.
* Bij de maatregel "Het project gebruikt tools voor vastgestelde taken" (M16) versiebeheer toegevoegd, met als concrete tools GitLab en Azure DevOps.
* Explicieter aandacht besteed aan gebruikskwaliteit in de maatregelen "Het project levert in elke fase vastgestelde informatie over het product op" (M01) en "Het project zorgt dat het product continue aan de kwaliteitsnormen voldoet" (M02). ISO 9241-210 opgenomen als standaard die ICTU hanteert voor gebruikskwaliteit.
* De maatregel "Betrokkenheid bij inzet" (M22) verwijderd.
* De maatregel "Implementatie van wijzigingen aan de kwaliteitsaanpak en -normen" (M24) verwijderd.
* Nieuwe maatregel toegevoegd voor het starten van projecten: "ICTU zorgt dat een project verantwoord kan starten" (M29).
* Nieuwe maatregel toegevoegd voor risicomanagement: "Projecten identificeren, mitigeren en bewaken risico's" (M30).
* Termen aangepast: 'projectverantwoordelijke' is vervangen door 'projectleider', 'projectenorganisatie' en 'projectorganisatie' door 'ICTU' en 'realiserend team' door 'projectteam'.
* De beschrijving van de rollen van software delivery manager en kwaliteitsmanager aangescherpt.
* Waar relevant bij de rationale van maatregelen verwezen naar overeenkomende risicobeheersmaatregelen uit de NPR 5326.
* Referenties aan de Baseline Informatiebeveiliging Rijksdienst (BIR) omgezet naar de Baseline Informatiebeveiliging Overheid (BIO).
* Referenties aan tools geactualiseerd.
* Tekstuele en stilistische verbeteringen.
* Actielijst toegevoegd aan self-assessment spreadsheet.
* Generatie van documenttemplates is onderdeel van de Kwaliteitsaanpak.

### Versie 1.3.1, 1 mei 2019

* M14: Maatregeltitel ingekort zodat paginanummers in de inhoudsopgave niet overlappen.

### Versie 1.3, 5 april 2019

* Overbodig kopje in de wijzigingsgeschiedenis van de generieke versie verwijderd.
* Bijlage met afkortingen toegevoegd.
* M07: Toegankelijkheidstests toegevoegd.
* M10: Aanwezigen bij periodiek projectoverleg aangepast.
* M16: Een tool voor het testen van toegankelijkheid toegevoegd.
* M01: Wbni, EN 301 549 en WCAG 2.1 als bron voor niet-functionele eisen toegevoegd. Toegankelijkheidsverklaring als mogelijke deliverable genoemd.
* M05: Iteratief en incrementeel ontwikkelproces: Sprint retrospective en sprint backlog toegevoegd.
* M16: Axe toegevoegd.
* WCAG 2.1 toegevoegd aan bijlage C: Documenten voor M01.

### Versie 1.2, 1 augustus 2018

* M01: Op te leveren producten: Niet alle producten hoeven door het project te worden gemaakt.
* M02: Continu voldoen aan kwaliteitsnormen: Zo snel mogelijk voldoen aan kwaliteitsnormen in plaats van altijd.
* M13: Gebruik van NEN-ISO/IEC 25010: Verduidelijkt dat het om het toepassen van NEN-ISO/IEC 25010 in projecten gaat en verplaatsen naar hoofdstuk Producten.
* M19: Afgeschermde digitale omgeving: De titel van de maatregel verduidelijkt naar "afgeschermde digitale omgeving".
* M25: De inhoud is verplaatst naar M01: Op te leveren producten, M25 zelf is vervallen.
* M28: Self-assessment: Maatregel met betrekking tot self-assessment toegevoegd.
* Tekstuele en stilistische verbeteringen.
* Manifest toegevoegd.
* ICTU-specifieke invulling van maatregelen aangepast aan nieuwe organisatiestructuur en rollen zoals die in 2018 gelden.
* In M16: Verplichte tools, de verwijzing naar ICTU-specifieke SonarQube kwaliteitsprofielen verwijderd omdat ICTU de standaard Sonar Way kwaliteitsprofielen gebruikt.

### Versie 1.1, 7 november 2017

* BIR-maatregelen toegevoegd.

### Versie 1.0.2, 9 mei 2017

* Eerste publicatie.
