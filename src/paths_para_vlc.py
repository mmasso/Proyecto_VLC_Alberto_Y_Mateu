def dic_lista_paths(diccionario):
    assert isinstance(diccionario, dict)
    lista_vlc = []
    for currentSong in diccionario:
        lista_vlc.append([diccionario[currentSong]['order'],
                         diccionario[currentSong]['localizacion']])
    lista_path = []
    lista_vlc.sort()
    for valor in lista_vlc:
        lista_path.append(valor[1])
    assert len(lista_path) == len(lista_vlc) == len(diccionario)
    assert lista_path != []
    return lista_path


if __name__ == "__main__":
    assert len(dic_lista_paths({"When It's All Gone": {'album': "When It's All Gone", 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop', 'order': '1',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\When_it_is_all_gone.mp3"'},
                           'Buried Alive': {'album': 'Buried Alive', 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop', 'order': '2',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\Buried_alive.mp3"'}})) == 2