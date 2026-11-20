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
Deze repository bevat scripts die Markdown-bronbestanden (content) omzetten in onderstaande uitvoerformaten.
- **HTML** (voor het hoofddocument).
- **DOCX** (voor sjablonen).
- **XLSX** (voor de checklist).
- **PPTX** (voor de Kwaliteitsaanpak).

### Mappenstructuur
De repository is als volgt opgebouwd:
- **`build`**: Tijdelijke map voor tussenresultaten tijdens het genereren van de documentatie.
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
- `[pagina].md`: De pagina met de voorpagina van het document, waarin de verschillende bronbestanden worden geïmporteerd (door middel van #include).
- `Shared/[document].css`: Stijlen voor het betreffende document.

Gedeeld materiaal (zoals headers, footers en stylesheets) staat in `./DocumentDefinitions/Shared`.

Zie [DocumentDefinitions/README.md](DocumentDefinitions/README.md) voor meer informatie.

## Bijdragen
### Vereisten
- [uv](https://docs.astral.sh/uv/) geïnstalleerd op je systeem.
- [just](https://just.systems) geïnstalleerd op je systeem. De `justfile` bevat recipes voor het installeren van de dependencies, het genereren van de documentatie, het uitvoeren van de unittests en kwaliteitscontroles en het opruimen van gegenereerde bestanden. Voer `just` uit voor een overzicht van de beschikbare recipes.
- [Node.js](https://nodejs.org/) geïnstalleerd op je systeem, voor het renderen van diagrammen.

### Stappen
Voer de volgende stappen uit om de resultaatbestanden lokaal te genereren.
1. Clone deze repository:
   ```console
   git clone https://github.com/ICTU/Kwaliteitsaanpak.git
   cd Kwaliteitsaanpak
   ```
2. Installeer de dependencies:
   ```console
   just install
   ```
3. Genereer de documentatie:
   ```console
   just make
   ```
   De gegenereerde documenten staan in de map `docs/wip` (work-in-progress).

   Om een specifiek document te genereren, geef alleen het desbetreffende JSON-bestand. Bijvoorbeeld:
   ```console
   just make DocumentDefinitions/wijzigingsgeschiedenis.json
   ```

   Om meer voortgangsinformatie te krijgen, roep het conversiescript direct aan en verander het loggingniveau:
   ```console
   uv run src/convert.py --log INFO DocumentDefinitions/*.json
   ```
4. Voer de unittests en kwaliteitscontroles uit:
   ```console
   just test
   just check
   ```
   De kwaliteitscontroles controleren ook de links in de gegenereerde documenten in de map `build`; genereer de documenten dus eerst.

   Verwijder gegenereerde bestanden en caches met:
   ```console
   just clean
   ```

⚠️ Documenteer wijzigingen (alleen aan de inhoud van de Kwaliteitsaanpak) in `./Content/Wijzigingsgeschiedenis.md`.

### Een nieuwe versie van de Kwaliteitsaanpak uitbrengen
1. Bepaal het nieuwe versienummer. Zie https://ictu.github.io/Kwaliteitsaanpak/latest/ICTU-Kwaliteitsaanpak.html#versionering

2. Maak een release branch:
   ```console
   git checkout -b release-vx.y.z
   ```
3. Werk het versienummer en de releasedatum bij in `./Content/Wijzigingsgeschiedenis.md`.

4. Maak een nieuwe map voor de release in `./docs` en voeg deze toe aan versiebeheer:
   ```console
   mkdir docs/vx.y.z
   git add docs
   ```
5. Werk het versienummer en de releasedatum bij in `docs/index.html` en het versienummer in `docs/404.html` (zodat links met `latest` naar de nieuwe versie verwijzen).
6. Werk het versienummer bij in `pyproject.toml`.
7. Werk het versienummer bij in de variable `LATEST` in `DocumentDefinitions/Shared/variables.json`.
8. Genereer de documentatie met het nieuwe versienummer:
   ```console
   VERSION=x.y.z just make
   ```
   De gegenereerde documenten staan in de map `docs/vx.y.z`.
9. Commit en push de wijzigingen:
   ```console
   git add .
   git commit -m "Release vx.y.z"
   git push
   ```
10. Review en merge de branch op GitHub.
11. Tag de release, push de tag naar GitHub en verwijder de release branch lokaal:
   ```console
   git checkout master
   git pull -p
   git tag vx.y.z
   git push --tags
   git branch -D release-vx.y.z
   ```
12. Controleer dat de docs folder is gepubliceerd door de [pages-build-deployment](https://github.com/ICTU/Kwaliteitsaanpak/actions/workflows/pages/pages-build-deployment) GitHub Action op [https://ictu.github.io/Kwaliteitsaanpak](https://ictu.github.io/Kwaliteitsaanpak).
13. Kondig de release aan in het MS Teams-kanaal **"ICTU Softwareontwikkeling/Algemeen"**.
   - Bij een **minor release**: stuur ook een e-mail naar SDM'ers en Kwaliteitsmanagers en CC: hoofd ISE.
   - Bij een **major release**: stuur een e-mail naar iedereen bij ISE.

# Bijdragen aan de Toolgidsen
Zie [Content/Toolgids/README.md](Content/Toolgids/README.md) voor meer informatie.

## Contact
Voor vragen over de Kwaliteitsaanpak of deze repository, neem contact op met:
- [Sebastiaan Koot 📧](mailto:sebastiaan.koot@ictu.nl)
- [Frank Niessink 📧](mailto:frank.niessink@ictu.nl)
