from random import choice


def random_assign(diccionario):
    assert isinstance(diccionario, dict)
    diccionarioRandomizado = diccionario.copy()
    contador_order = 0
    dic_aux = {}
    while contador_order < len(diccionarioRandomizado):
        randomSong = choice(list(diccionario))
        if diccionario[randomSong]['artista'] \
           and diccionario[randomSong]['album'] \
           and diccionario[randomSong]['genero'] \
           and diccionario[randomSong]['compositor'] \
           not in dic_aux:
            dic_aux = diccionario[randomSong]
            contador_order = contador_order + 1
            diccionarioRandomizado[randomSong]["order"] = contador_order
            diccionario.pop(randomSong)
    assert diccionarioRandomizado != []
    return diccionarioRandomizado
    
