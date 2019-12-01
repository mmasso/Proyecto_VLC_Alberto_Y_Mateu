def dic_lista_paths(diccionario):
    assert isinstance(diccionario, dict)
    listaVLC = []
    '''
    contador = 1
    while contador < len(diccionario):
        for currentSong in diccionario:
            if diccionario[currentSong]['order'] == contador:
                contador = contador + 1
                listaVLC.append(diccionario[currentSong]['localizacion'])
    assert listaVLC != []
    return listaVLC
    '''
    for currentSong in diccionario:
        listaVLC.append([diccionario[currentSong]['order'], diccionario[currentSong]['localizacion']])
    listaPath = []
    listaVLC.sort()
    for valor in listaVLC:
        listaPath.append(valor[1])
    assert len(listaPath) == len(listaVLC) == len(diccionario)
    assert listaPath != []
    return listaPath
    # crear lista de tuplas orden localizacion, hacer sort i scar lista de localizacion.
