from parser_xml import hacer_diccionario
from random_assign import random_assign
from paths_para_vlc import dic_lista_paths
from lista_al_vlc import lista_a_vlc


def main(ruta_xml):
    assert isinstance(ruta_xml, str)
    diccionario_xml = hacer_diccionario(ruta_xml)
    dic_canciones_orden_aleatorio = random_assign(diccionario_xml)
    lista_paths_aleatorios = dic_lista_paths(dic_canciones_orden_aleatorio)
    comando_para_vlc = lista_a_vlc(lista_paths_aleatorios)
    return comando_para_vlc


if __name__ == "__main__":
    main("C:\\Users\\mateu\\Desktop\\Proyecto\\Proyecto_VLC_Alberto_Y_Mateu\\lib\\xml_vlc.xml")
