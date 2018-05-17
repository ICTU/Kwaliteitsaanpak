#!/bin/bash
npm i
npm version patch --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version) > ./Content/Versie.md

node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/Full/document.json
mkdir -p Generated/Full
node node_modules/.bin/markdown-toc --maxdepth=2 --no-firsth1 ICTU-Kwaliteitsaanpak-Full.md | grep -v "Inhoudsopgave" > ./Generated/Full/TOC.md
node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/Full/document.json
node_modules/markdown-to-html/bin/markdown ICTU-Kwaliteitsaanpak-Full.md -s /ka/DocumentDefinitions/Full/document.css > ICTU-Kwaliteitsaanpak-Full.html
node htmltopdf.js ICTU-Kwaliteitsaanpak-Full.html

node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/ISR/document.json
mkdir -p Generated/ISR
node node_modules/.bin/markdown-toc --maxdepth=2 --no-firsth1 ICTU-Kwaliteitsaanpak-ISR.md | grep -v "Inhoudsopgave" > ./Generated/ISR/TOC.md
node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/ISR/document.json
node_modules/markdown-to-html/bin/markdown ICTU-Kwaliteitsaanpak-ISR.md -s /ka/DocumentDefinitions/ISR/document.css > ICTU-Kwaliteitsaanpak-ISR.html
node htmltopdf.js ICTU-Kwaliteitsaanpak-ISR.html

node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/Generic/document.json
mkdir -p Generated/Generic
node node_modules/.bin/markdown-toc --maxdepth=2 --no-firsth1 ICTU-Kwaliteitsaanpak-Generic.md | grep -v "Inhoudsopgave" > ./Generated/Generic/TOC.md
node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/Generic/document.json
node_modules/markdown-to-html/bin/markdown ICTU-Kwaliteitsaanpak-Generic.md -s /ka/DocumentDefinitions/Generic/document.css > ICTU-Kwaliteitsaanpak-Generic.html
node htmltopdf.js ICTU-Kwaliteitsaanpak-Generic.html
