import xml.etree.ElementTree as ET
import os
from xml_parser import parse_xml
import json

comparison_files = [
    ['xml/PokeFollowingEn.xml', 'xml/PokeFollowingRenegadeEn.xml'],
    ['xml/PokePlatinumEs.xml', 'xml/PokePlatinumEn.xml'],
    ['xml/PokePlatinumEn.xml', 'xml/PokeFollowingRenegadeEn.xml'],
    ['xml/PokePlatinumEn.xml', 'xml/PokeFollowingEn.xml'],
    ['xml/PokeRenegadeEn.xml', 'xml/PokeRenegadeEs.xml'],
    ['xml/PokeRenegadeEn.xml', 'xml/PokeFollowingEn.xml'],
    ['xml/PokeFollowingEs.xml', 'xml/PokeFollowingEn.xml'],
]

def compare_files(files_dict1, files_dict2):
    result = {}

    # Loop through all files in files_dict1
    for file_id, texts_dict1 in files_dict1.items():
        # Check if the file exists in files_dict2
        if file_id not in files_dict2:
            # Add all texts in texts_dict1 to the result with None for text2
            for text_id, text1 in texts_dict1.items():
                result.setdefault(file_id, {})[text_id] = {
                    "text1": text1,
                    "text2": None
                }
            continue

        # Get the texts dictionary for the current file in files_dict2
        texts_dict2 = files_dict2[file_id]

        # Loop through all texts in texts_dict1
        for text_id, text1 in texts_dict1.items():
            # Check if the text exists in texts_dict2
            if text_id not in texts_dict2:
                # Add the text from text_dict1 to the result with None for text2
                result.setdefault(file_id, {})[text_id] = {
                    "text1": text1,
                    "text2": None
                }
                continue

            # Get the text for the current text_id in texts_dict2
            text2 = texts_dict2[text_id]

            # Compare the text from both files
            if text1 != text2:
                result.setdefault(file_id, {})[text_id] = {
                    "text1": text1,
                    "text2": text2
                }

    for file_id, texts_dict2 in files_dict2.items():
        # Check if the file exists in files_dict1
        if file_id not in files_dict1:
            # Add all texts in texts_dict2 to the result with None for text1
            for text_id, text2 in texts_dict2.items():
                result.setdefault(file_id, {})[text_id] = {
                    "text1": None,
                    "text2": text2
                }
            continue

        texts_dict1 = files_dict1[file_id]

        for text_id, text2 in texts_dict2.items():
            if text_id not in texts_dict1:
                result.setdefault(file_id, {})[text_id] = {
                    "text1": None,
                    "text2": text2
                }
        
    return result

def compare_files_split(files_dict1, files_dict2):
    result = {
        "changed": {},
        "missing_in_1": {},
        "missing_in_2": {}
    }

    # Loop through all files in files_dict1
    for file_id, texts_dict1 in files_dict1.items():
        # Check if the file exists in files_dict2
        if file_id not in files_dict2:
            # Add all texts in texts_dict1 to the missing_in_2 section
            for text_id, text1 in texts_dict1.items():
                result["missing_in_2"].setdefault(file_id, {})[text_id] = {
                    "text1": text1,
                    "text2": None
                }
            continue

        # Get the texts dictionary for the current file in files_dict2
        texts_dict2 = files_dict2[file_id]

        # Loop through all texts in texts_dict1
        for text_id, text1 in texts_dict1.items():
            # Check if the text exists in texts_dict2
            if text_id not in texts_dict2:
                # Add the text from text_dict1 to the missing_in_2 section
                result["missing_in_2"].setdefault(file_id, {})[text_id] = {
                    "text1": text1,
                    "text2": None
                }
                continue

            # Get the text for the current text_id in texts_dict2
            text2 = texts_dict2[text_id]

            # Compare the text from both files
            if text1 != text2:
                # Add the text from both files to the changed section
                result["changed"].setdefault(file_id, {})[text_id] = {
                    "text1": text1,
                    "text2": text2
                }

    for file_id, texts_dict2 in files_dict2.items():
        # Check if the file exists in files_dict1
        if file_id not in files_dict1:
            # Add all texts in texts_dict2 to the missing_in_1 section
            for text_id, text2 in texts_dict2.items():
                result["missing_in_1"].setdefault(file_id, {})[text_id] = {
                    "text1": None,
                    "text2": text2
                }
            continue

        texts_dict1 = files_dict1[file_id]

        for text_id, text2 in texts_dict2.items():
            if text_id not in texts_dict1:
                # Add the text from text_dict2 to the missing_in_1 section
                result["missing_in_1"].setdefault(file_id, {})[text_id] = {
                    "text1": None,
                    "text2": text2
                }
        
    return result


def get_file_name(path):
    return os.path.splitext(os.path.basename(path))[0]

for files in comparison_files:
    xml1 = parse_xml(files[0])
    xml2 = parse_xml(files[1])

    # TODO: Better a csv?
    output_folder = f"output/comparisons/"
    merge_folder = output_folder + "merge/"
    split_folder = output_folder + "split/"
    output_file_name = f"{get_file_name(files[0])}-{get_file_name(files[1])}"

    os.makedirs(os.path.dirname(merge_folder), exist_ok=True)
    os.makedirs(os.path.dirname(split_folder), exist_ok=True)

    with open(merge_folder + output_file_name+'.json', 'w', encoding='utf-8') as f:
        json.dump(compare_files(xml1, xml2), f, indent=4)

    with open(split_folder + output_file_name + '.json', 'w', encoding='utf-8') as f:
        json.dump(compare_files_split(xml1, xml2), f, indent=4)

