# Convert all the xml into csv table with the file_id, text_id and the text for each file

import os
import csv

import xml_parser

# get all the xml files in the xml folder
xml_files = [f for f in os.listdir('./xml') if f.endswith('.xml')]
files = {}

# loop through all the xml files
for xml_file in xml_files:
    try:
        # parse the xml file
        files.update({ xml_file.split('.')[0]: xml_parser.parse_xml("./xml/" + xml_file)})
    except:
        print("Error parsing " + xml_file)
        continue

table = {}

outputFolder = "output/comparisons/"

# Check if the folder doesn't exists and create it
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

with open(outputFolder + "all_texts.csv", "w", newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=';')

    # Write the header row
    fieldnames = ["file", "text"] + list(files.keys())
    writer.writerow(fieldnames)
    
    for file, data in files.items():
        for file_id, texts in data.items():
            for text_id, text in texts.items():
                table.setdefault(file_id, {}).setdefault(text_id, {})[file] = text
    
    for file_id, texts in table.items():
        for text_id, text in texts.items():
            row = [file_id, text_id]
            for file in files.keys():
                row.append(text.get(file, ""))
            writer.writerow(row)
