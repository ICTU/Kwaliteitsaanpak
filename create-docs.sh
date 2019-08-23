#!/bin/bash
npm i
npm version prerelease --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

MAATREGEL_DICTIONARY="maatregel-dictionary.txt"
MAATREGEL_DICTIONARY_LINKS="maatregel-dictionary-linked.txt"

# Map symbolic references, like title and Maatregelen, to their actual content
# map-refs 1:<source file> 2:<output file> 3:<document title> 4:<document header>
function map-refs {
    sed s/{{TITLE}}/"$3"/g $1 | \
    sed s/{{HEADER}}/"$4"/g > $2
}

# Map symbolic references, like title and Maatregelen, to their mapped content from a dictionary file
# map-refs 1:<source file> 2:<output file> 3:<dictionary file>
function map-refsd {
    awk -F= 'FNR==NR{a[$1]=$2;next} {for (i in a)sub(i, a[i]);print}' $3 $1 > $2
}

# Create html document from MD source.
# create-html 1:<output folder> 2:<source md> 3:<css> 4:<output name without extension> 5:<dictionary file>
function create-html
{
    EXPANDED="$1/$4-expanded.md"
    JSON="$1/$4.json"
    POST="$1/$4-post.md"
    HTML="$1/$4.html"

    echo "{	\"build\" : \"$EXPANDED\", \"files\" : [\"$2\"] }" > $JSON
    node node_modules/markdown-include/bin/cli.js $JSON

    map-refsd $EXPANDED $POST $5

    node_modules/markdown-to-html/bin/markdown $POST -s $3 | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > $HTML
}

# Generate into folder $1 the document $2.pdf, with title $3 and header $4, using MD cover file $5 and MD document file $6.
# generate 1:<output folder> 2:<name of document output without PDF extension>
#          3:<document title> 4:<document header> 5:<cover md> 6:<document md> 7:<dictionary file>
function generate {
    OUTPUT_PATH="Generated/$1"
    DICTIONARY="$OUTPUT_PATH/dict.txt"

    mkdir -p $OUTPUT_PATH

    # Create dictionary
    cat $7 > $DICTIONARY
    echo -e "{{TITLE}}=$3\n{{HEADER}}=$4\n" >> $DICTIONARY

    # Cover
    create-html $OUTPUT_PATH $5 /ka/DocumentDefinitions/Shared/cover.css "cover" $DICTIONARY   
    # Body
    create-html $OUTPUT_PATH $6 /ka/DocumentDefinitions/Shared/document.css "document" $DICTIONARY
    # Header
    map-refsd DocumentDefinitions/Shared/header.html $OUTPUT_PATH/header.html $DICTIONARY
    # Create pdf
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html $OUTPUT_PATH/header.html --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover $OUTPUT_PATH/cover.html \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        $OUTPUT_PATH/document.html $2.pdf
}

# Generate into folder $1 the document $2.pdf, titled $3.
# generate-kwaliteitsaanpak 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-kwaliteitsaanpak {
    TITLE="$3"
    HEADER="$TITLE"
    generate $1 $2 "$TITLE" "$HEADER" DocumentDefinitions/$1/cover.md DocumentDefinitions/$1/document.md $MAATREGEL_DICTIONARY_LINKS
}

# Generate into folder Templates/$1 the template document $2.pdf, titled $3.
# generate-template 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-template {
    TITLE="$3"
    HEADER="$TITLE {projectnaam} {versie}"
    generate Templates/$1 $2 "$TITLE" "$HEADER" DocumentDefinitions/Templates/Shared/cover.md DocumentDefinitions/Templates/$1/document.md $MAATREGEL_DICTIONARY
}

python3 create-dictionary.py > $MAATREGEL_DICTIONARY
python3 create-dictionary.py --link > $MAATREGEL_DICTIONARY_LINKS

generate-kwaliteitsaanpak Full ICTU-Kwaliteitsaanpak-Full "ICTU Kwaliteitsaanpak Software Realisatie"
generate-kwaliteitsaanpak Generic ICTU-Kwaliteitsaanpak-Generic "Kwaliteitsaanpak Software Realisatie"
generate-template Template Template-Generiek "Generiek Template"
generate-template Kwaliteitsplan Template-Kwaliteitsplan "Kwaliteitsplan"
generate-template NFE Template-Niet-Functionele-Eisen "Niet-Functionele Eisen"

python3 create-checklist.py
