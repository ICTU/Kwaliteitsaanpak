# ICTU Kwaliteitsaanpak Softwareontwikkeling

[ICTU's Kwaliteitsaanpak](https://www.ictu.nl/kwaliteitsaanpak) is a set of guidelines used at [ICTU](https://www.ictu.nl) for software development projects. It is only available in Dutch, sorry.

This repository contains the source information and automation scripts for generating ICTU's Kwaliteitsaanpak documentation. The Kwaliteitsaanpak itself is available via [https://ictu.github.io/Kwaliteitsaanpak](https://ictu.github.io/Kwaliteitsaanpak).

## Documents

The Kwaliteitsaanpak consists of a main document containing the Kwaliteitsaanpak itself, a number of templates, and a self-assessment checklist. The sources are a collection of Markdown files and supporting material. Scripts convert the Kwaliteitsaanpak main document to html, the templates to docx, and the self-assessment checklist to xslx.

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
- Run `open html/index.html` to view the latest release and the work in progress (wip)

## Releasing a new version of the documentation

1. Create a release branch: `git checkout -b release-vx-y-z`
2. Update the version number and release date in the change log in `./Content/Wijzigingsgeschiedenis.md``
3. Create a new release folder in ./docs: `mkdir docs/vx.y.z`
4. Update the version number in `docs/index.html`
5. Update the version number in `pyproject.toml`
6. Run `VERSION=x.y.z docker compose up` to generate the documents
7. Commit the changes and push to GitHub: `git commit -a -m "Release vx.y.z"; git push`
8. Review and merge the branch on GitHub
9. Tag the release and push the tag to GitHub: `git checkout master; git pull -p; git tag vx.y.z; git push --tags`
10. Announce the release in MS Teams channel "ICTU Softwareontwikkeling/Algemeen". In case of a minor release, also mail the SDM'ers. In case of a major release, also email everyone at ISE.

## Point of contact

Points of contact for the ICTU Kwaliteitsaanpak Softwareontwikkeling and this repository are [Birgitte Plasse](https://github.com/bipla2) and [Frank Niessink](https://github.com/fniessink).
