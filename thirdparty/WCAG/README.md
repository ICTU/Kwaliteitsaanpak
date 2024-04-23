# Convert WCAG guidelines to Markdown

Script om het [WCAG JSON-bestand](https://github.com/w3c/wai-wcag-quickref/blob/gh-pages/_data/wcag22.json) om te zetten in een Markdown tabel die in de Kwaliteitsaanpak kan worden ingevoegd.

Het WCAG JSON-bestand is in deze directory gekopieerd als `wcag.json`.

Het script `wcag.py`:
- runt met behulp van node `axe.getRules()` om de rules te importeren die axe-core ondersteunt,
- leest het `wcag.json` bestand met de WCAG succescriteria,
- converteert dit naar een Markdown tabel en,
- schrijft die in de Content/Templates/NFE/ folder.

Hoe te runnen:

```console
$ npm install
$ python3 wcag.py
```
