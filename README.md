# ICTU Kwaliteitsaanpak Softwareontwikkeling

ICTU's Kwaliteitsaanpak is a set of guidelines used at [ICTU](https://www.ictu.nl/) for software development projects.

This repository contains the source information and automation scripts for generating ICTU's Kwaliteitsaanpak documentation. The latest release of the Kwaliteitsaanpak is available from the ICTU website: [https://www.ictu.nl/kwaliteitsaanpak](https://www.ictu.nl/kwaliteitsaanpak).

## Documents

The Kwaliteitsaanpak consists of a main document containing the Kwaliteitsaanpak itself, a number of Templates, and a self-assessment checklist. The sources are a collection of markdown files and supporting material. Scripts convert the Kwaliteitsaanpak main document to pdf, the Templates to docx, and the self-assessment checklist to xslx.

## Authoring guidelines

- For each guideline:
  - Create a folder under ./Content/Maatregelen
  - Add 2 files to the folder
    - Definitie.md - brief one paragraph definition of the guideline
    - Maatregel.md - guideline title, description, and rationale
- Add the maatregel to the document structure definition in ./Content/DocumentDefinitions/Full/document.md

## Document definitions

- Each document definition is stored inside a subfolder of ./DocumentDefinitions
- A document definition is composed of a number of files:
  - document.md - list of guidelines composing a document
  - document.css - styling
  - cover.md - cover material (front page)
  - cover.css - styling
- Shared material such as headers, footers, and stylesheets are in the ./DocumentDefinitions/Shared folder
- The script instructions for building a new Template have to be added to ./create-docs.sh

## Generating the documentation (pdf, docx, and xlsx)

- Make sure you have Docker and Docker-compose.
- Clone this repository
- Run "docker-compose up ka"
  - The document patch version is updated (in package.json and Content/Versie.md)
  - The pdf, docx and xlsx versions of the documents are created in the dist folder
