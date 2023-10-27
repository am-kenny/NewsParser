import requests
from bs4 import BeautifulSoup

from utils import create_xml, save_note

create_xml()

# BeautifulSoup
soup = BeautifulSoup(open("my_xml.xml"), "lxml-xml")
news = soup.find_all("entry")
doc_soup = open("my_soup_notes.txt", "w")


def parse_note(note):
    title_text = note.title.text
    link = note.link.attrs["href"]
    note_post = requests.get(link).content
    soup2 = BeautifulSoup(note_post, "lxml")
    abstract_text = soup2.find("p", {"class": "abstract"}).text

    return {
        "title_text": title_text,
        "link": link,
        "abstract_text": abstract_text
    }


for one_note in news:
    parsed_note = parse_note(one_note)
    save_note(parsed_note, doc_soup)
    print(parsed_note)
    print("_" * 50)









