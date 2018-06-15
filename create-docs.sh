#!/bin/bash
npm i
npm version patch --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

function generate {
    mkdir -p Generated/$1
    echo "To be replaced by actual TOC" > Generated/$1/TOC.md
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json
    node node_modules/.bin/markdown-toc --maxdepth=2 --no-firsth1 ICTU-Kwaliteitsaanpak-$1.md | sed "s/\-\-/\-/" | sed "s/risicos/risico\-s/" | grep -v -e "#inhoudsopgave" -e "#wijzigingsgeschiedenis" -e "#algemeen" -e "#ictu-specifiek" > ./Generated/$1/TOC.md
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json
    node_modules/markdown-to-html/bin/markdown ICTU-Kwaliteitsaanpak-$1.md -s /ka/DocumentDefinitions/$1/document.css |  sed 's/^<head>$/<head><meta charset="UTF-8">/' > ICTU-Kwaliteitsaanpak-$1.html
    wkhtmltopdf --footer-center "[page] van [toPage]" --footer-font-size 10 --footer-font-name muli --footer-spacing 10 --zoom 1.6 --margin-bottom 20 --margin-top 20 ICTU-Kwaliteitsaanpak-$1.html ICTU-Kwaliteitsaanpak-$1.pdf
}

generate Full
generate Generic
