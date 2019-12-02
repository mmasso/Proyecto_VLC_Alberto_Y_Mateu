from random import choice


def random_assign(diccionario):
    assert isinstance(diccionario, dict)
    diccionarioRandomizado = diccionario.copy()
    contador_order = 0
    dic_aux = {}
    while contador_order < len(diccionarioRandomizado):
        randomSong = choice(list(diccionario))
        if (diccionario[randomSong]['artista'] \
           and diccionario[randomSong]['album'] \
           and diccionario[randomSong]['genero'] \
           and diccionario[randomSong]['compositor'] \
           not in dic_aux) or (contador_order == len(diccionarioRandomizado) -1) :
            dic_aux = diccionario[randomSong]
            contador_order = contador_order + 1
            diccionarioRandomizado[randomSong]["order"] = contador_order
            diccionario.pop(randomSong)
    assert diccionarioRandomizado != []
    return diccionarioRandomizado
    
if __name__ == "__main__":
    assert isinstance(random_assign({"When It's All Gone": {'album': "When It's All Gone", 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\When_it_is_all_gone.mp3"'},
                           'Buried Alive': {'album': 'Buried Alive', 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\Buried_alive.mp3"'}}), dict)
    assert len(random_assign({"When It's All Gone": {'album': "When It's All Gone", 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\When_it_is_all_gone.mp3"'},
                           'Buried Alive': {'album': 'Buried Alive', 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\Buried_alive.mp3"'}})) == 2