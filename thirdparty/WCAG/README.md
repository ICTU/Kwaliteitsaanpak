# Convert WCAG guidelines to Markdown

Script om het [WCAG JSON bestand](https://github.com/w3c/wai-wcag-quickref/blob/gh-pages/_data/wcag21.json) om te zetten in een Markdown tabel die in de Kwaliteitsaanpak kan worden ingevoegd. 

Het script `wcag.py` leest het `wcag.json` bestand, converteert dit naar een Markdown tabel en schrijft die in de Content/Templates/NFE/ folder.

Usage:: 

```console
$ python3 wcag.py
```

