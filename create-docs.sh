#!/bin/bash
npm i
npm version patch --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

function generate {
    mkdir -p Generated/$1
    # Cover
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/cover.json
    node_modules/markdown-to-html/bin/markdown Generated/$1/cover.md -s /ka/DocumentDefinitions/$1/cover.css | \
        sed 's/^<head>$/<head><meta charset="UTF-8">/' > Generated/$1/cover.html
    # Body
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json
    node_modules/markdown-to-html/bin/markdown Generated/$1/document.md -s /ka/DocumentDefinitions/$1/document.css | \
        sed 's/^<head>$/<head><meta charset="UTF-8">/' > Generated/$1/document.html
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html  --footer-font-size 10 --footer-font-name muli \
        --footer-spacing 10 --header-line --header-left "Kwaliteitsaanpak ICTU Softwarerealisatie" \
        --header-right "[page]/[toPage]" --header-font-name muli --header-font-size 10 --header-spacing 10 \
        --margin-bottom 30 --margin-left 20 --margin-right 20 --margin-top 30 \
        cover Generated/$1/cover.html toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        Generated/$1/document.html ICTU-Kwaliteitsaanpak-$1.pdf
}

generate Full
generate Generic
