# In the name of GOD
import xml.etree.ElementTree as ET

tree = ET.parse('../xml_files/books.xml')
root = tree.getroot()

for element in root.iter('year'):
    element.text = '1996'
    element.set('updated', 'true')

tree.write('../xml_files/updated_books.xml')
