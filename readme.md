# ICTU Kwaliteitsaanpak

ICTU's Kwaliteitsaanpak is a set of guidelines used at [ICTU](https://www.ictu.nl/) for software development projects.

This repository contains the source information and automation scripts for generating ICTU's Kwaliteitsaanpak documentation. The latest release of the Kwaliteitsaanpak is available from the ICTU website: [https://www.ictu.nl/kwaliteitsaanpak](https://www.ictu.nl/kwaliteitsaanpak).

## Authoring guidelines

- For each guideline:
  - Create a folder under ./Content/Maatregelen
  - Add 3 files to the folder
    - Titel.md - guideline title
    - Maatregel.md - guideline description and rationale
    - ISR - guideline implementation at ICTU-ISR
- Add the maatregel to one or more document definitions

## Document definitions

- Each document definition is stored inside subfolder of ./DocumentDefinitions
- A document definition is composed of 6 files:
  - document.md - list of guidelines composing a document
  - document.css - styling
  - document.json - document configuration
  - cover.md - cover material (front page, change history)
  - cover.css - styling
  - cover.json - document configuration
- The script instructions for building a new Document Definition have to be added to ./create-docs.sh

## Generating the documentation (pdf)

- Clone this repository
- Run "docker-compose up"
  - The document patch version is updated (on packages.json and Content/Versie.md)
  - The pdf version of the documents are created in the root folder
