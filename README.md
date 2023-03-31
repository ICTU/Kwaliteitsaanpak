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

## Generating the documentation

- Make sure you have Docker
- Clone this repository
- Run `docker compose up`
- View the documents in the docs/wip folder

## Releasing a new version of the documentation

1. Create a release branch: `git checkout -b releaseX-Y-Z`
2. Update the version number and release date in the change log in ./Content/Bijlagen/Wijzigingsgeschiedenis.md
3. Update the version number in ./docker-compose.yml
4. Update the version number in docs/index.html
5. Create a new release folder in ./docs: `mkdir docs/vX.Y.Z`
6. Run `docker compose up` to generate the documents
7. Copy the generated documents from the wip folder to folder for the new version: `cp docs/wip/* docs/vX.Y.Z`
8. Commit the changes and push to GitHub: `git commit -a -m "Release vX.Y.Z"; git push`
9. Review and merge the branch on GitHub
10. Tag the release and push the tag to GitHub: `git checkout master; git pull -p; git tag vX.Y.Z; git push --tags`

## Point of contact

Points of contact for the ICTU Kwaliteitsaanpak Softwareontwikkeling and this repository are [Auke Bloembergen](https://github.com/aukebloembergen) and [Frank Niessink](https://github.com/fniessink).
