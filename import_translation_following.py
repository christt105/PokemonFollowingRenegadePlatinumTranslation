import json
import xml.etree.ElementTree as ET
import csv

manual_translations = {
    "220": {
        "19": "NO",
        "20": "BATALLA",
        "21": "SIEMPRE",
        "47": "Utilícelo bajo su propio riesgo.\\nLa velocidad puede no ser constante.",
        "7": "DESBLOQUEO FPS"
    },
    "609": {
        "0": "\n"
    },
    "213": {
        "132": "¡\\v0103ぁ\\x0000\\x0000 se siente mejor, así que\\ndecidiste llevarte a \\v0103ぁ\\x0000\\x0000 contigo!\r"
    }
}

# Open xml file
tree = ET.parse('xml/PokeFollowingEs.xml')
root = tree.getroot()

# Find file with id=724
file724 = root.find('file[@id="724"]')

if file724 is None:
    print('Could not find file with id=724')
    exit(1)

# Set change attribute to true
file724.set('change', 'true')

# Load special_characters.json
with open('special_characters.json', 'r') as f:
    special_characters = json.load(f)

new_line_at = 38


def split_text(text, new_line_at):
    lines = []
    while len(text) > new_line_at:
        # Find the last space within the limit of new_line_at
        last_space = text[:new_line_at].rfind(' ')
        if last_space == -1:  # If no space is found, split at new_line_at anyway
            last_space = new_line_at
        lines.append(text[:last_space])
        text = text[last_space+1:]  # Skip the space character
    lines.append(text)
    return '\\n'.join(lines)


lines_to_review = []

# Open csv file
with open('output/translated/Following_724.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        # Find text with id=row['id']
        text = file724.find('text[@id="{}"]'.format(row['id']))
        if text is None:
            print('Could not find text with id={}'.format(row['id']))
            continue

        translated = row['translated']

        if translated == "":
            continue

        translated = translated.replace('{Pokémon}', "{Pokemon}")
        translated = translated.replace('{Tú}', "{You}")

        # Pokémon names have 10 characters
        translated = translated.replace("{Pokemon}", "0000000000")
        # Player name has 7 characters
        translated = translated.replace("{You}", "7777777")

        # Split text by new line
        translated = translated.replace("...... ", "......\\n")
        if translated.find(r"{DownArrow}") != -1:
            lines_to_review.append(row['id'] + ": " + translated)
        else:
            translated = split_text(translated, new_line_at)

        translated = translated.replace("0000000000", "{Pokemon}")
        translated = translated.replace("7777777", "{You}")

        # Replace special characters
        for key, value in special_characters.items():
            translated = translated.replace(value, key)

        text.text = translated


print("Finished the translation of file 724.")


# Apply manual translations
for file_id, texts in manual_translations.items():
    file = root.find('file[@id="{}"]'.format(file_id))
    if file is None:
        print('Could not find file with id={}'.format(file_id))
        continue
    # Set change attribute to true
    file.set('change', 'true')
    for text_id, text_value in texts.items():
        text = file.find('text[@id="{}"]'.format(text_id))
        if text is None:
            print('Could not find text with id={} in file {}'.format(
                text_id, file_id))
            continue
        text.text = text_value


# save xml file
tree.write('xml/PokeFollowingEs.xml', encoding='utf-16', short_empty_elements=False)

print("Please review lines:" + str(lines_to_review))
