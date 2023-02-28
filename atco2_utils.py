#
# Utilities tailored for ATCO2 dataset
#
import xml.etree.ElementTree as ET
import re


def extract_text_from_xml(f_name):
    """
    Given an xml file name returns all the text extracted from the file

    Created to process ATCO2 xml files
    """
    tree = ET.parse(f_name)

    root = tree.getroot()

    all_text = ""

    for elem in root.iter():
        if elem.tag == "text":
            # replace [ with <
            new_text = elem.text.replace("[", "<")
            # replace ] with >
            new_text = new_text.replace("]", ">")

            # remove all chars between < >
            new_text = re.sub("<[^>]+>", "", new_text)

            all_text += new_text + " "

    return all_text
