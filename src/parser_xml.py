import xml.etree.ElementTree as ET


def hacer_diccionario(rutaXml):
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
        nom_artist = artist.findtext('nom')
        for album in artist.iter('album'):
            title_album = album.findtext('title')
            for track in album.iter('track'):
                track_name = track.findtext('name')
                path = track.findtext('path')
                genre = track.findtext('genre')
                composer = track.findtext('composer')
                diccionario[track_name] = {'localizacion': path,
                                          'artista': nom_artist,
                                          'album': title_album,
                                          'genero': genre,
                                          'compositor': composer}
    assert diccionario != {}
    return diccionario


# en vez de parsear el documento xml_vlc deberia servir para cualquier xml
# acceder a nombre artista, titulo del album, titulo cancion,
# el path de la cancion
# despues de conseguir cada cosa, creamos diccionario donde este cada
# cosa ordenanda segun el ejemplo
