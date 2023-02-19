import xml.etree.ElementTree as ET
import argparse
import os


def compare_xml_files(file1, file2, output_file):
    # parse the two XML files
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    # get the root elements of the two trees
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # create the directory for the output file if it does not exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as f:
        # iterate through all the <file> nodes
        for file1_node, file2_node in zip(root1.findall('file'), root2.findall('file')):
            # iterate through all the <text> nodes in the current <file> node
            for text1_node, text2_node in zip(file1_node.findall('text'), file2_node.findall('text')):
                # compare the text content of the two <text> nodes
                if text1_node.text != text2_node.text:
                    # write the differences to the output file
                    f.write(
                        f"File {file1_node.get('id')}, Text {text1_node.get('id')}:\n")
                    f.write(f"  {file1}: {text1_node.text.strip()}\n")
                    f.write(f"  {file2}: {text2_node.text.strip()}\n")
                    f.write("\n")



parser = argparse.ArgumentParser(description='Compare two XML files.')
parser.add_argument('file1',nargs='?', default='xml/PokeRenegadeEn.xml', type=str, help='path to first XML file')
parser.add_argument('file2',nargs='?', default='xml/PokeRenegadeEs.xml', type=str, help='path to second XML file')
args = parser.parse_args()

compare_xml_files(args.file1, args.file2, "output/" + os.path.splitext(os.path.basename(args.file1))[0] + "-" + os.path.splitext(os.path.basename(args.file2))[0] + '.txt')
