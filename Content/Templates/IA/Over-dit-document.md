## Over dit document

De infrastructuurarchitectuur (IA) heeft als doel om een globaal overzicht te geven van de technische infrastructuur van {het product}. Hierbij is er vanuit gegaan dat de oplossing ten minste {aantal} jaar conform specificaties kan functioneren. In de praktijk is een kortere of langere periode mogelijk.

Onder infrastructuur wordt verstaan het samenstel van alle generieke off-the-shelf ICT-componenten die nodig zijn om de applicatie te kunnen installeren, operationeel te maken en houden. De infrastructuur eindigt daar waar specifieke elementen (code) en applicatiespecifieke configuraties ontstaan. Concreet omvat de infrastructuur:

* Housing (locatie, gebouw, racks, stroom, koeling, bekabeling, brandbeveiliging, etc.),
* Hardware (harddisk, SAN, servers, netwerkswitches, proxy’s, load balancers, HSMs, etc.),
* Virtuals (virtual cpu, virtual memory, virtual disk, virtual servers, virtual network, etc.),
* Standaardsoftware/middleware (operating system, webserver, applicatieserver, databaseserver, messaging- en ontwikkelplatform, etc.).

Dit document beschrijft de lagen van de hardware en virtuals op het niveau van globale settings, netwerkarchitectuur en guidelines. Er zal dus niet op technisch detailniveau worden ingegaan op instellingen van routers, firewalls, virtualisatie en (virtuele) servers.

Waar in dit document gesproken wordt van infrastructuurarchitectuur (IA) mag ook high level design (HLD) gelezen worden.
