# Script to put the Pokemon Following spanish translation into the Following Renegade version

import xml.etree.ElementTree as ET
import json

comparisonFile = "output/comparisons/split/PokeRenegadeEn-PokeFollowingEn.json"
xmlFile = "xml/PokeFollowingRenegadeEs.xml"
translatedFile = "xml/PokeFollowingEs.xml"


with open(comparisonFile, "r", encoding="utf-8") as f:
    comparison = json.load(f)

# Open xml file
tree = ET.parse(xmlFile)
root = tree.getroot()

# Open translated file
translatedTree = ET.parse(translatedFile)
translatedRoot = translatedTree.getroot()

# go through "missing_in_1"
comparison = comparison["missing_in_1"]

# add manual translations
comparison["220"] = {
    "19": "NO",
    "20": "BATALLA",
    "21": "SIEMPRE",
    "47": "Utilícelo bajo su propio riesgo.\\nLa velocidad puede no ser constante.",
    "7": "DESBLOQUEO FPS"
}

for file_id, texts in comparison.items():
    # Find file with id=file_id
    fileElement = root.find('file[@id="{}"]'.format(file_id))
    if fileElement is None:
        print('Could not find file with id={}'.format(file_id))
        continue

    # Set change attribute to true
    fileElement.set('change', 'true')

    # Find translated file with id=file_id
    translatedFileElement = translatedRoot.find(
        'file[@id="{}"]'.format(file_id))
    if translatedFileElement is None:
        print('Could not find translated file with id={}'.format(file_id))
        continue

    for text_id, text in texts.items():
        # Find text with id=text_id
        textElement = fileElement.find('text[@id="{}"]'.format(text_id))
        if textElement is None:
            print('Could not find text with id={}'.format(text_id))
            continue

        # Find translated text with id=text_id
        translatedTextElement = translatedFileElement.find(
            'text[@id="{}"]'.format(text_id))
        if translatedTextElement is None:
            print('Could not find translated text with id={}'.format(text_id))
            continue

        textElement.text = translatedTextElement.text

# save xml file
tree.write(xmlFile, encoding="utf-16", short_empty_elements=False)
