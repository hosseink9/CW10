# In the name of GOD
import xml.etree.ElementTree as ET
from CW10.Q6 import dict_to_str

tree = ET.parse("../xml_files/Data.xml")
root1 = tree.getroot()


def tree_reader(root, tab=0):
    for child in root:
        print((tab * "\t") + f"{child.tag}: ",
              '\n' + f"{dict_to_str(child.attrib, len(child.tag)+4)}" if child.attrib else "",
              f"{child.text if child.text and not child.text.isspace() else ''}") #

        if child.tag:
            tree_reader(child, tab+1)


def attribute_finder(root, attribute_key):
    for child in root:
        if child.get('name'):
            yield child.get('name')
        attribute_finder(child, attribute_key)


def element_finder(root, element_key):
    for element in root.iter(element_key):
        yield element.text


if __name__ == '__main__':
    # tree_reader(root1)
    print(*list((attribute_finder(root1, 'name'))))
    print(*list((element_finder(root1, 'name'))))
    # for char in root1.itertext():
    #     print(char)



