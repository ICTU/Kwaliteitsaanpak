# ICTU Kwaliteitsaanpak Softwareontwikkeling

[ICTU's Kwaliteitsaanpak](https://www.ictu.nl/kwaliteitsaanpak) is a set of guidelines used at [ICTU](https://www.ictu.nl) for software development projects. It is only available in Dutch, sorry.

This repository contains the source information and automation scripts for generating ICTU's Kwaliteitsaanpak documentation. The Kwaliteitsaanpak itself is available via [https://ictu.github.io/Kwaliteitsaanpak](https://ictu.github.io/Kwaliteitsaanpak).

## Documents

The Kwaliteitsaanpak consists of a main document containing the Kwaliteitsaanpak itself, a number of templates, and a self-assessment checklist. The sources are a collection of Markdown files and supporting material. Scripts convert the Kwaliteitsaanpak main document to html and pdf, the templates to docx, and the self-assessment checklist to xslx.

## Authoring guidelines

- For each guideline:
  - Create a folder under ./Content/Maatregelen
  - Add 2 files to the folder
    - Definitie.md - brief one paragraph definition of the guideline
    - Maatregel.md - guideline title, description, and rationale
- Add the maatregel to the document structure definition in ./DocumentDefinitions/Kwaliteitsaanpak/ICTU-Kwaliteitsaanpak.md

## Document definitions

- Each document definition is stored inside a subfolder of ./DocumentDefinitions
- A document definition is composed of a number of files:
  - document.json - meta data about the document
  - document.md - content of the document
  - document.css - styling
  - cover.css - styling
- Shared material such as headers, footers, and stylesheets are in the ./DocumentDefinitions/Shared folder

## Generating the documentation (pdf, docx, and xlsx)

- Make sure you have Docker and Docker-compose.
- Clone this repository
- Run "docker-compose up"
  - The document patch version is updated in docker-compose.yml
  - The html, pdf, docx and xlsx versions of the documents are created in the dist folder

## Point of contact

Points of contact for the ICTU Kwaliteitsaanpak Softwareontwikkeling and this repository are [Auke Bloembergen](https://github.com/aukebloembergen) and [Frank Niessink](https://github.com/fniessink).
