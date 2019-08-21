#!/bin/bash
npm i
npm version prerelease --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

# Map symbolic references, like title and Maatregelen, to their actual content
# map-refs 1:<source file> 2:<document title> 3:<output file>
function map-refs {
    sed s/{{TITLE}}/"$2"/g $1 > $3
}

# create-html 1:<output folder> 2:<source md> 3:<css> 4:<output name without extension> 5:<document title>
function create-html
{
    EXPANDED="$1/$4-expanded.md"
    JSON="$1/$4.json"
    POST="$1/$4-post.md"
    HTML="$1/$4.html"

    echo "{	\"build\" : \"$EXPANDED\", \"files\" : [\"$2\"] }" > $JSON
    node node_modules/markdown-include/bin/cli.js $JSON
    map-refs $EXPANDED "$5" $POST
    node_modules/markdown-to-html/bin/markdown $POST -s $3 | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > $HTML
}

# Generate into folder $1 the document $2.pdf, titled $3.
# generate <document definition folder> <name of document output without extension> <title>
function generate {
    OUTPUT_PATH="Generated/$1"
    mkdir -p $OUTPUT_PATH

    # Cover
    create-html $OUTPUT_PATH DocumentDefinitions/$1/cover.md \
        /ka/DocumentDefinitions/$1/cover.css "cover" "$3"   

    #node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/cover.json
    #node_modules/markdown-to-html/bin/markdown Generated/$1/cover.md -s /ka/DocumentDefinitions/$1/cover.css | \
    #    PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/$1/cover.html

    # Body
    create-html $OUTPUT_PATH DocumentDefinitions/$1/document.md \
        /ka/DocumentDefinitions/$1/document.css "document" "$3"

    #node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json  # pass 1: generated input for abbreviations
    #cat Generated/$1/document.md | python3 create-abbreviations-appendix.py > Generated/$1/abbreviations.md   
    #node node_modules/markdown-include/bin/cli.js ./DocumentDefinitions/$1/document.json  # pass 2: include up-to-date list of abbreviations
    #node_modules/markdown-to-html/bin/markdown Generated/$1/document.md -s /ka/DocumentDefinitions/$1/document.css | \
    #    PYTHONIOENCODING="UTF-8" python3 post-process-html.py > Generated/$1/document.html

    # Header
    map-refs DocumentDefinitions/Shared/header.html "$3" $OUTPUT_PATH/header.html
    # Create pdf
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html $OUTPUT_PATH/header.html --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover $OUTPUT_PATH/cover.html \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        $OUTPUT_PATH/document.html $2.pdf
}

# Generate into folder Templates/$1 the template document $2.pdf, titled $3.
# generate-template <document definition folder> <name of document output without extension> <title>
function generate-template {
    OUTPUT_PATH="Generated/Templates/$1"
    mkdir -p $OUTPUT_PATH
   
    # Cover
    create-html $OUTPUT_PATH DocumentDefinitions/Templates/Shared/cover.md \
        /ka/DocumentDefinitions/Shared/cover.css "cover" "$3"   
    # Body
    create-html $OUTPUT_PATH DocumentDefinitions/Templates/$1/document.md \
        /ka/DocumentDefinitions/Shared/document.css "document" "$3"
    # Header
    map-refs DocumentDefinitions/Shared/header.html "$3" $OUTPUT_PATH/header.html
 
    # Create pdf
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html $OUTPUT_PATH/header.html --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover $OUTPUT_PATH/cover.html \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        $OUTPUT_PATH/document.html $2.pdf
}

generate Full ICTU-Kwaliteitsaanpak-Full "ICTU Kwaliteitsaanpak Software Realisatie"
generate Generic ICTU-Kwaliteitsaanpak-Generic "Kwaliteitsaanpak Software Realisatie"
generate-template Kwaliteitsplan Template-Kwaliteitsplan "Kwaliteitsplan"
generate-template NFE Template-Niet-Functionele-Eisen "Niet-Functionele Eisen"
generate-template Template Template-Generiek "Generiek Template"

python3 create-checklist.py
