import requests


def create_xml():
    my_xml = requests.get("https://scipost.org/atom/publications/comp-ai")
    open("my_xml.xml", "wb").write(my_xml.content)


def save_note(note, document):
    document.write(f"{note.get('title_text')}\n{note.get('link')}\n{note.get('abstract_text')}\n{'_'*50}\n")