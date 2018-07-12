### Continuous delivery pipeline (M07)

Er is een geautomatiseerde continuous delivery pipeline die aantoonbaar correct werkt en ten minste de volgende activiteiten uitvoert:

- bouw van de software,
- unit tests,
- regressietests,
- kwaliteitscontroles,
- performancetests (*),
- beveiligingstests (*),
- installatie van de software,
- oplevering van het totale product, dus inclusief alle deliverables, in de vorm zoals bruikbaar voor en afgesproken met de opdrachtgever.

(*) Idealerwijs voert de geautomatiseerde continuous delivery pipeline ook performance tests en beveiligingstests uit. Vanwege de doorlooptijden van tests (met name van duurtesten) en licenties van testtools is dat niet altijd haalbaar. In dat geval vinden de performance tests en beveiligingstests periodiek en zo vaak mogelijk plaats, bij voorkeur dagelijks.

De projectenorganisatie voorziet in mensen en hulpmiddelen, zodat projecten deze pipeline kunnen toepassen. Projecten zijn verantwoordelijk voor de correcte werking van de pipelin.

#### Rationale

Software incrementeel opleveren (zie [M05: Iteratief en incrementeel ontwikkelproces](#iteratief-en-incrementeel-ontwikkelproces-m05-)) vereist dat de software frequent gebouwd, getest en opgeleverd kan worden. Om dit efficiënt en foutvrij te doen, dient het proces van bouwen, testen en opleveren geautomatiseerd te zijn; een continuous delivery pipeline faciliteert dit.
