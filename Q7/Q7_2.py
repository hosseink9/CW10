# In the name of GOD
import xml.etree.ElementTree as ET


book = ET.Element('book')
book_info = ET.SubElement(book, 'book_info')
title = ET.SubElement(book_info, 'title')
author = ET.SubElement(book_info, 'author')
year = ET.SubElement(book_info, 'year')

title.text = 'One Flew Over The Cuckoos Nest'
author.text = 'Ken Kesey'
year.text = '1962'

book = ET.ElementTree(book)
ET.indent(book, '\t')
book.write('../xml_files/books.xml')



