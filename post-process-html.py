""" Script to ensure that headers are kept together with the next paragraph by inserting them into a div
with the keep-together class. This class should have the page-breakinside: avoid CSS property. """

import sys


class StateMachine:
    headings = tuple("<h{nr}".format(nr=nr) for nr in range(3, 7))

    def __process_line(self, *lines):
        """ Process one ore more lines. Replace some specific unicode characters and add the UTF-8 charset
            to the head. """
        for line in lines:
            line = line.replace("✔", '<i class="fas fa-check"></i>')  # Font Awesome Solid Checkmark
            line = line.replace("᠆", "-")  # Replace soft hyphen with hard hyphen because soft hyphens are ignored
            print(line)

    def default(self, line):
        """ While in the default state, look for headings we need to keep together with the first paragraph
            following it. """
        if line.startswith(self.headings):
            self.__process_line('<div class="keep-together">', line)
            return self.keep_together
        self.__process_line(line)
        return self.head if line == "<head>" else self.default

    def keep_together(self, line):
        """ While in the keep-together state, look for the end of the paragraph. """
        if line.endswith("</p>"):
            self.__process_line(line, "</div>")
            return self.default
        else:
            self.__process_line(line)
            return self.keep_together

    def head(self, line):
        """ Add extra content to the head. """
        self.__process_line('<meta charset="UTF-8">', line)
        return self.default


sm = StateMachine()
process_line = sm.default
for line in sys.stdin.readlines():
    process_line = process_line(line.strip())
