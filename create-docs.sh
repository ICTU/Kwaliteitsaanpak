#!/bin/bash
npm i

node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/Full/document.json
node_modules/markdown-to-html/bin/markdown ICTU-Kwaliteitsaanpak-Full.md -s /ka/DocumentDefinitions/Full/document.css > ICTU-Kwaliteitsaanpak-Full.html
node htmltopdf.js ICTU-Kwaliteitsaanpak-Full.html

node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/ISR/document.json
node_modules/markdown-to-html/bin/markdown ICTU-Kwaliteitsaanpak-ISR.md -s /ka/DocumentDefinitions/ISR/document.css > ICTU-Kwaliteitsaanpak-ISR.html
node htmltopdf.js ICTU-Kwaliteitsaanpak-ISR.html
