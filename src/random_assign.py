from random import choice


def random_assign(diccionario):
    assert isinstance(diccionario, dict)
    longitudOriginal = len(diccionario)
    diccionario_randomizado = diccionario.copy()
    contador_order = 0
    dic_aux = {}
    while contador_order < len(diccionario_randomizado):
        random_song = choice(list(diccionario))
        if (diccionario[random_song]['artista'] \
           and diccionario[random_song]['album'] \
           and diccionario[random_song]['genero'] \
           and diccionario[random_song]['compositor'] \
           not in dic_aux) or (contador_order == len(diccionario_randomizado) -1) :
            dic_aux = diccionario[random_song]
            contador_order = contador_order + 1
            diccionario_randomizado[random_song]["order"] = contador_order
            diccionario.pop(random_song)
    assert diccionario_randomizado != {}
    assert len(diccionario_randomizado) == longitudOriginal
    return diccionario_randomizado


if __name__ == "__main__":
    assert len(random_assign({"When It's All Gone": {'album': "When It's All Gone", 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\When_it_is_all_gone.mp3"'},
                           'Buried Alive': {'album': 'Buried Alive', 'artista': 'Terror Reid',
                           'compositor': 'Getter', 'genero': 'Hip hop',
                           'localizacion': '"C:\\Users\\mateu\\Desktop\\CancionesVLC\\Buried_alive.mp3"'}})) == 2