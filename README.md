# ICTU Kwaliteitsaanpak Softwareontwikkeling

| Disclaimer |
| ----------- |
| [ICTU's Kwaliteitsaanpak](https://ictu.github.io/Kwaliteitsaanpak) is a set of guidelines used at [ICTU](https://www.ictu.nl/kwaliteitsaanpak) for software development projects. It is only available in Dutch as is this readme.md.|

**Inhoudsopgave**
- [Over de Kwaliteitsaanpak](#over-de-kwaliteitsaanpak)
- [Werking van deze software](#werking-van-deze-software)
  - [Indeling](#indeling)
  - [Mappenstructuur](#mappenstructuur)
  - [Structuur van Richtlijnen](#structuur-van-richtlijnen)
  - [Documentdefinities](#documentdefinities)
- [Bijdragen](#bijdragen)
  - [Vereisten](#vereisten)
  - [Stappen](#stappen)
  - [Een nieuwe versie van de documentatie uitbrengen](#een-nieuwe-versie-van-de-documentatie-uitbrengen)
- [Contact](#contact)

## Over de Kwaliteitsaanpak
De ICTU Kwaliteitsaanpak is een set van maatregelen voor softwareontwikkelprojecten om de kans op een succesvol project te vergroten.
De werkwijze van ICTU is hierdoor openbaar en een open bron voor andere organisaties die (delen van) deze aanpak willen toepassen.

De ICTU Kwaliteitsaanpak en ondersteunende documenten zijn beschikbaar via [https://ictu.github.io/Kwaliteitsaanpak](https://ictu.github.io/Kwaliteitsaanpak).

## Werking van deze software
### Indeling
Deze repository bevat de bronbestanden die door middel van scripts de Markdown-bestanden omzetten in:
- **HTML** (voor het hoofddocument).
- **DOCX** (voor sjablonen).
- **XLSX** (voor de checklist).

### Mappenstructuur
De repository is als volgt opgebouwd:
- **`build`**: Tijdelijke map voor tussenresultaten tijdens het genereren van de documentatie.
- **`ci`**: Bevat shellscripts die de kwaliteitscontroles en unittests aansturen.
- **`Content`**: Bevat alle bronteksten in Markdown waarmee de eindproducten worden gegenereerd.
- **`docs`**: Bevat de gegenereerde documentatie, zoals HTML-, DOCX- en XLSX-bestanden. Alle documentatie is hier ingedeeld op release; historische versies van de Kwaliteitsaanpak zijn hier terug te vinden.
- **`DocumentDefinitions`**: Bevat de definitiebestanden voor documenten, zoals metadata, inhoud en stijlen.
- **`src`**: Bevat de broncode voor de scripts die de documentatie genereren.
- **`tests`**: Bevat tests voor de software.
- **`thirdparty/WCAG`**: Externe afhankelijkheden of tools die worden gebruikt in het project

### Structuur van Richtlijnen
Voor elke nieuwe richtlijn:
1. Maak een map aan in `./Content/Maatregelen`.
2. Voeg twee bestanden toe:
   - `Definitie.md`: Een korte alinea met de definitie van de richtlijn.
   - `Maatregel.md`: Titel, beschrijving en onderbouwing van de richtlijn.
3. Voeg de richtlijn toe aan de documentstructuur in `./DocumentDefinitions/Kwaliteitsaanpak/ICTU-Kwaliteitsaanpak.md`.

### Documentdefinities
Een documentdefinitie is een [JSON](https://nl.wikipedia.org/wiki/JSON)-bestand dat per bron beschrijft waar deze zich bevindt en in welk formaat deze moet worden omgezet en met welke stijl en opmaak.

Elke documentdefinitie bevindt zich in een submap van `./DocumentDefinitions` en bestaat uit:
- `[documenttype].json`: Metadata over het document.
- `[pagina].md`: De pagina waarin de verschillende bronbestanden worden geïmporteerd (door middel van #include).
- `Shared/[document].css`: Stijlen voor het betreffende document.

Gedeeld materiaal (zoals headers, footers en stylesheets) staat in `./DocumentDefinitions/Shared`.

Zie [DocumentDefinitions/README.md](DocumentDefinitions/README.md) voor meer informatie.

## Bijdragen
### Vereisten
- [Docker](https://www.docker.com/) geïnstalleerd op je systeem.

### Stappen
Voer de volgende stappen uit om de resultaatbestanden lokaal te genereren.
1. Clone deze repository:
   ```bash
   git clone https://github.com/ICTU/Kwaliteitsaanpak.git
   cd Kwaliteitsaanpak
   ```
2. Genereer de documentatie:
   ```bash
   docker compose up
   ```
   Wanneer het proces succesvol is verlopen wordt de container vanzelf afgesloten. De terminal geeft dan iets weer als `ka-1 exited with code 0`. De gegenereerde documenten staan in de map `docs/wip` (work-in-progress).

⚠️ Documenteer wijzigingen (alleen aan de inhoud van de Kwaliteitsaanpak) in `./Content/Wijzigingsgeschiedenis.md`.

### Een nieuwe versie van de documentatie uitbrengen
1. Bepaal het nieuwe versienummer. Zie https://ictu.github.io/Kwaliteitsaanpak/v5.2.0/ICTU-Kwaliteitsaanpak.html#versionering

2. Maak een release branch:
   ```bash
   git checkout -b release-vx.y.z
   ```
3. Werk het versienummer en de releasedatum bij in `./Content/Wijzigingsgeschiedenis.md`.

4. Maak een nieuwe map voor de release in `./docs` en voeg deze toe aan versiebeheer:
   ```bash
   mkdir docs/vx.y.z
   git add docs
   ```
5. Werk het versienummer bij in `docs/index.html` en `pyproject.toml`.
6. Genereer de documentatie met het nieuwe versienummer:
   ```bash
   VERSION=x.y.z docker compose up
   ```
   De gegenereerde documenten staan in de map `docs/vx.y.z`.
7. Commit en push de wijzigingen:
   ```bash
   git commit -a -m "Release vx.y.z"
   git push
   ```
8. Review en merge de branch op GitHub.
9. Tag de release en push de tag naar GitHub:
   ```bash
   git checkout master
   git pull -p
   git tag vx.y.z
   git push --tags
   ```
10. Kondig de release aan in het MS Teams-kanaal **"ICTU Softwareontwikkeling/Algemeen"**.
   - Bij een **minor release**: stuur ook een e-mail naar de SDM'ers.
   - Bij een **major release**: stuur een e-mail naar iedereen bij ISE.

## Contact
Voor vragen over de Kwaliteitsaanpak of deze repository, neem contact op met:
- [Sebastiaan Koot 📧](mailto:sebastiaan.koot@ictu.nl)
- [Frank Niessink 📧](mailto:frank.niessink@ictu.nl)
