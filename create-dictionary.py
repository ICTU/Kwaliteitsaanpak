import pathlib
import re

def read_maatregel(path):
    maatregel_path = path / "Maatregel.md"
    with open(maatregel_path, mode='r', encoding='utf8') as maatregel_file:
        headers = [line.strip("###").strip(path.name+":").strip() for line in maatregel_file if line.startswith('### ')]
    for header in headers:
        print("{{" + path.name + "}}=**" + header + "**")

def create_dictionary():
    with open("Content/Versie.md") as version_file:
        version = version_file.read().strip()
        print("{{VERSIE}}=" + version)
    path = pathlib.Path('Content/Maatregelen')
    for mdir in sorted(path.glob('M*')):
        if mdir.is_dir():
            read_maatregel(mdir)

if __name__ == "__main__":
    create_dictionary()
