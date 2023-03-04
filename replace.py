import xml.etree.ElementTree as ET
import json
import os

# Pokémon Renegade English to Spanish changes in Pokémon Following Renegade English

# Parse the XML file
file = 'xml/PokeFollowingRenegadeEs.xml'
tree = ET.parse(file)

with open('output/comparisons/PokeRenegadeEn-PokeRenegadeEs-split.json') as f:
    comparison = json.load(f)

# Loop through each file element
for file_id, text_dict in comparison["changed"].items():
    file_element = tree.find(f".//file[@id=\"{file_id}\"]")
    if file_element is None or "":
        print(f'Not able to find file with id: {file_id}')
        continue
    file_element.set("change", "true")

    for text_id, texts in text_dict.items():
        text_element = file_element.find(f".//text[@id=\"{text_id}\"]")
        if text_element is None:
            print(f'Not able to find text with id {text_id} in file {file_id}')
            continue
        text_replace = texts.get('text2')
        if(text_replace is None or ""):
            print(f"text {text_id} of file {file_id} does not have a translation of {texts.get('text1')}")
            continue

        if len(text_replace) == 0:
            text_replace = texts.get('text1')
            if text_replace is None or len(text_replace) == 0:
                print(f"{file_id}({text_id}) are both empty?")
        text_element.text = text_replace

export_path = './output/results/' + os.path.basename(file)

os.makedirs(os.path.dirname(export_path), exist_ok=True)

# Write the updated XML to a new file
tree.write(export_path, encoding='utf-16')

# Pokémon Following English to Spanish changes in Pokémon Following English

file = 'xml/PokeFollowingEs.xml'
tree = ET.parse(file)

with open('output/comparisons/PokeFollowingEn-PokeEn-split.json') as f:
