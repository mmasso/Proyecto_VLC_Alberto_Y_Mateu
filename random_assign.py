from api_xml import diccionario
from random import choice

def random_assign(diccionario):
    diccionarioRandomizado = diccionario.copy()
    contador_order = 0
    while contador_order < len(diccionarioRandomizado):
        randomSong = choice(list(diccionario))
        '''if diccionario[randomSong]['artista']
        and diccionario[randomSong]['album']
        and diccionario[randomSong]['genero']
        and diccionario[randomSong]['compositor'] no coincide con el anterior:'''
        contador_order = contador_order + 1
        diccionarioRandomizado[randomSong]["order"] = contador_order
        diccionario.pop(randomSong)
    return (diccionarioRandomizado)

print(random_assign(diccionario))


'''        listaVLC = []
        listaVLC.append(diccionario[randomSong]['localizacion'])'''