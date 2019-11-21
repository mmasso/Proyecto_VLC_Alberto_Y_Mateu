from diccionario_prueba import libreria


def add_order_dict(libreria):
    assert isinstance(libreria, dict)
    contador_order = 0
    ord_libreria = libreria.copy()
    for key in libreria:
        contador_order = contador_order + 1
        ord_libreria[key]["order"] = contador_order
    assert ord_libreria != 0
    return ord_libreria


print(add_order_dict(libreria))