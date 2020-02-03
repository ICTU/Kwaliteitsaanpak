import sys
import pathlib
import re
import fileinput

KEY_PATTERN=r"^\{\{[\w-]+\}\}"
QUOTE="\""

def read_dictionary(dictionary_file_name):
    dictionary = {}
    with open(dictionary_file_name) as dictionary_file:
        line = dictionary_file.readline()
        cnt = 1
        while line:
            line = line.strip()
            if len(line) > 0:
                source_line = line        
                m = re.search(KEY_PATTERN, line)
                valid_pair = False
                if m:
                    key = m.group()
                    line = re.sub(KEY_PATTERN, "", line, 1).strip()
                    if re.search("^=", line):
                        value = re.sub("^=", "", line, 1).strip()
                        if value.startswith(QUOTE) and value.endswith(QUOTE):
                            value = value.rstrip(QUOTE).lstrip(QUOTE)
                        if key and value:
                            dictionary[key] = value
                            valid_pair = True
                if not valid_pair:
                    sys.stderr.write(f"Invalid key-value pair (line {cnt}): {source_line}\n")
            line = dictionary_file.readline()
            cnt = cnt + 1
    return dictionary

def map_dictionary(input_file_name, dictionary_file_name):
    dictionary = read_dictionary(dictionary_file_name)
    with open(input_file_name) as input_file:
        line = input_file.readline()
        while line:
            for key in dictionary:
                line = line.replace(key, dictionary[key])
            print(line, end="")
            line = input_file.readline()
   
if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) == 2:
        input_file_name = arguments[0]
        dictionary_file_name = arguments[1]
        map_dictionary(input_file_name, dictionary_file_name)
    else:
        sys.stderr.write("USAGE: map <input file> <dictionary file>")
