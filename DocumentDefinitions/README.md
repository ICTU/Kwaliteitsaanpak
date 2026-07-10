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
