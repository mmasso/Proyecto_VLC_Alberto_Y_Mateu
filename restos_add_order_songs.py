from api_xml import diccionario

def add_order_dict(diccionario):
    assert isinstance(diccionario, dict)
    contador_order = 0
    ord_diccionario = diccionario.copy()
    for key in diccionario:
        contador_order = contador_order + 1
        ord_diccionario[key]["order"] = contador_order
    assert ord_diccionario != 0
    return ord_diccionario

order_canciones = add_order_dict(diccionario) 