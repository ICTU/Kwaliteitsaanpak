#!/bin/bash

mkdir -p build
mkdir -p dist

KA_TITLE="ICTU Kwaliteitsaanpak Softwareontwikkeling"
KA_VERSION="2.1.0-unreleased"

OUTPUT_PATH="dist"  # Folder to write the final documents to

# Generate into folder $1 the document $2.pdf, titled $3.
# generate-kwaliteitsaanpak 1:<output folder> 2:<name of document output without PDF extension> 3:<document title>
function generate-kwaliteitsaanpak
{
    BUILD_PATH="build/$1"
    HEADER="$3"
    COVER_HTML_BUILD="$BUILD_PATH/ICTU-Kwaliteitsaanpak.cover.html"
    DOC_MD="DocumentDefinitions/$1/ICTU-Kwaliteitsaanpak.md"
    HTML_BUILD="$BUILD_PATH/ICTU-Kwaliteitsaanpak.html"
    HEADER_HTML_BUILD="$BUILD_PATH/header.html"
    PDF_OUTPUT="$OUTPUT_PATH/$2.pdf"

    # PDF generation
    # Body
    python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/kwaliteitsaanpak.json
    # Header
    python -c "import sys; print(open('DocumentDefinitions/Shared/header.html').read() % sys.argv[1])" "$KA_TITLE" > $HEADER_HTML_BUILD
    # Create pdf
    docker-compose run wkhtmltopdf -c "wkhtmltopdf \
        --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html $HEADER_HTML_BUILD --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        cover $COVER_HTML_BUILD \
        toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
        $HTML_BUILD $PDF_OUTPUT"
}

generate-kwaliteitsaanpak Kwaliteitsaanpak ICTU-Kwaliteitsaanpak "$KA_TITLE"

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/generiek-template.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/detailtestplan.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/globaal-functioneel-ontwerp.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/high-level-design.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/kwaliteitsplan.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/niet-functionele-eisen.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/softwarearchitectuurdocument.json

python3 src/convert.py --log INFO --version $KA_VERSION DocumentDefinitions/projectvoorstel-voorfase.json
