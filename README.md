# ICTU Kwaliteitsaanpak Softwareontwikkeling

| Disclaimer |
| ----------- |
| [ICTU's Kwaliteitsaanpak](https://www.ictu.nl/kwaliteitsaanpak) is a set of guidelines used at [ICTU](https://www.ictu.nl) for software development projects. It is only available in Dutch as is this readme.md.|

**Inhoudsopgave**
- [Over de Kwaliteitsaanpak](#over-de-kwaliteitsaanpak)
- [Werking van deze software](#werking-van-deze-software)
  - [Indeling](#indeling)
  - [Structuur van Richtlijnen](#structuur-van-richtlijnen)
  - [Documentdefinities](#documentdefinities)
- [Bijdragen](#bijdragen)
  - [Vereisten](#vereisten)
  - [Stappen](#stappen)
  - [Een nieuwe versie van de documentatie uitbrengen](#een-nieuwe-versie-van-de-documentatie-uitbrengen)
- [Contact](#contact)

## Over de Kwaliteitsaanpak
De ICTU Kwaliteitsaanpak is een set van maatregelen voor softwareontwikkelprojecten om de kans op een succesvol project te vergroten.
De werkwijze van ICTU is hierdoor openbaar en een open bron voor andere organisaties die (delen) van deze aanpak willen toepassen.

De ICTU Kwaliteitsaanpak en bijbehorende documentsjablonen, de controlelijst en gidsen zijn beschikbaar via [https://ictu.github.io/Kwaliteitsaanpak](https://ictu.github.io/Kwaliteitsaanpak).

## Werking van deze software
### Indeling
Deze repository bevat de bronbestanden die door middel van scripts de Markdown-bestanden omzetten in:
- **HTML** (voor het hoofddocument).
- **DOCX** (voor sjablonen).
- **XLSX** (voor de checklist).

### Structuur van Richtlijnen
Voor elke richtlijn:
1. Maak een map aan in `./Content/Maatregelen`.
2. Voeg twee bestanden toe:
   - `Definitie.md`: Een korte alinea met de definitie van de richtlijn.
   - `Maatregel.md`: Titel, beschrijving en onderbouwing van de richtlijn.
3. Voeg de richtlijn toe aan de documentstructuur in `./DocumentDefinitions/Kwaliteitsaanpak/ICTU-Kwaliteitsaanpak.md`.

### Documentdefinities
Elke documentdefinitie bevindt zich in een submap van `./DocumentDefinitions` en bestaat uit:
- `document.json`: Metadata over het document.
- `document.md`: Inhoud van het document.
- `document.css`: Stijlen voor het document.
- `cover.css`: Stijlen voor de cover.

Gedeeld materiaal (zoals headers, footers en stylesheets) staan in `./DocumentDefinitions/Shared`.

## Bijdragen
### Vereisten
- [Docker](https://www.docker.com/) geïnstalleerd op je systeem.

### Stappen
1. Clone deze repository.
   ```bash
   git clone https://github.com/ICTU/Kwaliteitsaanpak.git
   cd Kwaliteitsaanpak
   ```
2. Genereer de documentatie.
   Met het starten van de containers wordt direct de documentatie gegenereerd.
   ```bash
   docker compose up
   ```
3. Open de gegenereerde documentatie.
   ```bash
   open docs/index.html
   ```
In de bovenste sectie staat de meest recente release.
In de sectie 'onderhanden werk' staat alles in de `wip`-map. Lokale wijzigingen worden ook weergeven onder 'onderhanden werk'.

⚠️ Wijzigingen (ook aan de software) moeten worden gedocumenteerd in `./Content/Wijzigingsgeschiedenis.md`.

### Een nieuwe versie van de documentatie uitbrengen
1. Maak een release branch:
   ```bash
   git checkout -b release-vx.y.z
   ```
2. Werk het versienummer en releasedatum bij in `./Content/Wijzigingsgeschiedenis.md`.
3. Maak een nieuwe map voor de release in `./docs` en voeg deze toe aan versiebeheer:
   ```bash
   mkdir docs/vx.y.z
   git add docs
   ```
4. Werk het versienummer bij in `docs/index.html` en `pyproject.toml`.
5. Genereer de documentatie met het nieuwe versienummer:
   ```bash
   VERSION=x.y.z docker compose up
   ```
6. Commit en push de wijzigingen:
   ```bash
   git commit -a -m "Release vx.y.z"
   git push
   ```
7. Review en merge de branch op GitHub.
8. Tag de release en push de tag naar GitHub:
   ```bash
   git checkout master
   git pull -p
   git tag vx.y.z
   git push --tags
   ```
9. Kondig de release aan in het MS Teams-kanaal **"ICTU Softwareontwikkeling/Algemeen"**.
   - Bij een **minor release**: stuur ook een e-mail naar de SDM'ers.
   - Bij een **major release**: stuur een e-mail naar iedereen bij ISE.

## Contact
Voor vragen over de Kwaliteitsaanpak of deze repository, neem contact op met:
- [Sebastiaan Koot 📧](mailto:sebastiaan.koot@ictu.nl)
- [Frank Niessink 📧](mailto:frank.niessink@ictu.nl)
