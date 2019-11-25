import xml.etree.ElementTree as ET

tree = ET.parse('xml_vlc.xml')
root = tree.getroot()

def get_all_nom(tree):
    for artists in root:
        for artist in artists:
            nom = artist.find('nom').text
            print(nom)

def get_all_nom_find_all(tree):
    nom = tree.findall('nom')
    print(nom)

def get_all_albums(tree):
    for artists in root:
        for artist in artists:
            for album in artist:
                titulo = album.find('title')
                print(titulo)

print(get_all_albums(tree))