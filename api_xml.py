import xml.etree.ElementTree as ET

tree = ET.parse('xml_vlc.xml') # crear variable libreria_canciones (por ejemplo sin comillas) HACER MAIN.
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

# en vez de parsear el documento xml_vlc deberia servir para cualquier xml
# acceder a nombre artista, titulo del album, titulo cancion, el path de la cancion
# despues de conseguir cada cosa, creamos diccionario donde este cada cosa ordenanda segun el ejemplo