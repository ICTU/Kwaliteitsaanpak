# ICTU Kwaliteitsaanpak

ICTU's Kwaliteitsaanpak is a set of guidelines used at https://www.ictu.nl/ for software development projects. 

This repository contains the source information and automation scripts for generating ICTU's Kwaliteitsaanpak documentation.

## Authoring guidelines

- For each guideline
    - create a folder under ./Content/Maatregelen/(Processen | Producten | ProjectOrganisatie)
    - Add 3 files to the folder
        - Titel.md - guideline title
        - Maatregel.md - guideline description and rationale
        - ISR - guideline implementation at ICTU-ISR
- Add the maatregel to one or more document definitions

## Document definitions

- Each document definition is stored inside subfolder of ./DocumentDefinitions;
- A document definition is composed of 3 files:
    - document.md - list of guidelines composing a document
    - document.css - styling
    - document.json - document configuration
- The script instructions for building a new Document Definition have to be added to ./create-docs.sh;

## Generating the documentation (html & pdf)

- Clone this repository
- Run "docker-compose up"
    - The document patch version is updated (on packages.json and Content/Versie.md)
    - The md, html and pdf versions of the documents are created on the root folder
