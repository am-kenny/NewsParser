import requests
from lxml import etree

from utils import create_xml, save_note

create_xml()

# lxml
namespace = {'atom': 'http://www.w3.org/2005/Atom'}
doc_lxml = open("my_lxml_notes.txt", "w")


def parse_lxml_note(note):
    title_text = note.xpath("atom:title", namespaces=namespace)[0].text
    link = note.xpath("atom:link", namespaces=namespace)[0].attrib["href"]
    note_post = requests.get(link).content
    tree2 = etree.HTML(note_post)
    abstract_text = tree2.xpath("/html/body/main/div[3]/div/p")[0].text

    return {
        "title_text": title_text,
        "link": link,
        "abstract_text": abstract_text
    }


tree = etree.fromstring(open("my_xml.xml", "rb").read())
items = tree.xpath("/atom:feed/atom:entry", namespaces=namespace)
for itm in items:
    parsed_note = parse_lxml_note(itm)
    save_note(parsed_note, doc_lxml)
    print(parsed_note)
    print("_" * 50)
