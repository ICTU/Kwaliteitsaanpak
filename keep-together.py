""" Script to ensure that headers are kept together with the next paragraph by inserting them into a div 
with the keep-together class. This class should have the page-breakinside: avoid CSS property. """

import sys


class StateMachine:
    headings = tuple("<h{nr}".format(nr=nr) for nr in range(3, 7))

    def default(self, line):
        if line.startswith(self.headings):
            print('<div class="keep-together">')
            print(line)
            return self.keep_together
        else:
            print(line)
            return self.default

    def keep_together(self, line):
        if line.endswith("</p>"):
            print(line)
            print("</div>")
            return self.default
        else:
            print(line)
            return self.keep_together


sm = StateMachine()
process_line = sm.default
for line in sys.stdin.readlines():
    process_line = process_line(line.strip())

