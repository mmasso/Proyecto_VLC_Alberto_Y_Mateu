def dic_lista_paths(diccionario):
    assert isinstance(diccionario, dict)
    lista_vlc = []
    for currentSong in diccionario:
        lista_vlc.append([diccionario[currentSong]['order'], diccionario[currentSong]['localizacion']])
    lista_path = []
    lista_vlc.sort()
    for valor in lista_vlc:
        lista_path.append(valor[1])
    assert len(lista_path) == len(lista_vlc) == len(diccionario)
    assert lista_path != []
    return lista_path

