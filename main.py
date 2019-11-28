from parser_xml import hacerdiccionario, root
from random_assign import random_assign
from paths_para_vlc import dic_lista_paths
from lista_al_vlc import lista_a_vlc


def main(hacerdiccionario):
    dic_canciones_orden_aleatorio = random_assign(hacerdiccionario)
    lista_paths_aleatorios = dic_lista_paths(dic_canciones_orden_aleatorio)
    comando_para_vlc = lista_a_vlc(lista_paths_aleatorios)
    return comando_para_vlc
