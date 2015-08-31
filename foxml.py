from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime
import xml.etree.cElementTree as ET
from xml.dom import minidom

#root = ET.Element("root")
root = ET.Element("foxml:digitalObject")
root.set('xmlns:foxml','info:fedora/fedora-system:def/foxml#')
root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
root.set('xsi:schemaLocation', 'info:fedora/fedora-system:def/foxml# http://www.fedora.info/definitions/1/0/foxml1-1.xsd')
#doc = ET.SubElement(root, "doc")
op = ET.SubElement(root, "foxml:ObjectProperties")

#ET.SubElement(op, "foxml:property", name="info:fedora/fedora-system:def/model#state").text = "info:fedora/fedora-system:def/model#state"
ET.SubElement(op, "foxml:property", {'name':'info:fedora/fedora-system:def/model#state', 'value':'A'})
ET.SubElement(op, "foxml:property", {'name':'info:fedora/fedora-system:def/model#label', 'value':'FOXML Reference Example'})

#datastream
datastream = ET.SubElement(root, "foxml:datastream", {'ID':'DC', 'STATE':'A', 'CONTROL_GROUP':'X'})

tree = ET.ElementTree(root)
tree.write("filename.xml")