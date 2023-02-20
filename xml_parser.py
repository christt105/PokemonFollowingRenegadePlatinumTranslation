import xml.etree.ElementTree as ET

def parse_xml(file_path):
    # Parse the XML file using ET.parse()
    tree = ET.parse(file_path)

    # Create a dictionary to store the files and their texts
    files_dict = {}

    # Loop through each <file> element in the XML
    for file_elem in tree.findall('file'):

        # Get the ID of the current file
        file_id = file_elem.get('id')

        # Create a dictionary to store the texts in the current file
        texts_dict = {}

        # Loop through each <text> element in the current file
        for text_elem in file_elem.findall('text'):

            # Get the ID and text of the current text element
            text_id = text_elem.get('id')
            text = text_elem.text.strip()

            # Add the ID and text as a dictionary to the texts dictionary
            texts_dict[text_id] = text

        # Add the file ID and texts dictionary as a dictionary to the files dictionary
        files_dict[file_id] = texts_dict

    return files_dict
