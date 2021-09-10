import lxml.etree as et

root = et.Element("knights")

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight = et.SubElement(root, 'knight', name=name)
        et.SubElement(knight, 'title').text = title
        color_tag = et.SubElement(knight, 'color')
        color_tag.text = color
        et.SubElement(knight, 'quest').text = quest
        et.SubElement(knight, 'comment').text = comment


xml_doc = et.tostring(root, pretty_print=True, xml_declaration=True,
                      encoding="utf-8")
print(xml_doc.decode())

doc = et.ElementTree(root)

doc.write('knights.xml', pretty_print=True, xml_declaration=True)






