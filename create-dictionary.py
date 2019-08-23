import sys
import pathlib
import re

def create_link(name):
    link=name.lower()
    link=link.replace(" ", "-")
    link=link.replace(":", "-")
    link=link.replace("(", "-")
    link=link.replace(")", "-")
    link=link.replace(",", "-")
    link=link.replace("--", "-")
    return link

def read_maatregel(path, do_create_link):
    maatregel_path = path / "Maatregel.md"
    with open(maatregel_path, mode='r', encoding='utf8') as maatregel_file:
        headers = [line.strip("###").strip(path.name+":").strip() for line in maatregel_file if line.startswith('### ')]
    for header in headers:
        if do_create_link:
            print("{{" + path.name + "}}=[**" + header + "**](#" + create_link(header) + ")")
        else:
            print("{{" + path.name + "}}=**" + header + "**")
        print("{{" + path.name + "-no-link}}=**" + header + "**")

def create_dictionary(do_create_links):
    with open("Content/Versie.md") as version_file:
        version = version_file.read().strip()
        print("{{VERSIE}}=" + version)
    path = pathlib.Path('Content/Maatregelen')
    for mdir in sorted(path.glob('M*')):
        if mdir.is_dir():
            read_maatregel(mdir, do_create_links)
    print("{{DUMMY}}=DUMMY")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    do_create_links = False
    if len(arguments) >= 1:
        do_create_links = arguments[0] in ("--link", "-l")
    create_dictionary(do_create_links)
