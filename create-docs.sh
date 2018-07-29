#!/bin/bash
npm i
npm version patch --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

function generate {
    mkdir -p Generated/$1
    # Cover
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/cover.json
    node_modules/markdown-to-html/bin/markdown Generated/$1/cover.md -s /ka/DocumentDefinitions/$1/cover.css | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/$1/cover.html
    # Body
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json
    node_modules/markdown-to-html/bin/markdown Generated/$1/document.md -s /ka/DocumentDefinitions/$1/document.css | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/$1/document.html
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html DocumentDefinitions/Shared/header.html --header-spacing 10 \
        --margin-bottom 30 --margin-left 30 --margin-right 30 --margin-top 30 \
        cover Generated/$1/cover.html toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        Generated/$1/document.html ICTU-Kwaliteitsaanpak-$1.pdf
}

generate Full
generate Generic
python3 create-checklist.py
