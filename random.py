from diccionario_prueba import libreria


def add_order_dict():
    assert isinstance(libreria(), dict)
    canciones = libreria()
    contador_order = 0
    for key, valor in canciones:
        contador_order = contador_order + 1
        canciones.append[{"order": contador_order}]
    return canciones


print(add_order_dict())
