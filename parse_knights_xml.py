import lxml.etree as et

doc = et.parse('knights.xml')
print(doc)

root = doc.getroot()
print(root)

for knight in root:
    print(knight.get('name'))

b = doc.find('.//knight[@name="Bedevere"]')

print(b.find('color').text, b.findtext('quest'))

# for knight in doc.find('.//knight[comment[contains("peril")]]'):
#     print(knight.get('name'))

