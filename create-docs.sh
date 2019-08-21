#!/bin/bash
npm i
npm version prerelease --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

# Map symbolic references, like title and Maatregelen, to their actual content
# map-refs <source> <document title> <output>
function map-refs {
    sed s/{{TITLE}}/"$2"/g $1 > $3
}

# Generate into folder $1 the document $2.pdf, titled $3.
# generate <document definition folder> <name of document output without extension> <title>
function generate {
    mkdir -p Generated/$1
    # Cover
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/cover.json
    node_modules/markdown-to-html/bin/markdown Generated/$1/cover.md -s /ka/DocumentDefinitions/$1/cover.css | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/$1/cover.html
    # Body
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json  # pass 1: generated input for abbreviations
    cat Generated/$1/document.md | python3 create-abbreviations-appendix.py > Generated/$1/abbreviations.md   
    node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json  # pass 2: include up-to-date list of abbreviations
    node_modules/markdown-to-html/bin/markdown Generated/$1/document.md -s /ka/DocumentDefinitions/$1/document.css | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/$1/document.html
    # Create header
    sed s/{{TITLE}}/$3/g DocumentDefinitions/Shared/header.html > Generated/$1/header.html
    # Create pdf
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html Generated/$1/header.html --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover Generated/$1/cover.html \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        Generated/$1/document.html $2.pdf
}

# Generate into folder Templates/$1 the template document $2.pdf, titled $3.
# generate-template <document definition folder> <name of document output without extension> <title>
function generate-template {
    mkdir -p Generated/Templates/$1
    # Initialize md files
    echo "{	\"build\" : \"Generated/Templates/$1/cover-expanded.md\", \"files\" : [\"DocumentDefinitions/Templates/Shared/cover.md\"] }" > Generated/Templates/$1/cover.json
    echo "{	\"build\" : \"Generated/Templates/$1/document-expanded.md\", \"files\" : [\"DocumentDefinitions/Templates/$1/document.md\"] }" > Generated/Templates/$1/document.json
    # Cover
    node node_modules/markdown-include/bin/cli.js Generated/Templates/$1/cover.json
    map-refs Generated/Templates/$1/cover-expanded.md "$3" Generated/Templates/$1/cover-post.md
    #sed s/{{TITLE}}/"$3"/g Generated/Templates/$1/cover-expanded.md > Generated/Templates/$1/cover-post.md
    node_modules/markdown-to-html/bin/markdown Generated/Templates/$1/cover-post.md \
        -s /ka/DocumentDefinitions/Shared/cover.css | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/Templates/$1/cover.html
    # Body
    node node_modules/markdown-include/bin/cli.js Generated/Templates/$1/document.json
    map-refs Generated/Templates/$1/document-expanded.md "$3" Generated/Templates/$1/document-post.md
    #sed s/{{TITLE}}/"$3"/g Generated/Templates/$1/document-expanded.md > Generated/Templates/$1/document-post.md
    node_modules/markdown-to-html/bin/markdown Generated/Templates/$1/document-post.md \
        -s /ka/DocumentDefinitions/Shared/document.css | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/Templates/$1/document.html
    # Create header
    map-refs DocumentDefinitions/Shared/header.html "$3" Generated/Templates/$1/header.html
    #sed s/{{TITLE}}/"$3"/g DocumentDefinitions/Shared/header.html > Generated/Templates/$1/header.html
    # Create pdf
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html Generated/Templates/$1/header.html --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover Generated/Templates/$1/cover.html \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        Generated/Templates/$1/document.html $2.pdf
}

generate Full ICTU-Kwaliteitsaanpak-Full "ICTU Kwaliteitsaanpak Software Realisatie"
generate Generic ICTU-Kwaliteitsaanpak-Generic "Kwaliteitsaanpak Software Realisatie"
generate-template Kwaliteitsplan Template-Kwaliteitsplan "Kwaliteitsplan"
generate-template NFE Template-Niet-Functionele-Eisen "Niet-Functionele Eisen"
generate-template Template Template-Generiek "Generiek Template"

python3 create-checklist.py
