import pathlib
import re

def create_dictionary():
    with open("Content/Versie.md") as version_file:
        version = version_file.read().strip()
        print("{{VERSIE}}:{{" + version + "}}")
    path = pathlib.Path('Content/Maatregelen')
    for mdir in path.glob('*'):
        print("{{" + mdir.name + "}}:")

if __name__ == "__main__":
    create_dictionary()
