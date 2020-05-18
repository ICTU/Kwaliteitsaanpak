#!/bin/bash

# npm i

mkdir -p build

KA_TITLE="ICTU Kwaliteitsaanpak Softwareontwikkeling"
KA_VERSION="2.1.0-unreleased"

OUTPUT_PATH="dist"  # Folder to write the final documents to

# Expand MD file
# expand-md 1:<source md file> 2:<output file>
function expand-md
{
    echo "--- expand {$1} into {$2}"

    JSON="$2.json"

    echo "---- creating temporary build config {$JSON}"
    echo "{\"build\" : \"$2\", \"files\" : [\"$1\"] }" > $JSON
    echo "---- importing MD files in {$1} creating {$2}"
    node node_modules/markdown-include/bin/cli.js $JSON
}

# Create main document for a template
# create-template 1:<template document> 2:<template folder name> 3:<output file>
function create-template
{
    echo "--- creating template {$3} from {$1} refering to {$2}"
    sed s/{{TEMPLATE-FOLDER}}/"$2"/g $1 > $3
}

# Expand MD document into folder $1, creating $2.md, and MD document file $3.
# expand 1:<output folder> 2:<name of document output without extension> 3:<document md>
function expand
{
    BUILD_PATH="build/$1"
    DICTIONARY="$BUILD_PATH/dict.txt"
    EXPANDED="$BUILD_PATH/$2.md"
    DOCUMENT_MD="$3"

    echo "-- generate: $2"

    # Create directories
    echo "--- build path: $BUILD_PATH"
    mkdir -p $BUILD_PATH
    echo "--- output path: $OUTPUT_PATH"
    mkdir -p $OUTPUT_PATH

    # Expand MD file
    expand-md $DOCUMENT_MD "$EXPANDED"
}

# Generate into folder $1 the document $2.pdf, titled $3.
# generate-kwaliteitsaanpak 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-kwaliteitsaanpak
{
    BUILD_PATH="build/$1"
    TITLE="$3"
    HEADER="$TITLE"
    COVER_HTML_BUILD="$BUILD_PATH/ICTU-Kwaliteitsaanpak.cover.html"
    DOC_MD="DocumentDefinitions/$1/document.md"
    DICTIONARY="$BUILD_PATH/dict.txt"
    EXPANDED="$BUILD_PATH/$2.md"
    HTML_BUILD="$BUILD_PATH/ICTU-Kwaliteitsaanpak.html"
    HEADER_HTML_BUILD="$BUILD_PATH/header.html"
    PDF_OUTPUT="$OUTPUT_PATH/$2.pdf"

    expand $1 $2 $DOC_MD

    # PDF generation
    # Body
    python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/kwaliteitsaanpak.json
    # Header
    python -c "import sys; print(open('DocumentDefinitions/Shared/header.html').read() % sys.argv[1])" "$HEADER" > $HEADER_HTML_BUILD
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
    BUILD_PATH="build/$TEMPLATE_PATH"
    DOC_MD="$BUILD_PATH/document.md"

    echo "--- template build path: $BUILD_PATH"
    mkdir -p $BUILD_PATH
    create-template "$TEMPLATE_TEMPLATE" $1 $DOC_MD

    expand $TEMPLATE_PATH $2 $DOC_MD
}

generate-kwaliteitsaanpak Kwaliteitsaanpak ICTU-Kwaliteitsaanpak "$KA_TITLE"

generate-template Template Template-Generiek "Generiek template"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/generiek-template.json

generate-template Detailtestplan Template-Detailtestplan "Detailtestplan"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/detailtestplan.json

generate-template GFO Template-Globaal-Functioneel-Ontwerp "Globaal Functioneel Ontwerp"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/globaal-functioneel-ontwerp.json

generate-template HLD Template-High-Level-Design "High-Level Design"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/high-level-design.json

generate-template Kwaliteitsplan Template-Kwaliteitsplan "Kwaliteitsplan"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/kwaliteitsplan.json

generate-template NFE Template-Niet-Functionele-Eisen "Niet-Functionele Eisen"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/niet-functionele-eisen.json

generate-template SAD Template-Software-architectuurdocument "Software-architectuurdocument"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/softwarearchitectuurdocument.json

generate-template Projectvoorstel-Voorfase Template-Projectvoorstel-Voorfase "Projectvoorstel Voorfase"
python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/projectvoorstel-voorfase.json
