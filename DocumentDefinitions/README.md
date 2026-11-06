# Documentdefinities

De JSON-bestanden in deze folder specificeren hoe de verschillende outputbestanden van de Kwaliteitsaanpak gegenereerd worden.

De documentdefinitie ziet er ongeveer zo uit:

```json
{
    "BuildPath": "build/Templates/Kwaliteitsplan/",
    "Title": "Kwaliteitsplan",
    "Subtitle": "{het project}",
    "DocumentType": "Template",
    "DocumentFolder": "Kwaliteitsplan",
    "FrontPage": "ICTU",
    "OutputFormats": {
        "docx": {
            "IncludeTableOfContents": true,
            "InputFile": "DocumentDefinitions/Templates/document-template.md",
            "OutputFile": "ICTU-Template-Kwaliteitsplan.docx",
            "OutputPaths": [
                "docs/$VERSIE$"
            ],
            "ReferenceFile": "DocumentDefinitions/reference-ictu.docx"
        }
    },
    "VariablesFiles": [
        "DocumentDefinitions/Shared/variables.json"
    ]
}
```

Bovenstaande specificatie geeft:
- `BuildPath`: de folder waar tussenbestanden geschreven kunnen worden.
- `Title`: de titel van het document.
- `Subtitle`: de subtitel van het document. De tekst `{het project}` staat tussen accolades, zodat deze in het document geel gearceerd wordt.
- `DocumentType`: het soort document. Mogelijke waardes zijn `Template` voor templates en `Kwaliteitsaanpak` voor alle andere documenten.
- `DocumentFolder`: de folder onder `Content/Templates` waar de inhoud van het document staat. Dit hoeft dus alleen voor templates te worden aangegeven.
- `FrontPage`: welke voorpagina moet het document krijgen? Mogelijke waardes zijn `ICTU` en `Neutral`.
- `OutputFormats`: een opsomming van de outputformaten die gegenereerd moeten worden. Mogelijke formaten zijn naast `docx`: `xlsx`, `pptx`, `html`, `json` en `zip`.
- `VariableFiles`: een lijst van bestanden met variabelen die gebruikt zijn in de Markdown bronbestanden.

Voor elk outputformaat moet worden opgegeven:
- `IncludeTableOfContents`: moet het document een inhoudsopgave krijgen? Mogelijke waardes zijn `true` en `false`.
- `InputFile`: het te converteren Markdowndocument. Kan weggelaten worden als het outputformaat `zip` is.
- `InputPaths`: alleen bij outputformaat `zip`, de te zippen bronbestanden.
- `OutputFile`: het te schrijven bestand in het outputformaat.
- `OutputPath`: de folders waar de outputbestanden terecht komen.
- `ReferenceFile`: het (lege) bestand dat als basis gebruikt wordt voor het outputbestand. Dit is alleen nodig bij outputformaten `docx` en `pptx`.
- `StyleSheets`: de paden van te gebruiken CSS-bestanden. Bijvoorbeeld: `StyleSheets": ["basis.css", "styles/extra.css"]`. Dit is alleen bedoeld voor het outputformaat `html`. De CSS-bestanden worden als link in de HTML opgenomen, bijvoorbeeld: `<link rel="stylesheet" href="basis.css"><link rel="stylesheet" href="styles/extra.css">`. Merk op dat de paden relatief zijn ten opzichte van de locatie van het HTML-bestand. `StyleSheets` zorgt alleen voor het opnemen van de links; het kopiëren van de CSS-bestanden doe je met `CopyFiles`, zie hieronder.

Bij outputformaat `html` is het nodig bestanden te kopiëren naar de outputfolder. Denk aan CSS-bestanden en plaatjes. Dit kan met `CopyFiles` gespecificeerd worden:

```json
{
    "BuildPath": "build/Kwaliteitsaanpak/",
    "Title": "ICTU Kwaliteitsaanpak Softwareontwikkeling",
    "Subtitle": "Samenvatting",
    "DocumentType": "Kwaliteitsaanpak",
    "FrontPage": "ICTU",
    "OutputFormats": {
        "html": {
            "IncludeTableOfContents": false,
            "InputFile": "DocumentDefinitions/Kwaliteitsaanpak/ICTU-Kwaliteitsaanpak-samenvatting.md",
            "OutputFile": "ICTU-Kwaliteitsaanpak-Samenvatting.html",
            "OutputPaths": [
                "docs/$VERSIE$"
            ],
            "StyleSheets": [
                "basis.css",
                "styles/extra.css"
            ],
            "CopyFiles": [
                {
                    "from": "DocumentDefinitions/Shared/document.css",
                    "to": "docs/$VERSIE$/basis.css"
                },
                {
                    "from": "DocumentDefinitions/Shared/fancy.css",
                    "to": "docs/$VERSIE$/styles/extra.css"
                },
                {
                    "from": "Content/Images/*.png",
                    "to": "docs/$VERSIE$"
                }
            ]
        }
    },
    "VariablesFiles": [
        "DocumentDefinitions/Shared/variables.json"
    ]
}
```

`CopyFiles` is een lijst met te kopiëren bestanden. Elk object in de lijst heeft een `from` en `to`:
- `from`: het bronbestand of de bronbestanden (`*` en `?` toegestaan).
- `to`: het doelbestand of de doelfolder. Als de `from` meerdere bestanden specificeert moet de `to` een folder zijn.

# Markdown-dialect

De bronbestanden zijn in Markdown geschreven. Naast de gebruikelijke Markdown-opmaak, zoals koppen, **vet**, _cursief_, `code`, ~~doorgehaald~~, links, plaatjes, lijsten en tabellen, kent de conversie een aantal uitbreidingen.

## Bestanden invoegen

Met `#include` wordt een ander Markdown-bestand ingevoegd. `{{DOCUMENT-FOLDER}}` wordt vervangen door de `DocumentFolder` uit de documentdefinitie:

```markdown
#include "Content/Templates/{{DOCUMENT-FOLDER}}/Template-Inhoud.md"
```

## Variabelen

`$NAAM$` wordt vervangen door de waarde van de variabele `NAAM` uit de `VariablesFiles` van de documentdefinitie, bijvoorbeeld `$KWALITEITSAANPAK$`. Variabelen worden overal vervangen, behalve in codeblokken.

## Instructies

Tekst tussen accolades, zoals `{het project}`, is een instructie voor de gebruiker van een template. Instructies worden in Word-documenten geel gearceerd.

## Blokken

Met `<!-- begin: naam -->` en `<!-- end: naam -->` wordt een blok gemarkeerd, optioneel met één attribuut. In gebruik zijn `measure` voor maatregelen (`<!-- begin: measure composite=true -->` voor maatregelen met submaatregelen) en `slide` voor de inhoud van dia's in de presentatie.

Binnen een maatregel markeren `[measure-title]…[/measure-title]` en `[submeasure-title]…[/submeasure-title]` de titel van de maatregel en de submaatregelen. Met `<!-- submeasures: 1,2 -->` wordt de paragraaf waarin dit staat gemarkeerd als toelichting op de submaatregelen met de genoemde nummers. In de self-assessment checklist komt die toelichting dan bij die submaatregelen te staan in plaats van bij de maatregel.

## Bijlagen

De kop `# Bijlagen` markeert het begin van de bijlagen. Koppen in de bijlagen krijgen in Word een eigen stijl. De presentatie, de self-assessment checklist en de JSON-export slaan de bijlagen over.

## Lijsten

Het niveau van een opsomming wordt bepaald door het opsommingsteken: `*` voor het eerste niveau, `+` voor het tweede en `-` voor het derde. Bij genummerde lijsten is `1.` het eerste niveau, `a.` het tweede en een ingesprongen `1.` het derde.

## Codeblokken

Een codeblok moet een taal hebben, zodat de code van syntax highlighting kan worden voorzien:

````markdown
```python
print("Hello world")
```
````

## Plaatjes

Een plaatje moet een titel hebben:

```markdown
![Alternatieve tekst](plaatje.png "Titel van het plaatje")
```

## Admonitions

Admonitions (ook wel callouts of alerts) zijn gekleurde blokken die de aandacht vestigen op een opmerking, tip of waarschuwing. De syntax is die van [GitHub-alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts). Er zijn vijf typen, elk met een eigen kleur, icoon en standaardtitel:

```markdown
> [!NOTE]
> Informatie die de lezer moet meenemen, ook bij snel lezen. Standaardtitel: "Opmerking".

> [!TIP]
> Optionele informatie die de lezer helpt. Standaardtitel: "Tip".

> [!IMPORTANT]
> Cruciale informatie die de lezer nodig heeft. Standaardtitel: "Belangrijk".

> [!WARNING]
> Informatie die vanwege mogelijke risico's direct aandacht vraagt. Standaardtitel: "Waarschuwing".

> [!CAUTION]
> Mogelijke negatieve gevolgen van een handeling. Standaardtitel: "Let op".
```

Regels:

- Het type is niet hoofdlettergevoelig: `> [!note]` mag ook.
- Een tekst achter het type vervangt de standaardtitel, bijvoorbeeld `> [!WARNING] Aandachtspunt`. Variabelen in de titel worden vervangen. Let op: GitHub toont een admonition met eigen titel niet als alert, maar als gewoon citaat.
- De admonition loopt tot de eerste regel die niet met `>` begint. Een lege regel beëindigt de admonition dus ook. Een nieuwe `> [!TYPE]`-regel beëindigt de vorige admonition en begint een nieuwe.
- De inhoud is gewone Markdown: alinea's, (geneste) lijsten, tabellen, codeblokken, opmaak, links en variabelen werken binnen een admonition. Een regel met alleen `>` scheidt alinea's. Koppen zijn niet toegestaan in een admonition.

Bijvoorbeeld:

```markdown
> [!TIP] Meer weten?
> Lees de **toolgids** voor:
>
> * het [installeren](https://example.org/installeren) van de tool;
> * het configureren van de tool.
```

In HTML wordt een admonition een `<aside>`-element met de classes `admonition` en `admonition-<type>`, zie `DocumentDefinitions/Shared/document.css` voor de opmaak. In Word wordt een admonition een tabel met één gekleurde cel. De opmaak staat in de referentiedocumenten (`DocumentDefinitions/reference-*.docx`): een tabelstijl `Admonition <Type>` voor de linkerrand en achtergrondkleur en een tekenstijl `Admonition <Type> Title` voor de titel, bijvoorbeeld `Admonition Warning` en `Admonition Warning Title`. Pas bij het wijzigen van de kleuren zowel de CSS als beide referentiedocumenten aan. In de self-assessment checklist wordt de tekst van een admonition, voorafgegaan door de titel, opgenomen in de toelichting bij de maatregel. De presentatie neemt alleen de tekst over.
