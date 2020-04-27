#!/bin/bash
npm i
npm version 2.0.0 --force --no-git-tag-version --allow-same-version
echo "Versie "$(./node_modules/.bin/extract-json package.json version)", "$(date '+%d-%m-%Y') > ./Content/Versie.md

mkdir -p build

KA_TITLE="ICTU Kwaliteitsaanpak Softwareontwikkeling"
OUTPUT_PATH="dist"  # Folder to write the final documents to

MAATREGEL_DICTIONARY="build/maatregel-dictionary.txt"
MAATREGEL_DICTIONARY_LINKS="build/maatregel-dictionary-linked.txt"

# Map symbolic references, like title and Maatregelen, to their mapped content from a dictionary file
# map-refs 1:<source file> 2:<output file> 3:<dictionary file>
function map-refsd
{
    echo "--- map references in {$1} using {$3} to create {$2}"
    python3 map.py $1 $3 > $2
}

# Expand MD file
# expand-md 1:<source md file> 2:<output file> 3:<dictionary file>
function expand-md
{
    echo "--- expand {$1} into {$2} using dictionary {$3}"

    JSON="$2.json"
    TMP="$2.tmp"

    echo "---- creating temporary build config {$JSON}"
    echo "{\"build\" : \"$TMP\", \"files\" : [\"$1\"] }" > $JSON
    echo "---- importing MD files in {$1} creating {$TMP}"
    node node_modules/markdown-include/bin/cli.js $JSON

    map-refsd $TMP $2 $3
}

# Create html document from MD source.
# create-html 1:<source md> 2:<output file> 3:<css>
function create-html
{
    echo "--- create-html {$2} from {$1} using style {$3}"
    node_modules/markdown-to-html/bin/markdown "$1" -s "$3" | \
        PYTHONIOENCODING="UTF-8" python3 post-process-html.py > $2
}

# Create main document for a template
# create-template 1:<template document> 2:<template folder name> 3:<output file>
function create-template
{
    echo "--- creating template {$3} from {$1} refering to {$2}"
    sed s/{{TEMPLATE-FOLDER}}/"$2"/g $1 > $3
}

# Expand MD document into folder $1, creating $2.md, with title $3 and header $4, using MD cover file $5 and MD document file $6 using dictionary file $7.
# expand 1:<output folder> 2:<name of document output without extension>
#        3:<document title> 4:<document header> 5:<cover md> 6:<document md> 7:<dictionary file>
function expand
{
    BUILD_PATH="build/$1"
    DICTIONARY="$BUILD_PATH/dict.txt"
    EXPANDED="$BUILD_PATH/$2.md"
    EXPANDED_COVER="$BUILD_PATH/$2-cover.md"
    COVER_MD="$5"
    DOCUMENT_MD="$6"
    TITLE="$3"
    HEADER="$4"
    HTML_BUILD="$BUILD_PATH/document.html"
    COVER_HTML_BUILD="$BUILD_PATH/cover.html"
    HEADER_HTML_BUILD="$BUILD_PATH/header.html"
    PDF_OUTPUT="$OUTPUT_PATH/$2.pdf"

    echo "-- generate: $2"

    # Create directories
    echo "--- build path: $BUILD_PATH"
    mkdir -p $BUILD_PATH
    echo "--- output path: $OUTPUT_PATH"
    mkdir -p $OUTPUT_PATH

    # Create dictionary
    cat $7 > $DICTIONARY
    echo -e "{{TITLE}}=$TITLE\n{{HEADER}}=$HEADER\n{{KA-TITLE}}=$KA_TITLE\n{{KA_TITLE}}=$KA_TITLE\n{{KWALITEITSAANPAK}}=$KA_TITLE\n" >> $DICTIONARY
    echo "--- dictionary created: $DICTIONARY"

    # Expand MD file
    expand-md $DOCUMENT_MD "$EXPANDED" "$DICTIONARY"
    expand-md $COVER_MD "$EXPANDED_COVER" "$DICTIONARY"
}

# Generate into folder $1 the document $2.pdf, titled $3.
# generate-kwaliteitsaanpak 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-kwaliteitsaanpak
{
    BUILD_PATH="build/$1"
    TITLE="$3"
    HEADER="$TITLE"
    COVER_MD="DocumentDefinitions/$1/cover.md"
    EXPANDED_COVER="$BUILD_PATH/$2-cover.md"
    COVER_HTML_BUILD="$BUILD_PATH/cover.html"
    DOC_MD="DocumentDefinitions/$1/document.md"
    DICTIONARY="$BUILD_PATH/dict.txt"
    EXPANDED="$BUILD_PATH/$2.md"
    HTML_BUILD="$BUILD_PATH/document.html"
    HEADER_HTML_BUILD="$BUILD_PATH/header.html"
    PDF_OUTPUT="$OUTPUT_PATH/$2.pdf"

    expand $1 $2 "$TITLE" "$HEADER" $COVER_MD $DOC_MD $MAATREGEL_DICTIONARY_LINKS

    # PDF generation
    # Cover
    create-html "$EXPANDED_COVER" "$COVER_HTML_BUILD" /work/DocumentDefinitions/Shared/cover.css
    # Body
    create-html "$EXPANDED" "$HTML_BUILD" /work/DocumentDefinitions/Shared/document.css
    # Header
    map-refsd DocumentDefinitions/Shared/header.html "$HEADER_HTML_BUILD" $DICTIONARY
    # Create pdf
    docker-compose run wkhtmltopdf -c "wkhtmltopdf \
        --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html $HEADER_HTML_BUILD --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover $COVER_HTML_BUILD \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        $HTML_BUILD $PDF_OUTPUT"
}

# Generate into folder Templates/$1 the template document $2.pdf, titled $3.
# generate-template 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-template
{
    TITLE="$3"
    HEADER="$TITLE {projectnaam} {versie}"
    TEMPLATE_TEMPLATE="DocumentDefinitions/Templates/document-template.md"
    TEMPLATE_PATH="Templates/$1"
    COVER_MD="DocumentDefinitions/Templates/Shared/cover.md"
    BUILD_PATH="build/$TEMPLATE_PATH"
    DOC_MD="$BUILD_PATH/document.md"
    DOCX_REF="DocumentDefinitions/reference.docx"

    echo "--- template build path: $BUILD_PATH"
    mkdir -p $BUILD_PATH
    create-template "$TEMPLATE_TEMPLATE" $1 $DOC_MD

    expand $TEMPLATE_PATH $2 "$TITLE" "$HEADER" $COVER_MD $DOC_MD $MAATREGEL_DICTIONARY $DOCX_REF
}

python3 create-dictionary.py > $MAATREGEL_DICTIONARY
python3 create-dictionary.py --link > $MAATREGEL_DICTIONARY_LINKS

#generate-kwaliteitsaanpak Full ICTU-Kwaliteitsaanpak "$KA_TITLE"
generate-template Template Template-Generiek "Generiek Template"
generate-template Kwaliteitsplan Template-Kwaliteitsplan "Kwaliteitsplan"
generate-template NFE Template-Niet-Functionele-Eisen "Niet-Functionele Eisen"
generate-template GFO Template-Globaal-Functioneel-Ontwerp "Globaal Functioneel Ontwerp"
generate-template HLD Template-High-Level-Design "High-Level Design"
generate-template Detailtestplan Template-Detailtestplan "Detailtestplan"
generate-template SAD Template-Software-architectuurdocument "Software-architectuurdocument"
generate-template Projectvoorstel-Voorfase Template-Projectvoorstel-Voorfase "Projectvoorstel Voorfase"

#python3 create-checklist.py "$KA_TITLE"

python3 src/convert.py --log DEBUG DocumentDefinitions/detailtestplan.json
#python3 src/convert.py --log INFO DocumentDefinitions/globaal-functioneel-ontwerp.json
#python3 src/convert.py --log INFO DocumentDefinitions/high-level-design.json
#python3 src/convert.py --log INFO DocumentDefinitions/kwaliteitsplan.json
#python3 src/convert.py --log INFO DocumentDefinitions/niet-functionele-eisen.json
#python3 src/convert.py --log INFO DocumentDefinitions/softwarearchitectuurdocument.json
#python3 src/convert.py --log INFO DocumentDefinitions/projectvoorstel-voorfase.json
#
#docker-compose run mdconvert DocumentDefinitions/detailtestplan.json
#docker-compose run mdconvert DocumentDefinitions/globaal-functioneel-ontwerp.json
#docker-compose run mdconvert DocumentDefinitions/high-level-design.json
#docker-compose run mdconvert DocumentDefinitions/kwaliteitsplan.json
#docker-compose run mdconvert DocumentDefinitions/niet-functionele-eisen.json
#docker-compose run mdconvert DocumentDefinitions/softwarearchitectuurdocument.json
#docker-compose run mdconvert DocumentDefinitions/projectvoorstel-voorfase.json
