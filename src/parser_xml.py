import xml.etree.ElementTree as ET


def hacerdiccionario(rutaXml):
    try:
        open(rutaXml)
    except OSError:
        print('No se puede abrir el archivo indicado')
        exit()
    else:
        pass
    tree = ET.parse(rutaXml)
    root = tree.getroot()
    diccionario = {}
    for artist in root.iter('artist'):
        nomArtist = artist.findtext('nom')
        for album in artist.iter('album'):
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
    assert diccionario != {}
    return diccionario


# en vez de parsear el documento xml_vlc deberia servir para cualquier xml
# acceder a nombre artista, titulo del album, titulo cancion,
# el path de la cancion
# despues de conseguir cada cosa, creamos diccionario donde este cada
# cosa ordenanda segun el ejemplo
