import xml.etree.ElementTree as ET
#part 1
mytree = ET.parse('data.xml')
myroot = mytree.getroot()

for element in myroot.findall('name'):
    print(element.text)

#part 2

root_tag = ET.Element('book')

title = ET.SubElement(root_tag, 'title')
author = ET.SubElement(root_tag, 'author')
year = ET.SubElement(root_tag, 'year')

title.text = "Python Programming"
author.text = "John Smith"
year.text = "2022"

root_tag = ET.tostring(root_tag)

with open("book.xml", "wb") as f:
    f.write(root_tag)


# part 3

mytree = ET.parse('book.xml')
myroot = mytree.getroot()

for child in myroot:
    if child.tag == "year":
        child.text = str(2023)

mytree.write('book.xml')