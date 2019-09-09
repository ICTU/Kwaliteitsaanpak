#!/bin/bash
npm i
npm version prerelease --force --no-git-tag-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

mkdir -p build

MAATREGEL_DICTIONARY="build/maatregel-dictionary.txt"
MAATREGEL_DICTIONARY_LINKS="build/maatregel-dictionary-linked.txt"

# Map symbolic references, like title and Maatregelen, to their actual content
# map-refs 1:<source file> 2:<output file> 3:<document title> 4:<document header>
function map-refs 
{
    sed s/{{TITLE}}/"$3"/g $1 | \
    sed s/{{HEADER}}/"$4"/g > $2
}

# Map symbolic references, like title and Maatregelen, to their mapped content from a dictionary file
# map-refs 1:<source file> 2:<output file> 3:<dictionary file>
function map-refsd 
{
    awk -F= 'FNR==NR{a[$1]=$2;next} {for (i in a)sub(i, a[i]);print}' $3 $1 > $2
}

# Expand MD file
# expand-md 1:<source md file> 2:<output file> 3:<dictionary file>
function expand-md
{
    echo "expand-md {$1} {$2} {$3}"

    JSON="$2.json"
    TMP="$2.tmp"

    echo "{	\"build\" : \"$TMP\", \"files\" : [\"$1\"] }" > $JSON
    node node_modules/markdown-include/bin/cli.js $JSON

    map-refsd $TMP $2 $3
}

# Create html document from MD source.
# create-html 1:<output folder> 2:<source md> 3:<css> 4:<output name without extension> 5:<dictionary file>
function create-html
{
    echo "create-html {$1} {$2} {$3} {$4} {$5}"
    #EXPANDED="$1/$4-expanded.md"
    HTML="$1/$4.html"

    #expand-md $2 $EXPANDED $5

    node_modules/markdown-to-html/bin/markdown "$2" -s "$3" | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > $HTML
}

# Create word document from MD source
# create-word 1:<output folder> 2:<source md> 3:<style ref document> 4:<output name without extension> 5:<dictionary file> 6:<document title>
function create-word
{
    echo "create-word {$1} {$2} {$3} {$4} {$5} {$6}"

    #EXPANDED="$1/$4-expanded.md"
    DOCX="$1/$4.docx"

    #expand-md $2 $EXPANDED $5

    python3 md-to-docx.py "$2" "$DOCX" "$6" "$3"
}

# Generate into folder $1 the document $2.pdf, with title $3 and header $4, using MD cover file $5 and MD document file $6.
# generate 1:<output folder> 2:<name of document output without extension>
#          3:<document title> 4:<document header> 5:<cover md> 6:<document md> 7:<dictionary file> 8:<docx reference file>
function generate 
{
    OUTPUT_PATH="build/$1"
    FINAL_DOCUMENTS_PATH="dist"  # Folder to write the final documents to
    DICTIONARY="$OUTPUT_PATH/dict.txt"
    EXPANDED="$OUTPUT_PATH/$2-expanded.md"
    EXPANDED_COVER="$OUTPUT_PATH/$2-cover-expanded.md"

    mkdir -p $OUTPUT_PATH
    mkdir -p $FINAL_DOCUMENTS_PATH

    # Create dictionary
    cat $7 > $DICTIONARY
    echo -e "{{TITLE}}=$3\n{{HEADER}}=$4\n" >> $DICTIONARY

    # Expand MD file
    expand-md $6 "$EXPANDED" "$7"
    expand-md $5 "$EXPANDED_COVER" "$7"

    # PDF generation
    # Cover
    create-html $OUTPUT_PATH "$EXPANDED_COVER" /ka/DocumentDefinitions/Shared/cover.css "cover" $DICTIONARY   
    # Body
    create-html $OUTPUT_PATH "$EXPANDED" /ka/DocumentDefinitions/Shared/document.css "document" $DICTIONARY
    # Header
    map-refsd DocumentDefinitions/Shared/header.html $OUTPUT_PATH/header.html $DICTIONARY
    # Create pdf
    wkhtmltopdf --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html $OUTPUT_PATH/header.html --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover $OUTPUT_PATH/cover.html \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        $OUTPUT_PATH/document.html $FINAL_DOCUMENTS_PATH/$2.pdf

    # DOCX generation
    create-word $OUTPUT_PATH $6 $8 "$FINAL_DOCUMENTS_PATH/$2" $DICTIONARY "$3"
}

# Generate into folder $1 the document $2.pdf, titled $3.
# generate-kwaliteitsaanpak 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-kwaliteitsaanpak 
{
    TITLE="$3"
    HEADER="$TITLE"
    COVER_MD="DocumentDefinitions/$1/cover.md"
    DOC_MD="DocumentDefinitions/$1/document.md"
    DOCX_REF="DocumentDefinitions/reference.docx"
    generate $1 $2 "$TITLE" "$HEADER" $COVER_MD $DOC_MD $MAATREGEL_DICTIONARY_LINKS $DOCX_REF
}

# Generate into folder Templates/$1 the template document $2.pdf, titled $3.
# generate-template 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-template 
{
    TITLE="$3"
    HEADER="$TITLE {projectnaam} {versie}"
    COVER_MD="DocumentDefinitions/Templates/Shared/cover.md"
    DOC_MD="DocumentDefinitions/Templates/$1/document.md"
    DOCX_REF="DocumentDefinitions/reference.docx"
    generate Templates/$1 $2 "$TITLE" "$HEADER" $COVER_MD $DOC_MD $MAATREGEL_DICTIONARY $DOCX_REF
}

python3 create-dictionary.py > $MAATREGEL_DICTIONARY
python3 create-dictionary.py --link > $MAATREGEL_DICTIONARY_LINKS

generate-kwaliteitsaanpak Full ICTU-Kwaliteitsaanpak-Full "ICTU Kwaliteitsaanpak Software Realisatie"
generate-kwaliteitsaanpak Generic ICTU-Kwaliteitsaanpak-Generic "Kwaliteitsaanpak Software Realisatie"
generate-template Template Template-Generiek "Generiek Template"
generate-template Kwaliteitsplan Template-Kwaliteitsplan "Kwaliteitsplan"
generate-template NFE Template-Niet-Functionele-Eisen "Niet-Functionele Eisen"
generate-template GFO Template-Globaal-Functioneel-Ontwerp "Globaal Functioneel Ontwerp"
generate-template HLD Template-High-Level-Design "High-Level Design"

python3 create-checklist.py
