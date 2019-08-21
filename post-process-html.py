""" Script to ensure that headers are kept together with the next paragraph by inserting them into a div
with the keep-together class. This class should have the page-breakinside: avoid CSS property. """

import re
import sys


class StateMachine:
    headings = tuple("<h{nr}".format(nr=nr) for nr in range(3, 7))

    def __init__(self):
        self.__state = self.default
        self.__in_bijlagen = False

    def default(self, line):
        """ While in the default state, look for headings we need to keep together with the first paragraph
            following it. """       
        if line.startswith('<h2 id="bijlagen">'):
            self.__in_bijlagen = True
        if line.startswith(self.headings):
            self.__state = self.keep_together
            yield '<div class="keep-together">'
        elif line == "<head>":
            self.__state = self.head
        line = self.styling(line)
        yield line

    def styling(self, line):
        line = line.replace("<p>@{", '<span class="maatregel"><p>')
        line = line.replace("}@", '</span>')
        #line = line.replace("<p>@{", '<p class="maatregel">')
        #line = line.replace("}@", '')
        line = self.bijlagen(line)
        return line

    def bijlagen(self, line):
        if self.__in_bijlagen:
            if line.startswith("<h3"):
                line = line.replace("<h3", '<h3 class="bijlage"')
            if line.startswith("<ol>"):
                line = line.replace("<ol>", '<ol class="bijlage">')
            if line.startswith("<h5") and "Risico: " in line:
                line = line.replace("<h5", '<h5 class="risk"')
        return line

    def keep_together(self, line):
        """ While in the keep-together state, look for the end of the paragraph. """
        line = self.styling(line)
        yield line
        if line.endswith("</p>"):
            self.__state = self.default
            yield "</div>"

    def head(self, line):
        """ Add extra content to the head. """
        self.__state = self.default
        yield '<meta charset="UTF-8">'
        yield line

    def process_line(self, line):
        """ Call the appropriate processor, depending on our current state. """
        for line in self.__state(line):
            yield line


def replace_chars(line):
    """ Replace some unicode characters with HTML. """
    line = line.replace("✔", '<i class="fas fa-check"></i>')  # Font Awesome Solid Checkmark
    line = line.replace("᠆", "-")  # Replace soft hyphen with hard hyphen because soft hyphens are ignored
    return re.sub("<li>([^\(]{,30}):", '<li><span class="label">\1</span>:', line)


sm = StateMachine()
for line in sys.stdin.readlines():
    for processed_line in sm.process_line(line.strip()):
        print(replace_chars(processed_line))
