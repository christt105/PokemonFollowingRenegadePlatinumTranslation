import xml.etree.ElementTree as ET
import argparse
import os

parser = argparse.ArgumentParser(description='Compare two XML files')
parser.add_argument('file1', help='first XML file')
parser.add_argument('file2', help='second XML file')
args = parser.parse_args()

output_file_name = f"output/{os.path.splitext(os.path.basename(args.file1))[0]}-{os.path.splitext(os.path.basename(args.file2))[0]}.txt"

os.makedirs(os.path.dirname(output_file_name), exist_ok=True)

tree1 = ET.parse(args.file1)
tree2 = ET.parse(args.file2)
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    processed_ids = set()  # set of (file_id, text_id) tuples that have been processed
    for file1, file2 in zip(tree1.iter('file'), tree2.iter('file')):
        file_id = file1.get('id')
        processed_ids.add((file_id, None))
        for text1, text2 in zip(file1.iter('text'), file2.iter('text')):
            text_id = text1.get('id')
            processed_ids.add((file_id, text_id))
            if text1.text != text2.text:
                output_file.write(f'File {file_id}, Text {text_id}:')
                output_file.write(f'  {text1.text}  {text2.text}\n')
        # check for any additional texts in file2
        for text2 in file2.iter('text'):
            text_id = text2.get('id')
            if (file_id, text_id) not in processed_ids:
                output_file.write(                    f'File {file_id}, Text {text_id} not in {args.file1}\n')
                output_file.write(f'  {text2.text}\n')
    # check for any additional files in tree2
    for file2 in tree2.iter('file'):
        file_id = file2.get('id')
        if (file_id, None) not in processed_ids:
            output_file.write(f'File {file_id} not in {args.file1}\n')
        # check for any additional texts in file2
        for text2 in file2.iter('text'):
            text_id = text2.get('id')
            if (file_id, text_id) not in processed_ids:
                output_file.write(
                    f'File {file_id}, Text {text_id} not in {args.file1}\n')
                output_file.write(f'  {text2.text}\n')
