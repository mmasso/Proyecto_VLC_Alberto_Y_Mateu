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
        print(composer.text)


def getlocationby(root):
    parent = root.getparent()
    location = (parent.tag).iter('location')
    location = location.text
    return location


def hacerdiccionario(root):
    diccionario = {}
    for artist in root.iter('artist'):
        nomArtist = artist.findtext('nom')
        for album in artist.iter('title'):
            titleAlbum = album.findtext('title')
            for track in album.iter('track'):
                trackName = track.findtext('name')
                path = track.findtext('path')
                genre = track.findtext('genre')
                composer = track.findtext('composer')
                diccionario[trackName] = {'localizacion': path,
                                          'artista': nomArtist,
                                          'album': titleAlbum,
                                          'genero': genre,
                                          'compositor': composer}
    return diccionario


print(hacerdiccionario(root))

# en vez de parsear el documento xml_vlc deberia servir para cualquier xml

