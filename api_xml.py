import xml.etree.ElementTree as ET


tree = ET.parse('xml_vlc.xml') # crear variable libreria_canciones (por ejemplo sin comillas) HACER MAIN. 
root = tree.getroot()


def get_all_name_artist(root):
    for nom in root.iter('nom'):
        print(nom.text)


def get_all_album_titles(root):
    for title in root.iter('title'):
        print(title.text) 


def get_all_name_track(root):
    for name in root.iter('name'):
        print(name.text)


def get_paths(root):
    for path in root.iter('path'):
        print(path.text)


def get_all_genres(root):
    for genre in root.iter('genre'):
        print(genre.text)


def get_all_composers(root):
    for composer in root.iter('composer'):
        print (composer.text)


get_all_composers(root)

# en vez de parsear el documento xml_vlc deberia servir para cualquier xml

