import xml.etree.ElementTree as ET
import json
import os


# def replace(xmlFile, fromFile, toFile):
def replace(xmlFile, jsonFile, reverse = False):
    # Parse the XML file
    tree = ET.parse(xmlFile)

    with open(jsonFile) as f:
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
            text_replace = texts.get('text1' if reverse else 'text2')
            if(text_replace is None or ""):
                print(f"text {text_id} of file {file_id} does not have a translation of {texts.get('text1' if reverse else 'text2')}")
                continue

            if len(text_replace) == 0:
                text_replace = texts.get('text2' if reverse else 'text1')
                if text_replace is None or len(text_replace) == 0:
                    print(f"{file_id}({text_id}) are both empty?")
            text_element.text = text_replace

    export_path = './output/results/' + os.path.basename(xmlFile)

    # os.makedirs(os.path.dirname(export_path), exist_ok=True)

    # Write the updated XML to a new file
    tree.write(xmlFile, encoding='utf-16', short_empty_elements=False)


# Pokémon Following English to Spanish changes in Pokémon Following English
replace('./xml/PokeFollowingEs.xml', 'output/comparisons/split/PokePlatinumEs-PokePlatinumEn.json', reverse = True)

# Pokémon Renegade English to Spanish changes in Pokémon Following Renegade English
replace('./xml/PokeFollowingRenegadeEs.xml', 'output/comparisons/split/PokeRenegadeEn-PokeRenegadeEs.json')

