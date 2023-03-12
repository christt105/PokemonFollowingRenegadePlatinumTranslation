# Script to know max characters in a line until a new line is added

import xml.etree.ElementTree as ET
import json
import re

# Load PokePlatinumEn.xml
tree = ET.parse('xml/PokePlatinumEn.xml')
root = tree.getroot()

# Load special_characters.json
with open('special_characters.json', 'r') as f:
    special_characters = json.load(f)

max_characters = 0
max_characters_texts = []

# ids of files that should be ignored
pass_ids = ["653", "345", "535"]

# go through all files
for file in root.findall('file'):

    if file.get("id") in pass_ids:
        continue

    print(file.get("id"))

    # go through all texts
    for textTree in file.findall('text'):
        # get text
        text = textTree.text.strip()

        if text is None or text == "" or text.find(r"\r") != -1:
            continue

        text = text.encode('ascii', 'ignore').decode()
        
        text = text.replace(r"\v0101\x0000\x0000", "0000000000") # Pokemon max characters
        text = text.replace(r"\v0101\x0001\x0000", "7777777") # Player name max characters

        if text == "":
            continue

        # split text by new line and iterate through each line
        for line in text.split(r"\n"):
            if line.find(r"\v") != -1 or line.find(r"\x") != -1:
                continue
            if len(line) > max_characters:
                max_characters = len(line)
                max_characters_texts = [line]
            elif len(line) == max_characters:
                max_characters_texts.append(line)

print("Max characters: {} on: {}".format(max_characters, max_characters_texts[0:5]))
        
        