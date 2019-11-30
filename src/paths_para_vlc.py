def dic_lista_paths(diccionario):
    assert isinstance(diccionario, dict)
    listaVLC = []
    contador = 1
    while contador < len(diccionario):
        for currentSong in diccionario:
            if diccionario[currentSong]['order'] == contador:
                contador = contador + 1
                listaVLC.append(diccionario[currentSong]['localizacion'])
    assert listaVLC != []
    return listaVLC

    #crear lista de tuplas orden localizacion, hacer sort i scar lista de localizacion.
