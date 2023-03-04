import json
import os
import csv
from deep_translator import GoogleTranslator, MyMemoryTranslator

# Function to extract special characters from text


def extract_special_chars(text):
    special_chars = []
    i = 0
    while i < len(text):
        if text[i:i+2] == "\\v":
            special_chars.append(text[i:i+10])
            i += 10
        elif text[i:i+2] == "\\x":
            special_chars.append(text[i:i+6])
            i += 6
        elif text[i:i+2] == "\\n":
            special_chars.append(text[i:i+2])
            i += 2
        else:
            i += 1
    return special_chars

# Function to convert special characters to words


def convert_special_chars_to_words(text, special_chars):
    text = text.replace("\\n", " ")

    for key, word in special_chars.items():
        text = text.replace(key, word)

    return text


def translate_text(text, translator="google"):
    if translator == "google":
        translation = GoogleTranslator(source="en", target="es").translate(text)
    elif translator == "mymemory":
        translation = MyMemoryTranslator(source="en", target="es").translate(text)
    else:
        print("Invalid translator")
        return None

    return translation


with open("special_characters.json") as special_chars_file:
    special_chars = json.load(special_chars_file)

with open("output/comparisons/PokePlatinumEn-PokeFollowingEn.json") as f:
    data = json.load(f)
    translations = {}
    for key, value in data["724"].items():
        # for special_char in extract_special_chars(value["text2"]):
        #     if special_char not in special_chars:
        #         special_chars.append(special_char)

        text = value.get("text2")

        if text is None or text == "":
            continue

        text = convert_special_chars_to_words(text, special_chars)
        print(text)

        translation = translate_text(text)

        if translation is not None:
            translations[key] = translation

if not os.path.exists("./output/results/translated/"):
    os.mkdir("./output/results/translated/")

with open(f"output/results/translated/724.csv", "w", newline='', encoding='utf-8') as outfile:
    fieldnames = ["id", "original", "translated"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    for key, value in translations.items():
        writer.writerow({"id": key, "original": data["724"][key]["text2"], "translated": value})
